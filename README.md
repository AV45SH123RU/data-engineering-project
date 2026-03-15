# Data Engineering Project

End-to-end data pipeline using Google Cloud Platform, dbt, and Airflow.

## Architecture
- Bronze layer: Raw data in GCS
- Silver layer: Cleaned data in BigQuery (dbt)
- Gold layer: Aggregated business metrics (dbt)
- Orchestration: Airflow
- CI/CD: GitHub Actions