# FinTrust Well-Architected Framework Pillar Mapping

## Scenario 1

Infrastructure changes must be reviewed and deployed automatically through a pipeline.

Pillar:
Operational Excellence

Justification:
This implements the "Perform Operations as Code" principle using CloudFormation and CodePipeline.

---

## Scenario 2

Database credentials are stored in Secrets Manager and administrators use Session Manager instead of SSH.

Pillar:
Security

Justification:
This implements the Security principle "Keep People Away from Data" by reducing direct access and removing exposed credentials.

---

## Scenario 3

Retail payments run across multiple Availability Zones.

Pillar:
Reliability

Justification:
Multi-AZ design removes single points of failure and supports automatic recovery.

---

## Scenario 4

CloudFront is used to cache content globally and reduce latency.

Pillar:
Performance Efficiency

Justification:
Caching and global edge delivery improve application performance.

---

## Scenario 5

S3 Lifecycle moves archive data to Glacier Deep Archive.

Pillar:
Cost Optimisation

Justification:
Storage costs are reduced while maintaining retention requirements.

---

## Scenario 6

Application workloads are migrated to Graviton instances.

Pillar:
Sustainability

Justification:
Graviton improves compute efficiency and reduces environmental impact.
