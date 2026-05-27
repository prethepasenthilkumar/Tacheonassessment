import logging
from fetch import fetch_weather_data, LATITUDE, LONGITUDE, DAYS_BACK
from transform import transform_weather_data
from load import get_bigquery_client, create_table_if_not_exists, load_to_bigquery, KEY_FILE

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

def run_pipeline():
    logger.info("Pipeline started")

    # Step 1 - Fetch
    raw_data = fetch_weather_data(LATITUDE, LONGITUDE, DAYS_BACK)
    if not raw_data:
        logger.error("Pipeline failed at fetch step")
        return

    # Step 2 - Transform
    records = transform_weather_data(raw_data, "Chennai")
    if not records:
        logger.error("Pipeline failed at transform step")
        return

    # Step 3 - Load
    client = get_bigquery_client(KEY_FILE)
    create_table_if_not_exists(client)
    load_to_bigquery(client, records)

    logger.info("Pipeline completed successfully")

if __name__ == "__main__":
    run_pipeline()