# Deterministic direct-download fixture (M0/M1)

The server is **our original implementation**, independent of candidate upstream applications. It provides a small HTTP test target for the Downloader desktop engine and browser handoff. It never fetches outside URLs, accesses local files, or processes real user videos.

## Start

From repository root, with Python 3.10+:

~~~sh
python3 -m tools.fixtures.http_fixture --port 8765
~~~

The server binds **only to 127.0.0.1**. A port of \`0\` assigns an available loopback port. Run tests:

~~~sh
python3 -m unittest discover -s tests -v
~~~

| URL | Behavior | Expected |
| --- | --- | --- |
| \`/file.bin\` | Fixed 16 KiB binary payload | HTTP 200, \`Accept-Ranges: bytes\`, deterministic SHA-256 |
| \`/file.bin\` with \`Range: bytes=0-8191\` | First half | HTTP 206 + correct \`Content-Range\` |
| \`/file.bin\` with \`Range: bytes=8192-\` | Second half | HTTP 206; concatenate pieces to obtain exact payload hash |
| \`/file.bin\` with \`Range: bytes=99999-\` | Invalid offset | HTTP 416 + \`Content-Range: bytes */16384\` |
| \`/no-range.bin\` | Deliberately ignores Range | HTTP 200, full body; a downloader must restart safely |
| \`/health\` | Readiness | HTTP 200 \`ok\` |
| Any unknown URL | No external proxy | HTTP 404 |

When M1 imports the approved engine, use these endpoints for direct, interrupted/resumed, invalid-range and integrity tests. The server intentionally does **not** emulate authentication, redirects, bandwidth throttling, HLS/DASH, multirange replies or network interruption yet; add separate deterministic fixtures when needed.
