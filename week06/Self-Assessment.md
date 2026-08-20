# Week 6 Self-Assessment

## Confidence Ratings (1–5)

### HA and Disaster Recovery (Day 1)

| Topic | Rating | Notes |
|---------|---------|---------|
| Multi-AZ vs Read Replicas | 4 | Comfortable explaining HA vs read scaling scenarios |
| DR Strategies (Backup & Restore, Pilot Light, Warm Standby, Multi-Site) | 3 | Understand concepts but need more RPO/RTO practice |
| CloudWatch Agent vs Default Metrics | 3 | Understand custom metrics but need reinforcement |
| CloudWatch Alarm States | 4 | Confident with OK, ALARM, and INSUFFICIENT_DATA |
| EventBridge → Lambda Automation | 4 | Comfortable with event-driven architectures |

### IAM Advanced (Day 2)

| Topic | Rating | Notes |
|---------|---------|---------|
| Policy Evaluation Order | 5 | Strong understanding of SCP → Boundary → Identity → Resource |
| Permission Boundary Calculations | 4 | Can apply intersection rule confidently |
| STS Temporary Credentials | 4 | Understand Access Key, Secret Key, Session Token |
| SAML vs Cognito Federation | 4 | Comfortable identifying correct solution from exam signal words |
| SCP Management Account Exception | 4 | Can identify related exam traps |

### Security Services (Day 3)

| Topic | Rating | Notes |
|---------|---------|---------|
| Config vs CloudTrail | 5 | Strong understanding of "What" vs "Who" |
| Secrets Manager vs Parameter Store | 4 | Understand automatic rotation requirement |
| ACM us-east-1 Rule | 5 | Fully memorized |
| WAF vs Shield | 4 | Comfortable distinguishing Layer 7 vs Layer 3/4 attacks |
| SSM Session Manager | 4 | Understand benefits and requirements |

### Threat Detection (Day 4)

| Topic | Rating | Notes |
|---------|---------|---------|
| GuardDuty Detection vs Response | 5 | Confident with EventBridge + Lambda remediation pattern |
| GuardDuty vs Macie vs Detective vs Inspector | 5 | Can identify each service quickly from signal words |
| CloudTrail Data Events | 4 | Understand object-level auditing requirements |
| VPC Flow Logs | 3 | Need more practice reading records and interpreting values |
| AWS Pen Testing Rules | 4 | Comfortable with approved testing and DDoS restrictions |

---

# Areas Requiring Further Review

## Priority 1

### Disaster Recovery Strategy Selection

Need additional practice with:

- RPO and RTO comparisons
- Cost trade-offs
- Backup & Restore vs Pilot Light
- Warm Standby vs Multi-Site

Reason:

```text
Exam questions often combine business requirements,
cost, and recovery objectives.
```

---

### VPC Flow Log Interpretation

Need additional practice reading:

```text
Source IP
Destination IP
Ports
Protocol
ACCEPT
REJECT
```

Reason:

```text
Flow Log questions are often presented as
security investigation scenarios.
```

---

## Priority 2

### CloudWatch Agent

Need to revisit:

```text
Memory metrics
Disk metrics
Custom operating system metrics
```

Reason:

```text
Easy to confuse with standard EC2 monitoring.
```

---

# Strong Portfolio Reflection Example

## Weak Entry

> I learned that AWS Config monitors resources and CloudTrail tracks user activity.

This only restates definitions.

---

## Strong Entry

For FinTrust's compliance requirements, I selected **AWS Config** to continuously verify that all S3 buckets remain encrypted and that public access is blocked. Config was chosen because it evaluates the current compliance state of resources and retains configuration history. However, Config could not answer who made a change, so **CloudTrail** was also enabled.

When investigating a scenario where an S3 bucket's encryption settings were disabled, CloudTrail provided the IAM user, source IP address, API call, and timestamp of the change. This allowed compliance teams to identify the responsible user while Config confirmed the resource was currently non-compliant.

The trade-off is that CloudTrail provides audit history but does not evaluate compliance, while Config provides compliance monitoring but not detailed user activity. FinTrust therefore requires both services to meet POPIA auditing and security requirements.

---

# Week 6 Overall Confidence

| Domain | Score |
|----------|---------|
| HA & Disaster Recovery | 3.6 / 5 |
| IAM Advanced | 4.2 / 5 |
| Security Services | 4.4 / 5 |
| Threat Detection | 4.2 / 5 |

## Overall Week 6 Confidence

```text
4 / 5
```

### Strengths

- IAM Architecture
- Federation
- SCPs
- Permission Boundaries
- Config vs CloudTrail
- Secrets Manager
- WAF / Shield
- GuardDuty / Macie / Detective / Inspector

### Improvement Areas

- Disaster Recovery strategies
- VPC Flow Log analysis
- CloudWatch Agent metrics

### Exam Readiness Assessment

```text
Week 6 Topics:
Approximately 80–85% Exam Ready

Focus revision on:
- DR strategy selection
- CloudWatch monitoring
- VPC Flow Logs

These are the areas most likely to cause confusion
in multi-service scenario questions.
```