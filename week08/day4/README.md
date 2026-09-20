README.md# Week 8 Day 4 - AI Services Integration

## FinTrust Intelligence Layer

Day 4 introduced AI-powered banking services using Amazon SageMaker, Amazon Rekognition and Amazon Comprehend.

## Rekognition KYC Verification

FinTrust uses Rekognition CompareFaces during customer onboarding.

Process:

1. Customer uploads a selfie
2. Customer uploads an ID document
3. Rekognition compares both images
4. Similarity score is returned
5. Similarity >= 95% passes KYC verification

Benefits:

- Faster onboarding
- Reduced fraud risk
- Automated identity verification

## Comprehend PII Detection

Support tickets often contain sensitive customer information.

Comprehend detects and redacts:

- Names
- Phone numbers
- ID numbers
- Account numbers
- Credit card details

This helps FinTrust comply with POPIA requirements.

## Support Ticket Routing

Comprehend performs sentiment analysis on support tickets.

Negative sentiment tickets are routed to a high-priority support queue while normal tickets are processed through standard support channels.

## SageMaker Fraud Scoring

FinTrust continues to use a SageMaker endpoint for real-time fraud scoring.

Architecture:

```text
API Gateway
    |
    v
Lambda
    |
    v
SageMaker Endpoint
    |
    v
DynamoDB
```

Transactions are scored in near real time before approval decisions are made.