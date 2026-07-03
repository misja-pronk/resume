---
title: Building a GDPR-Compliant Machine Learning API
description: A public API around a machine learning model that filters non-traffic-incident data for VeiligheidNL, keeping the platform GDPR-compliant.
client: VeiligheidNL
role: Data Engineer
employer: GoDataDriven
duration: 1
order: -2
tags:
  - Azure Functions
  - Azure DevOps
  - Machine Learning
  - Pydantic
---

VeiligheidNL processes data related to traffic incidents for the Dutch government, supplied by hospitals and other medical institutions. Due to GDPR regulations, any data not related to traffic incidents must be filtered out. A machine learning model was built to achieve this, and the model was incorporated into a public API where hospitals can upload their information.

As a data engineer I was responsible for designing the API, building it and improving the CI/CD pipelines.
