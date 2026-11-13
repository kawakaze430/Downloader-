"""Standard-library regression checks for the download test server."""

import hashlib
import http.client
import threading
import unittest
from http.server import ThreadingHTTPServer

from tools.fixtures.http_fixture import (
    PAYLOAD,
    PAYLOAD_SHA256,
    FixtureRequestHandler,
    parse_single_range,
)


class RangeParserTests(unittest.TestCase):
    def test_ranges(self):
        self.assertEqual(parse_single_range("bytes=0-10", 100), (0, 10))
        self.assertEqual(parse_single_range("bytes=20-", 100), (20, 99))
        self.assertEqual(parse_single_range("bytes=-5", 100), (95, 99))
        self.assertEqual(parse_single_range("bytes=-200", 100), (0, 99))
        self.assertEqual(parse_single_range("bytes=90-500", 100), (90, 99))

    def test_invalid_ranges(self):
        for header in ("bytes=-0", "bytes=-", "bytes=5-4", "bytes=100-", "bytes=0-1,3-4", "items=0-5"):
            with self.subTest(header=header):
                self.assertIsNone(parse_single_range(header, 100))


class DownloadFixtureTests(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        cls.server = ThreadingHTTPServer(("127.0.0.1", 0), FixtureRequestHandler)
        cls.server.daemon_threads = True
        cls.thread = threading.Thread(target=cls.server.serve_forever, daemon=True)
        cls.thread.start()

    @classmethod
    def tearDownClass(cls):
        cls.server.shutdown()
        cls.server.server_close()
        cls.thread.join(timeout=3)

    def request(self, path, headers=None, method="GET"):
        connection = http.client.HTTPConnection("127.0.0.1", self.server.server_port, timeout=3)
        try:
            connection.request(method, path, headers=headers or {})
            response = connection.getresponse()
            return response.status, dict(response.getheaders()), response.read()
        finally:
            connection.close()

    def test_full_download_and_sha256(self):
        status, headers, body = self.request("/file.bin")
        self.assertEqual(status, 200)
        self.assertEqual(headers["Accept-Ranges"], "bytes")
        self.assertEqual(len(body), 16384)
        self.assertEqual(body, PAYLOAD)
        self.assertEqual(hashlib.sha256(body).hexdigest(), PAYLOAD_SHA256)

    def test_partial_download_reassembles_without_corruption(self):
        first = self.request("/file.bin", {"Range": "bytes=0-8191"})
        second = self.request("/file.bin", {"Range": "bytes=8192-"})
        self.assertEqual((first[0], second[0]), (206, 206))
        self.assertEqual(first[1]["Content-Range"], "bytes 0-8191/16384")
        self.assertEqual(second[1]["Content-Range"], "bytes 8192-16383/16384")
        self.assertEqual(hashlib.sha256(first[2] + second[2]).hexdigest(), PAYLOAD_SHA256)

    def test_suffix_range(self):
        status, headers, body = self.request("/file.bin", {"Range": "bytes=-8"})
        self.assertEqual(status, 206)
        self.assertEqual(headers["Content-Range"], "bytes 16376-16383/16384")
        self.assertEqual(body, PAYLOAD[-8:])

    def test_unsatisfiable_range(self):
        status, headers, body = self.request("/file.bin", {"Range": "bytes=99999-"})
        self.assertEqual(status, 416)
        self.assertEqual(headers["Content-Range"], "bytes */16384")
        self.assertEqual(body, b"")

    def test_no_range_endpoint_ignores_range(self):
        status, headers, body = self.request("/no-range.bin", {"Range": "bytes=1-2"})
        self.assertEqual(status, 200)
        self.assertEqual(headers["Accept-Ranges"], "none")
        self.assertEqual(body, PAYLOAD)

    def test_head_and_health(self):
        status, headers, body = self.request("/file.bin", method="HEAD")
        self.assertEqual(status, 200)
        self.assertEqual(int(headers["Content-Length"]), 16384)
        self.assertEqual(body, b"")
        health_status, _, health_body = self.request("/health")
        self.assertEqual((health_status, health_body), (200, b"ok"))

    def test_unknown_path_not_a_proxy(self):
        status, _, body = self.request("/https://example.com/private")
        self.assertEqual((status, body), (404, b"not found"))


if __name__ == "__main__":
    unittest.main()
