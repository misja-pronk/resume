---
title: Databricks Asset Bundles in Production — Lessons from the Field
date: 2026-07-01
summary: What I learned standardizing CI/CD on Databricks Asset Bundles across data engineering and data science teams — the good, the sharp edges, and the patterns that stuck.
tags:
  - Databricks
  - Asset Bundles
  - CI/CD
draft: false
---

After rolling out Databricks Asset Bundles as the standard deployment mechanism at two construction-sector clients, a few patterns have proven themselves worth writing down.

## Why bundles at all

Before bundles, every team invented its own deployment story: notebooks pushed by hand, jobs edited in the UI, one brave soul with a Terraform provider. Asset Bundles give you a single, declarative `databricks.yml` that describes jobs, pipelines and workspace resources — versioned in Git next to the code they deploy.

```yaml
bundle:
  name: ingest-sap

targets:
  dev:
    mode: development
    workspace:
      host: https://adb-dev.azuredatabricks.net
  prd:
    mode: production
    workspace:
      host: https://adb-prd.azuredatabricks.net
```

## The patterns that stuck

1. **One bundle per data product.** Bundles that try to deploy half a platform become the platform's bottleneck.
2. **Shared Python packages, not shared notebooks.** The bundle deploys a wheel; the wheel carries the logic; the notebook is three lines.
3. **`mode: development` for every engineer.** Prefixed resources mean five people can deploy the same bundle to the same workspace without stepping on each other.

## The sharp edges

Bundles will not save you from unclear ownership. Decide who owns the job, the schema and the alerting *before* you standardize the pipeline that deploys them.

More on the Python package setup in a future memo.
