import logging
from google.cloud import bigquery
from google.oauth2 import service_account
import os

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)
logger = logging.getLogger(__name__)

# Configuration
PROJECT_ID = "carbide-calling-492505-p0"
DATASET_ID = "weather_data"
TABLE_ID = "daily_weather"
KEY_FILE = "carbide-calling-492505-p0-599aa03803fc.json"

def get_bigquery_client(key_file):
    credentials = service_account.Credentials.from_service_account_file(
        key_file,
        scopes=["https://www.googleapis.com/auth/cloud-platform"]
    )
    client = bigquery.Client(
        credentials=credentials,
        project=PROJECT_ID
    )
    logger.info("BigQuery client created successfully")
    return client

def create_table_if_not_exists(client):
    dataset_ref = client.dataset(DATASET_ID)
    table_ref = dataset_ref.table(TABLE_ID)

    schema = [
        bigquery.SchemaField("city", "STRING"),
        bigquery.SchemaField("date", "DATE"),
        bigquery.SchemaField("temp_max_c", "FLOAT"),
        bigquery.SchemaField("temp_min_c", "FLOAT"),
        bigquery.SchemaField("avg_temp_c", "FLOAT"),
        bigquery.SchemaField("temp_range_c", "FLOAT"),
        bigquery.SchemaField("precipitation_mm", "FLOAT"),
        bigquery.SchemaField("windspeed_kmh", "FLOAT"),
        bigquery.SchemaField("weather_category", "STRING"),
        bigquery.SchemaField("ingested_at", "TIMESTAMP"),
    ]

    try:
        client.get_table(table_ref)
        logger.info(f"Table {TABLE_ID} already exists")
    except Exception:
        table = bigquery.Table(table_ref, schema=schema)
        client.create_table(table)
        logger.info(f"Table {TABLE_ID} created successfully")

def load_to_bigquery(client, records):
    import json
    import tempfile
    table_ref = f"{PROJECT_ID}.{DATASET_ID}.{TABLE_ID}"
    
    # Write records to a temp JSON file
    with tempfile.NamedTemporaryFile(mode='w', suffix='.json', 
                                     delete=False) as f:
        for record in records:
            f.write(json.dumps(record) + '\n')
        temp_path = f.name

    # Load using batch load instead of streaming
    job_config = bigquery.LoadJobConfig(
        source_format=bigquery.SourceFormat.NEWLINE_DELIMITED_JSON,
        write_disposition=bigquery.WriteDisposition.WRITE_APPEND,
        autodetect=True
    )

    with open(temp_path, 'rb') as f:
        load_job = client.load_table_from_file(
            f, table_ref, job_config=job_config
        )

    load_job.result()
    logger.info(f"Successfully loaded {len(records)} rows to BigQuery")

if __name__ == "__main__":
    from fetch import fetch_weather_data, LATITUDE, LONGITUDE, DAYS_BACK
    from transform import transform_weather_data

    raw_data = fetch_weather_data(LATITUDE, LONGITUDE, DAYS_BACK)
    records = transform_weather_data(raw_data, "Chennai")

    client = get_bigquery_client(KEY_FILE)
    create_table_if_not_exists(client)
    load_to_bigquery(client, records)