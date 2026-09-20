# Week 7 Day 1 - Messaging, Events and Workflows

## Overview

This session focused on building event-driven architectures using Amazon SQS, SNS, EventBridge, and AWS Step Functions.

The goal was to extend the FinTrust banking platform by introducing loosely coupled services capable of processing transactions reliably, even when individual systems experience delays or failures.

---

## FinTrust System Extension

### SQS Message Processing

A FIFO queue named `payment-events-queue` was introduced to guarantee transaction ordering.

Transaction events are written to the queue by the payment service and processed by downstream Lambda functions.

Configuration:

- Queue Type: FIFO
- Visibility Timeout: 120 seconds
- Long Polling: 20 seconds
- Dead Letter Queue configured
- maxReceiveCount = 3

This design ensures that payment events are processed in the correct order and remain available during service interruptions.

---

### SNS Fan-Out Pattern

Once a transaction is confirmed, an event is published to the `transaction-confirmed` SNS topic.

Three independent subscribers consume the event:

- Email Notification Queue
- Fraud Audit Queue
- Ledger Update Queue

This removes direct dependencies between systems and allows new consumers to be added without changing the payment service.

---

### EventBridge Event Routing

EventBridge was introduced to automate infrastructure event handling.

Example:

- RDS failover event occurs
- EventBridge detects the event
- A rule routes the event to the Operations Lambda
- Operations team receives notification

This provides event-driven monitoring without custom polling solutions.

---

### Step Functions Workflow

The international wire transfer process was designed using AWS Step Functions Standard.

Workflow:

1. Compliance Hold
2. Currency Conversion
3. SWIFT Dispatch
4. Recipient Credit

The Saga pattern is used to ensure failed transactions are rolled back to a consistent state.

---

## Architecture Principles Applied

- Loose coupling
- Event-driven communication
- Independent service scaling
- Failure isolation
- Reliable message processing
- Automated workflow orchestration

---

## Key Services Used

- Amazon SQS
- Amazon SNS
- Amazon EventBridge
- AWS Step Functions
- AWS Lambda