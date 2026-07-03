---
title: Why I Moved Data Platform Teams from Bicep to Terragrunt
date: 2026-06-15
summary: Moving two cloud teams from Bicep to a Terragrunt-based way of working — the argument, the migration path, and what I would do differently.
tags:
  - Terragrunt
  - Terraform
  - Platform Engineering
draft: true
---

*Sample post — replace with a real one and set `draft: false`.*

Bicep is a fine language for deploying Azure resources. The problem is never the language — it is what happens when a data platform grows to forty modules across three environments and two teams, and every environment is a copy-pasted parameter file.

Terragrunt earns its place by making the *structure* of your infrastructure explicit: one folder per environment, DRY inputs, explicit dependencies between stacks. The learning curve is real, but it is shorter than the debugging curve of drift between hand-maintained parameter files.

The migration approach that worked: run both side by side, migrate stack by stack starting with stateless resources, and pair with the cloud team on every migrated stack — the goal is not migrated code, it is a team that owns the new way of working.
