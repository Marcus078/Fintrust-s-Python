# Fraud Scoring Lambda

## Purpose

This Lambda function performs transaction risk scoring for FinTrust.

## Why Lambda?

Lambda was selected because:

- Event-driven execution
- Automatic scaling
- No server management
- Cost effective for variable workloads

## Why SQS?

SQS decouples transaction submission from fraud processing.

Benefits:

- Handles traffic spikes
- Prevents message loss
- Supports retries
- Improves system resilience

## Why SNS?

SNS distributes high-risk alerts to multiple subscribers.

Example consumers:

- Compliance Team
- Audit Services
- Email Notifications

The fraud scorer publishes a single alert and SNS handles fan-out to multiple consumers.