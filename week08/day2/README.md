# Week 8 Day 2 - Kinesis and OpenSearch

## FinTrust Streaming Platform

FinTrust introduced real-time transaction processing using Amazon Kinesis Data Streams and OpenSearch.

### Kinesis Data Streams

The transaction-stream ingests transaction events from the banking platform.

Configuration:

- 8 shards
- Retention: 7 days
- Enhanced Fan-Out enabled
- Partition Key: account_id

The account_id partition key was chosen to ensure that all transactions for a specific customer account are processed in order.

### Kinesis Firehose

A Firehose delivery stream receives data from Kinesis and writes immutable backups to S3.

This allows transaction replay and long-term analytics.

### OpenSearch

OpenSearch receives:

- VPC Flow Logs
- CloudTrail Events
- Security Events
- Application Logs

Security analysts use OpenSearch Dashboards to investigate suspicious behaviour and create operational dashboards.

### Real-Time Fraud Pipeline

Transaction Stream → Fraud Scorer Lambda → SageMaker Endpoint → DynamoDB

This architecture provides near real-time fraud detection while maintaining ordered processing for each account.