# Week 7 Reflection

This week introduced application integration and event-driven architecture on AWS. I learned how to decouple services using SQS queues, SNS fan-out patterns, EventBridge routing, and Step Functions workflows.

The FinTrust architecture evolved from isolated services into a loosely coupled platform where services communicate through events rather than direct dependencies. This improves scalability, fault tolerance, and operational flexibility.

I also built REST and GraphQL APIs using API Gateway, AppSync, Flask, and FastAPI. Working with Lambda functions provided practical experience processing API Gateway, SQS, and S3 events while applying AWS serverless design patterns.

CloudFormation introduced Infrastructure as Code concepts that allow environments to be deployed consistently and managed through version control. Disaster recovery planning highlighted the trade-offs between cost, RTO, and RPO when choosing Backup and Restore, Pilot Light, Warm Standby, or Multi-Site Active-Active architectures.

The most valuable lesson from this week was understanding how modern cloud systems achieve resilience through loose coupling, automation, and event-driven design principles.