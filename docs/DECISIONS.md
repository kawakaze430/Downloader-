# Architectural decision register

This records preferences, **not immutable architecture**. Each decision must be updated after the audit and approved by the project owner where indicated.

| ID | Decision | Status | Rationale / next action |
| --- | --- | --- | --- |
| ADR-001 | Desktop-first, local-first product with web + browser companions | Proposed | Strong baseline for download reliability and reduced server cost |
| ADR-002 | AB Download Manager as primary desktop candidate | Proposed, audit required | Apache-2.0 application with existing queues/scheduler and browser ecosystem |
| ADR-003 | AB Browser Integration as first extension candidate | Proposed, audit required | Existing integration with AB; avoid building handoff twice |
| ADR-004 | ReClip as website candidate | Proposed, audit required | MIT, small Flask/JS web base; web-to-desktop API is not yet built |
| ADR-005 | MediaGrabber/HLS Downloader as selective additions | Proposed | Review only components needed for permitted media formats |
| ADR-006 | FFmpeg for media conversion | Proposed | Established tool, but distribution/configuration licensing varies |
| ADR-007 | yt-dlp as optional restricted connector | Proposed | No guarantee of site availability or platform permission |
| ADR-008 | No blanket GPL/AGPL code import into proprietary app | Proposed | Distribution and network-source obligations require owner/legal decision |
| ADR-009 | Project license / contributor terms | **Owner decision required** | Public GitHub visibility is not a software license; do not invent one |
| ADR-010 | Brand name, logos, domains and monetization | **Owner decision required** | Distinct identity and trademark review needed |
| ADR-011 | Initial OS/browser: Windows and Chrome | Recommended, unapproved | Efficient first end-to-end test pair |
| ADR-012 | Greenfield Tauri/Next.js rewrite | **Deferred** | Reassess after building the existing Kotlin-based candidate |
| ADR-013 | Cloud storage, Redis/PostgreSQL and billing | **Deferred** | Introduce only with a proven hosted use case |
| ADR-014 | Public media-download sources and allowed URL policy | **Owner/legal decision required** | Platform policies and distribution constraints differ by source |

## Decision template

~~~
ID:
Date:
Owner:
Context:
Options:
Decision:
License/security implications:
Evidence/tests:
Revisit when:
~~~

Changes to these decisions should be made via an issue or PR with explicit reasoning and review. Avoid committing to a framework because it appears in an example diagram.
