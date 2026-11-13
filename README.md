# Downloader — product blueprint

> **Status: planning and repository bootstrap. No downloader application has been implemented or tested in this repository yet.**

This is the public collaboration hub for an independently branded, cross-platform **download manager and authorized media-processing platform**. The ambition is to build a credible competitor to established desktop download managers, video downloaders, and browser media tools—not merely a page that accepts a YouTube URL.

The product name, software license, commercial model, and final architecture have **not** been approved yet. "Downloader" is a working name. The project owner controls this repository; contributors retain any rights not transferred or licensed under an agreed contribution policy.

## North star

Create one cohesive experience across:

1. **Desktop** — the flagship application for reliable local downloads, pause/resume, queues, scheduling, file organization, and media conversion.
2. **Browser extension** — discover permitted downloads and hand jobs securely to the desktop application.
3. **Website** — introduce the product and, in a later milestone, offer a secure browser-based interface for user-owned or explicitly downloadable media.
4. **Shared engine and optional services** — reusable jobs, format discovery, media processing, authentication where needed, and diagnostics.

We benchmark **4K Video Downloader Plus** for video workflows, **Internet Download Manager** for download reliability, **Video DownloadHelper** for browser integration, **JDownloader** for automation, and **Cobalt** for web usability. None has been independently established as the single worldwide "#1" across all categories. See [market analysis](docs/COMPETITOR_BENCHMARK.md).

## Project status

| Area | Current status | First next step |
| --- | --- | --- |
| Vision, scope, roadmap | Documented; review requested | Agree on priorities |
| Repository/license audit | Research candidates listed, not audited | Verify code, licenses, dependencies, activity and security |
| Desktop application | Not implemented | Evaluate AB Download Manager foundation |
| Browser extension | Not implemented | Evaluate AB Browser Integration foundation |
| Website/download UI | Not implemented | Evaluate ReClip and design API contracts |
| Media processing | Not implemented | Verify FFmpeg integration and permitted-source policy |
| Automated tests, CI and releases | Not implemented | Create audit baseline and first testable vertical slice |

Do not interpret the existence of a feature in an upstream project as an implemented feature **here**.

## Start here

- [New contributor quick start](docs/START_HERE.md)
- [Complete ordered implementation checklist](docs/IMPLEMENTATION_CHECKLIST.md) — milestones, dependencies, release gates and blockers
- [Project vision and users](docs/PRODUCT_VISION.md)
- [Complete feature inventory and acceptance criteria](docs/FEATURE_MATRIX.md)
- [Reference repositories, licenses and reuse strategy](docs/REFERENCE_REPOSITORIES.md)
- [Proposed system architecture](docs/ARCHITECTURE.md)
- [Milestones and definition of done](docs/ROADMAP.md)
- [Competitor benchmarks](docs/COMPETITOR_BENCHMARK.md)
- [Legal, copyright, privacy and security guardrails](docs/LEGAL_SECURITY.md)
- [Development and testing setup](docs/DEVELOPMENT_SETUP.md)
- [Codex/cloud workflow and credit-saving instructions](docs/CODEX_WORKFLOW.md)
- [Open architectural decisions](docs/DECISIONS.md)
- [How to contribute](CONTRIBUTING.md)
- [AI contributor instructions](AGENTS.md)

## Recommended starting points (not imported)

| Purpose | Candidate | Why |
| --- | --- | --- |
| Main desktop starting point | [AB Download Manager](https://github.com/amir1376/ab-download-manager) | Mature open-source download management; Apache-2.0 |
| Browser companion | [AB browser integration](https://github.com/amir1376/ab-download-manager-browser-integration) | Already works with AB application; Apache-2.0 |
| Web-download experience | [ReClip](https://github.com/averygan/reclip) | Small, approachable Flask/JS media UI; MIT |
| Media discovery | [MediaGrabber](https://github.com/miroshArtem/MediaGrabber) and [HLS Downloader](https://github.com/puemos/hls-downloader) | Extension architecture and non-DRM streams; both MIT |
| Media operations | [FFmpeg](https://github.com/FFmpeg/FFmpeg) | Conversion/remuxing with build-dependent licenses |
| Optional extraction | [yt-dlp](https://github.com/yt-dlp/yt-dlp) | For sources and uses that permit downloading; check bundled licenses |

**Important:** These are research inputs, not automatically approved dependencies. The software must not facilitate unauthorized access, DRM circumvention, or prohibited copying.

## Working rules

- **Reuse verified, appropriately licensed implementations.** Do not spend time rebuilding existing queues, scheduling, browser handoff, FFmpeg, or installers without a demonstrated need.
- **Keep one product repository** with modular packages rather than pasting unrelated projects together.
- **Implement in verified increments.** Every feature needs tests, meaningful errors and a clear status.
- **Privacy and safety first.** Protect user files, download permissions, cookies, local helper APIs and cloud services.
- **Do not promise universal website support.** Compatibility changes, permissions and platform policies limit availability.

## Contributing right now

The first milestone is an **evidence-backed repository and license audit**, not an entire product rewrite. Choose an issue, read [CONTRIBUTING.md](CONTRIBUTING.md), and propose improvements via a focused PR. The owner must select a software license and contribution policy before accepting substantial new application code.

## Links and scope

- Project: https://github.com/rejoansardar620-lang/Downloader-
- Research snapshot: **13 November 2026**; upstream capabilities and licenses must be rechecked before adoption.
- This repository does not contain source code from any reference project at this stage.
