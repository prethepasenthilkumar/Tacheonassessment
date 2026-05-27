-- Summary Query: Chennai Weather Analysis
-- This query retrieves weather data ordered by date
-- showing temperature trends and weather categories

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

-- Sample Output:
-- Row 1: Chennai | 2026-05-20 | 40.2 | 29.8 | 35.0 | 0.0 | Dry
-- Row 2: Chennai | 2026-05-21 | 39.5 | 31.4 | 35.45 | 0.0 | Dry
-- Row 3: Chennai | 2026-05-22 | 38.0 | 30.2 | 34.1 | 0.0 | Dry
-- Row 4: Chennai | 2026-05-23 | 35.8 | 31.3 | 33.55 | 0.0 | Dry
-- Row 5: Chennai | 2026-05-24 | 39.0 | 30.1 | 34.55 | 2.4 | Light Rain
-- Row 6: Chennai | 2026-05-25 | 39.0 | 29.2 | 34.1 | 0.7 | Light Rain
-- Row 7: Chennai | 2026-05-26 | 39.5 | 29.9 | 34.7 | 0.7 | Light Rain
-- Row 8: Chennai | 2026-05-27 | 39.6 | 29.4 | 34.5 | 0.0 | Dry
