# Security Services Configuration Summary

## Overview

During Week 6, FinTrust implemented several AWS security services to strengthen governance, compliance, secrets management, certificate management, network protection, and secure administration. Each service was selected based on a specific security requirement and aligned with AWS security best practices.

---

## AWS Security Services Deployed

| Service | Configuration | Purpose |
|-----------|--------------|-----------|
| AWS Config | 12 managed compliance rules | Compliance monitoring and configuration drift detection |
| AWS CloudTrail | Management and Data Events enabled | Audit logging and API activity tracking |
| AWS Secrets Manager | RDS credentials rotated every 30 days | Secure secret storage and automatic rotation |
| SSM Parameter Store | Application settings and feature flags | Centralized configuration management |
| AWS Certificate Manager (ACM) | CloudFront certificate in us-east-1 | HTTPS encryption and certificate management |
| AWS WAF | SQL injection, XSS, and rate-limiting rules | Application layer attack protection |
| AWS Shield Standard | Enabled automatically | DDoS protection |
| AWS Systems Manager Session Manager | Replaces bastion hosts and SSH access | Secure EC2 administration |
| AWS Control Tower | Landing Zone and Guardrails | Multi-account governance |
| AWS Trusted Advisor | Business Support Plan | Best-practice recommendations |

---

# AWS Config

## Rules Implemented

- S3 buckets must be encrypted
- S3 public access must be blocked
- EBS volumes must be encrypted
- CloudTrail must be enabled
- Security groups must not allow unrestricted SSH access
- Root account MFA must be enabled
- Logging must be enabled on critical resources

## Why AWS Config?

AWS Config continuously monitors resource configurations and compliance status.

It answers:

```text
"Is this resource configured correctly?"
```

### Benefits

- Detects configuration drift
- Tracks compliance over time
- Supports automated remediation
- Helps meet regulatory requirements

---

# AWS CloudTrail

## Configuration

```text
Management Events: Enabled
Data Events: Enabled
Retention: 90 Days
```

## Why CloudTrail?

CloudTrail provides a complete audit history of account activity.

It answers:

```text
"Who performed this action and when?"
```

### Benefits

- Tracks API calls
- Records user activity
- Supports investigations and auditing
- Integrates with CloudWatch and S3

---

# AWS Secrets Manager

## Rotation Schedule

### RDS Database Credentials

```text
Rotate Every 30 Days
```

### Payment API Keys

```text
Rotate Every 90 Days
```

## Why Secrets Manager?

Secrets Manager securely stores:

- Database passwords
- API keys
- Tokens
- Credentials

### Benefits

- Automatic secret rotation
- KMS encryption
- Eliminates hardcoded credentials
- Fine-grained access control

### Exam Signal

```text
Automatic Credential Rotation
=
Secrets Manager
```

---

# AWS Systems Manager Parameter Store

## Stored Information

- Feature flags
- Application settings
- Environment variables
- Logging levels

Example parameters:

```text
/app/prod/log-level
/app/prod/api-url
/app/prod/feature-flags
```

## Why Parameter Store?

Parameter Store provides centralized application configuration management.

### Benefits

- Low cost
- Hierarchical storage
- KMS encryption support
- Easy application integration

### Exam Signal

```text
Application Configuration
=
Parameter Store
```

---

# AWS Certificate Manager (ACM)

## Certificate Deployment

### CloudFront Certificate

```text
Region: us-east-1
```

### Application Load Balancer Certificate

```text
Region: af-south-1
```

## Why ACM?

ACM provides free SSL/TLS certificate management.

### Benefits

- Automated renewals
- Native AWS integration
- Simplified HTTPS deployment

### Critical CloudFront Rule

```text
CloudFront certificates
must be created
in us-east-1
```

---

# AWS WAF

## Web ACL Deployment

Attached to:

```text
CloudFront Distribution
Application Load Balancer
```

## Enabled Rule Groups

### AWS Managed Rules

- SQL Injection Protection
- Cross-Site Scripting (XSS) Protection
- Common Vulnerability Protection

### Rate-Based Rule

```text
Block IPs exceeding
1000 requests per 5 minutes
```

## Why WAF?

AWS WAF protects applications against Layer 7 attacks.

### Protects Against

- SQL Injection
- XSS attacks
- Brute-force login attempts
- Malicious HTTP requests

### Exam Signal

```text
SQL Injection
XSS
Layer 7 Protection

=
AWS WAF
```

---

# AWS Shield Standard

## Status

```text
Automatically Enabled
```

## Protection Provided

- SYN Floods
- UDP Floods
- Reflection Attacks

## Why Shield Standard?

Provides always-on network and transport layer DDoS protection.

### Benefits

- No additional cost
- Automatic protection
- Integrated with AWS edge services

---

# AWS Systems Manager Session Manager

## Replaces

```text
SSH
RDP
Bastion Hosts
```

## Requirements

- SSM Agent installed
- IAM role attached
- AmazonSSMManagedInstanceCore policy
- HTTPS outbound connectivity

## Session Logging

Enabled to:

```text
CloudWatch Logs
Amazon S3
```

## Why Session Manager?

Provides secure administrative access to EC2 instances without opening inbound ports.

### Benefits

- No SSH key management
- No bastion host maintenance
- Full audit logging
- IAM-based access control

### Architecture Change

Before:

```text
Administrator
      ↓
Bastion Host
      ↓
Private EC2
```

After:

```text
Administrator
      ↓
SSM Session Manager
      ↓
Private EC2
```

---

# AWS Control Tower

## Landing Zone Accounts

```text
Management
Log Archive
Audit
Production
```

## Guardrails

### Preventive

Implemented using:

```text
Service Control Policies (SCPs)
```

Examples:

- Prevent CloudTrail deletion
- Restrict unauthorized Region usage

### Detective

Implemented using:

```text
AWS Config Rules
```

Examples:

- Detect public S3 buckets
- Detect unencrypted resources

## Why Control Tower?

Provides automated governance for AWS Organizations.

### Benefits

- Standardized account setup
- Built-in security controls
- Simplified compliance management

---

# AWS Trusted Advisor

## Support Plan

```text
Business Support
```

## Categories Reviewed

- Cost Optimization
- Security
- Performance
- Fault Tolerance
- Service Limits

## Why Trusted Advisor?

Provides account-specific AWS best-practice recommendations.

### Benefits

- Security improvement suggestions
- Cost-saving opportunities
- Reliability enhancements
- Continuous account review

---

# Summary

FinTrust's Week 6 security architecture combines preventative, detective, and operational security controls. AWS Config enforces compliance, CloudTrail provides auditing, Secrets Manager protects credentials, ACM secures HTTPS communication, WAF and Shield protect external-facing applications, and Session Manager replaces traditional SSH access. Together, these services create a secure, compliant, and scalable security foundation suitable for a financial services environment.