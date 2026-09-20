# FinTrust Resilience Architecture

## Retail Payments

Strategy:
Multi-Site Active-Active

Primary:
af-south-1

Secondary:
eu-west-1

RTO:
Seconds

RPO:
Near Zero

Components:

- Route 53 Health Checks
- Aurora Global Database
- ECS Services
- Load Balancers

---

## FCA Reporting

Strategy:
Warm Standby

Region:
eu-west-2

RTO:
15 Minutes

RPO:
Seconds

Components:

- Reduced-size ECS Cluster
- Aurora Replica
- Auto Scaling

---

## Internal Tools

Strategy:
Backup and Restore

RTO:
4 Hours

RPO:
24 Hours

Components:

- AWS Backup
- EBS Snapshots
- RDS Snapshots

---

## Resilience Validation

AWS Resilience Hub

- Architecture assessment
- RTO validation
- RPO validation

AWS FIS

- Chaos engineering
- Instance failure tests
- Auto Scaling validation

Current Result:

ASG recovery time:
87 seconds

Target:
< 90 seconds
