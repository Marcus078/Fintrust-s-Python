## Day 1 - Analytics Foundation

FinTrust implemented a three-zone data lake architecture using Amazon S3.

Transaction data enters the Bronze zone in its original format and is preserved as the system of record. Glue ETL jobs transform raw CSV data into partitioned Parquet datasets stored in the Silver zone. Business-ready aggregates are stored in the Gold zone for reporting and analytics.

Amazon Athena enables compliance teams to run ad hoc SQL queries directly against curated datasets while AWS Glue provides schema discovery and metadata management.

This architecture provides the foundation for fraud analytics, compliance reporting, machine learning, and executive dashboards throughout the FinTrust platform.

## Day 2 - Streaming Analytics

FinTrust introduced a real-time transaction processing platform using Amazon Kinesis Data Streams.

Transactions are written to the transaction-stream using account_id as the partition key, ensuring that all events for a specific account remain in sequence. Fraud-scoring Lambda functions consume the stream through Enhanced Fan-Out and call a SageMaker endpoint to evaluate transaction risk in near real time.

A Kinesis Firehose delivery stream creates an immutable backup of all transaction events in Amazon S3 for future analytics and compliance reporting.

OpenSearch was introduced as the central security analytics platform. CloudTrail logs, VPC Flow Logs, and application logs are indexed into OpenSearch, allowing security teams to perform full-text searches, monitor threats, and investigate suspicious activity through OpenSearch Dashboards.

## Day 3 - Data Engineering and Business Intelligence

FinTrust expanded its analytics platform by introducing data engineering workflows that prepare transaction data for large-scale analytics and machine learning.

Raw transaction exports are transformed from CSV into partitioned Parquet datasets using Python-based ETL processes. The transformed data is stored in the S3 Silver zone where it becomes available to Athena, Amazon EMR and QuickSight.

Amazon EMR performs monthly fraud feature engineering across historical transaction data, producing analytical feature sets that support fraud detection models and future SageMaker training workloads.

QuickSight provides business intelligence dashboards for executives, compliance officers and fraud analysts. Datasets are loaded into SPICE to improve dashboard performance and reduce the cost of repeated Athena queries.
`

## Day 4 - AI and Machine Learning Services

FinTrust introduced an intelligence layer built on Amazon SageMaker, Amazon Rekognition and Amazon Comprehend.

Amazon Rekognition automates customer identity verification during onboarding by comparing customer selfies with identity document photographs. Verification results are stored for compliance and audit purposes.

Amazon Comprehend improves customer support automation by detecting personally identifiable information (PII), performing sentiment analysis and routing support requests to specialised teams. Sensitive information is redacted before tickets enter the analytics platform.

Amazon SageMaker continues to provide real-time fraud scoring through a deployed endpoint that evaluates transaction risk before approval.

Together these services extend FinTrust from a traditional analytics platform into an intelligent banking platform capable of automated fraud detection, KYC verification and customer support automation.