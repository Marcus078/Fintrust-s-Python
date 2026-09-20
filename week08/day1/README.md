# Week 8 Day 1 - Analytics Foundations

## FinTrust System Extension

Week 8 introduced the FinTrust analytics platform.

The solution follows a five-stage analytics pipeline:

1. Ingest
2. Store
3. Process
4. Analyse
5. Visualise

### Data Lake Architecture

The FinTrust data lake uses Amazon S3 as the central storage layer.

#### Bronze Zone

Raw transaction exports, Kinesis deliveries and DMS data.

Bucket:

fintrust-raw

#### Silver Zone

Processed Parquet datasets produced by AWS Glue ETL jobs.

Bucket:

fintrust-processed

#### Gold Zone

Business-ready datasets and compliance reporting tables.

Bucket:

fintrust-curated

---

## Amazon Athena

Athena was selected because it provides serverless SQL querying directly against S3 data.

Benefits:

- No infrastructure to manage
- Pay-per-query pricing
- Integration with Glue Catalog
- Fast compliance reporting

---

## AWS Glue

Glue was introduced for:

- Schema discovery
- Metadata management
- CSV to Parquet conversion
- Data lake ETL processing

The Glue Data Catalog acts as the central schema registry for Athena, EMR, and other analytics services.

---

## Architecture Principles

- Data lake design
- Immutability of raw data
- Cost optimisation through Parquet
- Partition-based query optimisation
- Serverless analytics
