import logging
from datetime import datetime

logger = logging.getLogger(__name__)

def transform_weather_data(raw_data, city):
    if not raw_data or "daily" not in raw_data:
        logger.error("Invalid or empty data received")
        return []

    daily = raw_data["daily"]
    records = []

    for i, date in enumerate(daily["time"]):
        temp_max = daily["temperature_2m_max"][i]
        temp_min = daily["temperature_2m_min"][i]
        precipitation = daily["precipitation_sum"][i]
        windspeed = daily["windspeed_10m_max"][i]

        # Handle nulls
        temp_max = temp_max if temp_max is not None else 0.0
        temp_min = temp_min if temp_min is not None else 0.0
        precipitation = precipitation if precipitation is not None else 0.0
        windspeed = windspeed if windspeed is not None else 0.0

        # Derived fields
        temp_range = round(temp_max - temp_min, 2)
        avg_temp = round((temp_max + temp_min) / 2, 2)

        # Weather category
        if precipitation > 10:
            weather_category = "Heavy Rain"
        elif precipitation > 0:
            weather_category = "Light Rain"
        else:
            weather_category = "Dry"

        record = {
            "city": city,
            "date": date,
            "temp_max_c": temp_max,
            "temp_min_c": temp_min,
            "avg_temp_c": avg_temp,
            "temp_range_c": temp_range,
            "precipitation_mm": precipitation,
            "windspeed_kmh": windspeed,
            "weather_category": weather_category,
            "ingested_at": datetime.utcnow().strftime("%Y-%m-%dT%H:%M:%S")
        }
        records.append(record)

    logger.info(f"Transformed {len(records)} records successfully")
    return records

if __name__ == "__main__":
    import logging
    logging.basicConfig(
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s"
    )
    from fetch import fetch_weather_data, LATITUDE, LONGITUDE, DAYS_BACK
    raw = fetch_weather_data(LATITUDE, LONGITUDE, DAYS_BACK)
    records = transform_weather_data(raw, "Chennai")
    for r in records:
        print(r)