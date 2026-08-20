# Week 2 Compute Services Summary

## EC2 vs Lambda vs ECS

During Week 2, we explored the different AWS compute services used in the FinTrust Bank architecture. Each service was selected based on the requirements of a specific workload.

### Amazon EC2

Amazon EC2 provides virtual servers in the cloud.

**Best used when:**
- Full control of the operating system is required
- Applications need long-running processes
- Custom software or configurations are needed
- Specific hardware requirements exist

**FinTrust Example:**
- Legacy banking applications
- Transaction processing systems requiring dedicated server resources

### AWS Lambda

AWS Lambda is a serverless compute service that runs code in response to events without managing servers.

**Best used when:**
- Workloads are event-driven
- Functions run for short periods
- Automatic scaling is required
- Reducing infrastructure management is a priority

**FinTrust Example:**
- Fraud detection functions
- Monthly compliance reports
- Processing files uploaded to S3

### Amazon ECS

Amazon ECS (Elastic Container Service) is AWS's container orchestration platform.

**Best used when:**
- Applications are containerised using Docker
- Microservices architectures are being deployed
- Workloads require scalability and portability
- Multiple services need to run together

**FinTrust Example:**
- Transaction API
- Account Service
- Fraud Batch Processor

---

## Key Differences

| Service | Infrastructure Management | Scaling | Runtime |
|----------|--------------------------|----------|----------|
| EC2 | Customer manages servers | Manual or Auto Scaling | Unlimited |
| Lambda | AWS manages servers | Automatic | Up to 15 minutes per invocation |
| ECS | AWS manages containers and orchestration | Automatic | Unlimited |

---

## Decision Rules

### Choose EC2 when:
- Full server control is required.
- Applications are not containerised.
- Custom operating system configurations are needed.

### Choose Lambda when:
- The workload is event-driven.
- Execution time is short.
- You want a fully serverless solution.

### Choose ECS when:
- Applications are packaged in containers.
- A microservices architecture is required.
- Services need to scale independently.

---

## Reflection

This week helped me understand that there is no single "best" compute service. The correct choice depends on the workload requirements. In the FinTrust architecture, ECS was selected for containerised microservices, Lambda for event-driven processing, and EC2 remains a suitable option for workloads that require full control over the operating environment.