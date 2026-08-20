# Day 4 – Incident Response Flow Diagram

## Overview

FinTrust uses AWS native threat detection and automated response services to rapidly detect, investigate, and contain security incidents. High-severity GuardDuty findings trigger automated remediation through EventBridge and Lambda, while CloudTrail, VPC Flow Logs, Inspector, Macie, and Detective provide visibility across the environment.

---

# Automated Incident Response Flow

## GuardDuty → EventBridge → Lambda → Isolation Security Group

```text
+------------------+
|   GuardDuty      |
| High Severity    |
| Finding Raised   |
+--------+---------+
         |
         v
+------------------+
|   EventBridge    |
| Rule Matches     |
| Severity >= 7    |
+--------+---------+
         |
         v
+------------------+
|     Lambda       |
| Response Function|
+--------+---------+
         |
         +--------------------+
         |                    |
         v                    v
+----------------+    +----------------+
| Modify EC2 SG  |    | SNS Alert      |
| Attach         |    | Notify SOC     |
| Isolation SG   |    | Security Team  |
+----------------+    +----------------+
         |
         v
+------------------+
| Compromised EC2  |
| Fully Isolated   |
+------------------+
         |
         v
+------------------+
| Amazon Detective |
| Root Cause       |
| Investigation    |
+------------------+
```

---

# Example GuardDuty Finding

### Simulated Finding

```text
Finding Type:
UnauthorizedAccess:EC2/TorIPCaller

Severity:
8.5 (High)

Resource:
i-0abc123456789def0

Description:
EC2 instance communicated with an IP address
associated with the TOR anonymous network.

Region:
af-south-1

Action Taken:
Automatic Isolation Triggered
```

### Why This Matters

GuardDuty continuously analyzes:

- CloudTrail logs
- VPC Flow Logs
- DNS logs

to identify suspicious activity.

Examples include:

- Cryptocurrency mining
- TOR network access
- Known malicious IP communication
- Credential compromise
- Anomalous API calls

### Important Exam Rule

```text
GuardDuty Detects

GuardDuty Does NOT Remediate
```

Automated remediation requires:

```text
GuardDuty
     ↓
EventBridge
     ↓
Lambda
     ↓
Response Action
```

---

# Lambda Isolation Process

When a high-severity finding is raised:

### Step 1

Extract the EC2 Instance ID from the GuardDuty finding.

### Step 2

Replace existing Security Groups with:

```text
sg-isolation
```

### Step 3

Isolation Security Group Rules

Inbound:

```text
None
```

Outbound:

```text
None
```

Result:

```text
No inbound connectivity
No outbound connectivity
No lateral movement
```

The instance remains running for forensic investigation while immediately losing network access.

---

# CloudTrail Data Events Configuration

## Enabled Event Types

### Management Events

```text
Enabled
```

Examples:

- RunInstances
- CreateBucket
- DeleteRole
- ModifySecurityGroup

### S3 Data Events

```text
Enabled
```

Examples:

- GetObject
- PutObject
- DeleteObject

---

## FinTrust Configuration

```text
CloudTrail
   ↓
Multi-Region Trail
   ↓
S3 Log Archive Account
   ↓
CloudWatch Logs
```

Additional protections:

```text
MFA Delete
Log File Validation
S3 Object Lock
```

### Why S3 Data Events Were Enabled

Management Events answer:

```text
Who changed the bucket?
```

Data Events answer:

```text
Who accessed the object?
```

### Common Exam Trap

```text
CloudTrail enabled
≠
Object-level auditing enabled
```

S3 Data Events must be explicitly configured.

---

# VPC Flow Log Analysis

## Sample Flow Log Record

```text
2 123456789 eni-123abc
203.0.113.10 10.0.1.15
45520 22
6
1
52
1700000000
1700000020
REJECT
OK
```

---

## Annotated Flow Log

| Field | Value | Meaning |
|---------|---------|----------|
| Source IP | 203.0.113.10 | External client or attacker |
| Destination IP | 10.0.1.15 | EC2 instance |
| Source Port | 45520 | Client ephemeral port |
| Destination Port | 22 | SSH |
| Protocol | 6 | TCP |
| Packets | 1 | One packet sent |
| Bytes | 52 | Very small payload |
| Action | REJECT | Blocked by SG or NACL |
| Status | OK | Flow log recorded successfully |

---

## Security Interpretation

```text
External Host
       ↓
Attempted SSH Connection
       ↓
Port 22
       ↓
Traffic Rejected
       ↓
No Access Granted
```

This is commonly seen during:

- Internet scanning
- Brute-force attacks
- SSH probing
- Reconnaissance activity

---

# VPC Flow Log Alerting

FinTrust publishes Flow Logs to:

```text
CloudWatch Logs
```

A metric filter searches for:

```text
REJECT
```

records.

When suspicious activity exceeds thresholds:

```text
CloudWatch Alarm
        ↓
SNS Notification
        ↓
Security Team Alert
```

---

# Threat Detection Service Stack

## GuardDuty

Purpose:

```text
Threat Detection
```

Finds:

- Compromised instances
- Malicious IP activity
- Cryptocurrency mining
- Suspicious API usage

---

## Detective

Purpose:

```text
Investigation
```

Answers:

```text
What happened?
Why did it happen?
What else was affected?
```

---

## Macie

Purpose:

```text
PII Discovery
```

Finds:

- ID numbers
- Credit card data
- Customer personal information

Scope:

```text
Amazon S3 Only
```

---

## Inspector

Purpose:

```text
Vulnerability Scanning
```

Finds:

- CVEs
- Outdated packages
- Vulnerable container images

---

# FinTrust Threat Detection Architecture

```text
CloudTrail
      +
VPC Flow Logs
      +
DNS Logs
      ↓
GuardDuty
      ↓
High Severity Finding
      ↓
EventBridge
      ↓
Lambda
      ↓
Isolation Security Group
      ↓
SNS Alert
      ↓
Security Operations Team
      ↓
Amazon Detective Investigation
```

---

# Conclusion

FinTrust's threat detection architecture combines CloudTrail, VPC Flow Logs, GuardDuty, Macie, Detective, and Inspector to provide comprehensive security visibility. High-severity GuardDuty findings automatically trigger EventBridge and Lambda workflows that isolate compromised instances within minutes, while CloudTrail and VPC Flow Logs provide the forensic evidence required for investigation. This automated response model reduces incident response times, limits potential damage, and supports FinTrust's security and compliance requirements.