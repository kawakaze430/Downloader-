# Start here: new developer onboarding

**Current status:** The repository contains a plan and contributor instructions, not a running downloader.

## Understand the product in 10 minutes

1. [README](../README.md) — overview and current implementation status.
2. [Product vision](PRODUCT_VISION.md) — users, competition and product boundaries.
3. [Feature matrix](FEATURE_MATRIX.md) — exact capabilities, priority and acceptance.
4. [Architecture](ARCHITECTURE.md) — intended components and interaction.
5. [Roadmap](ROADMAP.md) — what to build first.
6. [Reference projects](REFERENCE_REPOSITORIES.md) — what to evaluate and reuse.
7. [Legal/security](LEGAL_SECURITY.md) — non-negotiable safeguards.
8. [Codex workflow](CODEX_WORKFLOW.md) — budget-conscious AI implementation.

## First contribution: repository audit

**Expected output, before any large import:**

- Pin a commit/tag for each proposed source project.
- Record language, frameworks, build instructions, release activity and tests.
- Verify licenses including transitive libraries, bundled tools and NOTICE obligations.
- Build and test the proposed base in an isolated environment; capture real results.
- Map each feature to **implemented upstream / partially implemented / missing**, and separately to **implemented here / unimplemented**.
- Compare integration costs, security risks, package sizes and maintenance burden.
- Recommend one base app and extension with a small working integration target.

Use the issue template. Put audit results in a PR; avoid copying upstream trees before approval.

## Owner decisions needed before substantial code imports

1. Product/brand name and trademark checks.
2. Intended distribution: open-source, source-available, or proprietary.
3. Project license and contributor terms (no LICENSE has been chosen).
4. Initial supported OS/browser pair (recommend Windows + Chrome, then Linux/Firefox).
5. Whether the initial web app supports uploads, authorized direct URLs, or only marketing.
6. Whether any third-party source requires written authorization before downloads.

## Suggested first runnable demonstration

With permission to implement, show a Chrome extension sending an **authorized HTTPS file URL** to a desktop app. The app downloads with progress, pause/resume where the server supports range requests, checksum verification, and restart recovery. A short test fixture proves the flow. This validates the hardest shared integration without relying on YouTube compatibility.

## Common mistakes to avoid

- Calling a planned feature "implemented."
- Importing AGPL/GPL code into a closed-source product without resolving obligations.
- Copying user credentials into test fixtures or CI.
- Building the whole stack before validating one application-extension bridge.
- Depending on scraping or external network behavior for the entire test suite.
