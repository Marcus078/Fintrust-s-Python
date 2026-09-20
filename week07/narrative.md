# FinTrust Narrative - Week 7

## Week 7 System Evolution

Week 7 focused on transforming the FinTrust platform into an event-driven and serverless architecture.

### Day 1 - Messaging and Workflows

The FinTrust payment platform was extended with Amazon SQS, SNS, EventBridge, and Step Functions.

A FIFO SQS queue named `payment-events-queue` was introduced to process transaction events in the correct order. Confirmed transactions are published to the `transaction-confirmed` SNS topic, allowing multiple downstream services such as notifications, fraud monitoring, and ledger updates to process transactions independently.

EventBridge was added to route operational events such as RDS failovers to monitoring and operations services. Step Functions was introduced to orchestrate international wire transfers using the Saga rollback pattern.

### Day 2 - APIs and Serverless Processing

API Gateway became the primary entry point for FinTrust services.

Customer-facing APIs use Cognito authentication, while partner and regulatory integrations use Lambda Authorizers. The mobile application was enhanced using AppSync and GraphQL, allowing account balances, transaction history, and FX rates to be retrieved through a single query.

Lambda functions were added to process events from API Gateway, SQS, and S3.

### Day 4 - Infrastructure and Resilience

Infrastructure management was standardized using AWS CloudFormation. Change Sets, Drift Detection, and Deletion Policies were introduced to improve governance and operational safety.

The fraud-scoring service was extracted from the monolith and implemented as an event-driven Lambda function. Transactions are submitted to SQS, processed asynchronously, and high-risk transactions generate SNS alerts for compliance teams.

Disaster recovery planning was introduced using Active-Active, Warm Standby, and Backup-and-Restore strategies according to business requirements.

## Week 7 Outcome

By the end of Week 7, FinTrust had evolved from a collection of interconnected services into an event-driven architecture that supports:

- Reliable message processing with Amazon SQS
- Fan-out communication with Amazon SNS
- Event routing with Amazon EventBridge
- Workflow orchestration with AWS Step Functions
- Secure APIs through Amazon API Gateway
- GraphQL integration with AWS AppSync
- Serverless processing with AWS Lambda
- Infrastructure as Code through AWS CloudFormation
- Improved resilience through Disaster Recovery strategies

### Key Benefits Achieved

- Improved scalability through loosely coupled services
- Greater fault isolation and resilience
- Automated event processing and workflow orchestration
- Secure and scalable API exposure
- Consistent infrastructure deployment through IaC
- Better operational governance and monitoring
- Reduced dependency between application components

The Week 7 architecture establishes the foundation for a modern cloud-native FinTrust platform that is scalable, maintainable, secure, and resilient.