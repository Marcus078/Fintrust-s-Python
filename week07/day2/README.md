# Week 7 Day 2 - APIs, GraphQL and Lambda

## FinTrust System Extension

Day 2 focused on exposing FinTrust services through secure API layers and serverless compute.

## API Gateway

FinTrust uses API Gateway as the entry point for customer and partner applications.

### REST APIs

The trading platform exposes a REST API protected by Cognito User Pools for retail customers and Lambda Authorizers for regulatory integrations.

### HTTP APIs

Internal service communication uses HTTP APIs with IAM authentication to reduce cost while maintaining security.

### WebSocket APIs

Institutional trading partners receive real-time trade notification updates through WebSocket APIs.

---

## AWS AppSync

The FinTrust mobile application uses GraphQL through AWS AppSync.

A single query retrieves:

- Account balances
- Recent transactions
- Foreign exchange rates

This reduces the number of API calls required by mobile clients and improves performance.

AppSync subscriptions provide real-time balance updates without polling.

---

## AWS Lambda

Several Lambda functions were created to process events from different AWS services.

### API Gateway Event Processing

Lambda functions receive and process API requests routed through API Gateway.

### SQS Event Processing

Lambda functions consume messages from SQS queues for asynchronous processing.

### S3 Event Processing

Lambda functions react automatically when files are uploaded to S3 buckets.

---

## SWF vs Step Functions

FinTrust continues to use SWF for legacy KYC processes that require human review by compliance officers.

New workflows use AWS Step Functions because of their visual orchestration, retry handling, and scalability.
