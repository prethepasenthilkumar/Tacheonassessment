import requests
import logging
from datetime import datetime, timedelta

# Setup logging
logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Parameters
LATITUDE = 13.0827
LONGITUDE = 80.2707
DAYS_BACK = 7

def fetch_weather_data(latitude, longitude, days_back):
    end_date = datetime.today().strftime("%Y-%m-%d")
    start_date = (datetime.today() - timedelta(days=days_back)).strftime("%Y-%m-%d")

    url = "https://api.open-meteo.com/v1/forecast"
    params = {
        "latitude": latitude,
        "longitude": longitude,
        "daily": [
            "temperature_2m_max",
            "temperature_2m_min",
            "precipitation_sum",
            "windspeed_10m_max"
        ],
        "start_date": start_date,
        "end_date": end_date,
        "timezone": "Asia/Kolkata"
    }

    logger.info(f"Fetching weather data for coordinates ({latitude}, {longitude})")
    logger.info(f"Date range: {start_date} to {end_date}")

    try:
        response = requests.get(url, params=params, timeout=10)
        response.raise_for_status()
        data = response.json()
        logger.info("Data fetched successfully")
        return data

    except requests.exceptions.ConnectionError:
        logger.error("Connection failed. Check your internet connection.")
        return None
    except requests.exceptions.Timeout:
        logger.error("Request timed out. API may be slow.")
        return None
    except requests.exceptions.HTTPError as e:
        logger.error(f"HTTP error occurred: {e}")
        return None
    except Exception as e:
        logger.error(f"Unexpected error: {e}")
        return None

if __name__ == "__main__":
    data = fetch_weather_data(LATITUDE, LONGITUDE, DAYS_BACK)
    if data:
        print(data)