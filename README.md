# Data Workbench Catalog

**Five real Python products. One inspectable starting point.** Maintained by [Muzammil Qazi](https://m-qazi99.github.io/profile/) in Pune, India.

This repository occupies the existing `Reverse` URL, which was previously empty. Its purpose is now explicit: a machine-readable catalog, offline link/identity validator and contributor starting point for the five independent applications. Existing product URLs stay unchanged. It does not duplicate their engines or claim to be another application.

[Open the portfolio project finder](https://m-qazi99.github.io/#live-projects) · [Compare the products](https://m-qazi99.github.io/project-guide/) · [Engineering notes](https://m-qazi99.github.io/notes/)

## Product directory
| Project | Purpose | Version | Explore |
|---|---|---|---|
| Pipeline Pulse | Failed-activity priorities, recovery coverage and capacity handoffs | 2.1.0 | [Live](https://m-qazi99.github.io/pipeline-pulse/) · [Source](https://github.com/m-qazi99/pipeline-pulse) · [Guide](https://github.com/m-qazi99/pipeline-pulse/blob/main/docs/USER_GUIDE.md) |
| DataLens | Contract coverage gaps and failing-rule review priorities | 2.1.0 | [Live](https://m-qazi99.github.io/datalens/) · [Source](https://github.com/m-qazi99/datalens) · [Guide](https://github.com/m-qazi99/datalens/blob/main/docs/USER_GUIDE.md) |
| Recon Lab | Keyset exceptions and field-level reconciliation priorities | 2.1.0 | [Live](https://m-qazi99.github.io/recon-lab/) · [Source](https://github.com/m-qazi99/recon-lab) · [Guide](https://github.com/m-qazi99/recon-lab/blob/main/docs/USER_GUIDE.md) |
| Runbook Radar | Evaluation coverage, top-K misses and no-match review | 2.1.0 | [Live](https://m-qazi99.github.io/runbook-radar/) · [Source](https://github.com/m-qazi99/runbook-radar) · [Guide](https://github.com/m-qazi99/runbook-radar/blob/main/docs/USER_GUIDE.md) |
| Privacy Forge | Retained signals, singleton groups and policy review | 2.1.0 | [Live](https://m-qazi99.github.io/privacy-forge/) · [Source](https://github.com/m-qazi99/privacy-forge) · [Guide](https://github.com/m-qazi99/privacy-forge/blob/main/docs/USER_GUIDE.md) |


## Use the catalog

```bash
python catalog.py --check
python catalog.py --format markdown
python catalog.py --format json
python -m unittest discover -s tests -v
```

Python 3.11+, no external packages or network calls. `projects.json` contains canonical slugs, live/source/guide links, versions and descriptive technical terms. Validation checks identity and URL consistency; it does not contact the websites or certify availability.

## Contribute meaningful work

Follow a product's guide, run its synthetic example, and inspect the source and tests. Report a reproducible problem or propose a bounded improvement in that repository. Use [CONTRIBUTING.md](CONTRIBUTING.md) for this catalog. Do not create empty PRs or split cosmetic edits to manufacture contribution activity.

## Scope and ownership

The apps are independent portfolio projects developed with Codex assistance. They do not establish employer deployments, client outcomes or production adoption. The catalog is MIT licensed; each linked project retains its own license.
