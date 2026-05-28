# Tacheon Assessment — Prethepa Senthilkumar

## Overview

This repository contains my submission for the Data & AI Product 
Engineer assessment. It is organised into two tasks completed within 
the given timeframe.

## Repository Structure
tacheon-assessment/
├── task1/
│   └── product_brief.md    — Product scoping document
└── task2/
├── fetch.py             — Fetches weather data from Open-Meteo API
├── transform.py         — Cleans and transforms raw data
├── load.py              — Loads transformed data to BigQuery
├── pipeline.py          — Runs full ETL pipeline end to end
├── README.md            — Task 2 detailed documentation
└── queries/
└── summary.sql      — SQL summary query with sample output

## Task 1 — Product Scoping

Scoped an internal marketing performance tool for a marketing 
technology team. The brief covers the primary user, v1 scope, 
data sources, trust considerations, and what is deliberately 
left out.

Read the full brief here: task1/product_brief.md

## Task 2 — Pipeline Building

Built a complete end to end data pipeline:
- Fetches weather data from Open-Meteo API (no API key needed)
- Transforms raw JSON into clean tabular format with derived fields
- Loads data into Google BigQuery using batch loading
- Includes logging, error handling, and parameterised configuration

Read the full documentation here: task2/README.md

## Decisions Made

- Chose Open-Meteo because it is free, reliable, and returns 
  realistic nested JSON to work with
- Used BigQuery batch loading instead of streaming insert due to 
  Sandbox free tier limitations
- Kept each pipeline step in a separate file for clarity and 
  maintainability
- Added derived fields (avg temperature, temp range, weather 
  category) to demonstrate analytical thinking beyond raw data

## What I Would Revisit With More Time

- Add unit tests for transform logic
- Support multiple cities in the pipeline
- Add a configuration file instead of hardcoded parameters
- Record a Loom walkthrough video

---
*Prethepa Senthilkumar — May 2026*

