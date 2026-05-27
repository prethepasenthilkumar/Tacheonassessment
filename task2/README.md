# Task 2: Weather Data Pipeline

## What This Pipeline Does

This pipeline automatically fetches weather data for Chennai from the 
Open-Meteo API, transforms it into a clean tabular format, and loads 
it into BigQuery. It runs end to end with a single command.

## Why Open-Meteo

- Free and public — no API key required
- Returns structured JSON data that is realistic to work with
- Reliable uptime and well documented
- Weather data is relevant to marketing — campaigns, footfall, and 
  seasonal demand are all affected by weather conditions

## How to Run

### 1. Install dependencies
### 2. Add your service account key
Place your Google Cloud service account JSON key file in this folder.
Update the KEY_FILE value in load.py with your filename.
### 3. Run the full pipeline

## What Each File Does

- fetch.py — calls Open-Meteo API for Chennai weather data
- transform.py — flattens nested JSON, handles nulls, adds derived fields
- load.py — connects to BigQuery and loads transformed data
- pipeline.py — orchestrates all three steps in sequence
- queries/summary.sql — SQL query to analyse the stored data

## Derived Fields Added

- avg_temp_c — average of max and min temperature
- temp_range_c — difference between max and min temperature
- weather_category — Dry, Light Rain, or Heavy Rain based on precipitation

## BigQuery Setup

- Project: carbide-calling-492505-p0
- Dataset: weather_data
- Table: daily_weather
- Used BigQuery Sandbox (free tier)
- Used batch load instead of streaming insert due to Sandbox limitations

## SQL Summary Query

```sql
SELECT
  city,
  date,
  temp_max_c,
  temp_min_c,
  avg_temp_c,
  precipitation_mm,
  weather_category
FROM
  `carbide-calling-492505-p0.weather_data.daily_weather`
ORDER BY
  date ASC;
```

### Sample Output

| city | date | temp_max_c | temp_min_c | avg_temp_c | precipitation_mm | weather_category |
|---|---|---|---|---|---|---|
| Chennai | 2026-05-20 | 40.2 | 29.8 | 35.0 | 0.0 | Dry |
| Chennai | 2026-05-21 | 39.5 | 31.4 | 35.45 | 0.0 | Dry |
| Chennai | 2026-05-22 | 38.0 | 30.2 | 34.1 | 0.0 | Dry |
| Chennai | 2026-05-24 | 39.0 | 30.1 | 34.55 | 2.4 | Light Rain |
| Chennai | 2026-05-25 | 39.0 | 29.2 | 34.1 | 0.7 | Light Rain |

## Production Thinking

### How would you schedule this pipeline?
I would use Google Cloud Scheduler to trigger the pipeline daily 
via a Cloud Function or Cloud Run job. Alternatively, Apache Airflow 
could be used for more complex scheduling needs.

### How would you know if it failed?
I would add email or Slack alerts using Cloud Monitoring. The 
pipeline already has logging built in — those logs would be 
captured in Cloud Logging and alerts triggered on ERROR level logs.

### What would you change for 10x data volume?
- Switch from single city to multiple cities in parallel using 
  Python threading or multiprocessing
- Use chunked batch loading instead of loading all records at once
- Add partitioning to the BigQuery table by date for faster queries
- Consider using Cloud Dataflow for large scale transformations

## What I Would Do Differently With More Time

- Add unit tests for the transform logic
- Add a config file instead of hardcoding parameters
- Support multiple cities
- Add data validation checks before loading to BigQuery

