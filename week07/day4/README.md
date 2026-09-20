# Week 7 Day 4 - Infrastructure as Code, Microservices and Disaster Recovery

## FinTrust System Extension

This session focused on Infrastructure as Code, event-driven microservices, and disaster recovery planning.

## CloudFormation

FinTrust infrastructure is managed using AWS CloudFormation.

Key practices adopted:

- Infrastructure as Code (IaC)
- Version-controlled infrastructure
- Change Sets before production updates
- Drift Detection for governance
- DeletionPolicy protection for databases

Aurora PostgreSQL resources use:

DeletionPolicy: Snapshot

to protect critical data.

---

## Microservices Migration

FinTrust is migrating from a monolithic architecture using the Strangler Fig pattern.

Extracted services include:

- Fraud Scoring
- Transaction Processing
- Notifications

API Gateway routes requests to either the monolith or the extracted microservices.

This approach reduces migration risk and avoids a large-scale system rewrite.

---

## Disaster Recovery

Different recovery strategies are selected based on business requirements.

### Retail Payments

- Multi-Site Active-Active
- Near-zero RTO
- Near-zero RPO

### Regulatory Reporting

- Warm Standby
- Aurora Global Database
- Reduced capacity compute resources

### Internal Platforms

- Backup and Restore
- Lower cost
- Higher recovery time acceptable

---

## Fraud Scoring Pipeline

An event-driven fraud detection pipeline was implemented.

Transaction Flow:

Flask API → SQS FIFO → Fraud Scorer Lambda → SNS Topic → Compliance Team

The architecture enables asynchronous processing, scalability, and independent failure handling.