## Day 1 - Cost Optimisation and Financial Governance

Week 9 introduced financial governance and cost optimisation across the FinTrust AWS environment.

FinTrust operates fourteen AWS accounts under a single AWS Organization. Compute Savings Plans were selected because they provide coverage for Amazon EC2, AWS Fargate, and AWS Lambda workloads deployed throughout Weeks 6 to 8.

The cost optimisation strategy reduced annual compute spend by approximately $847,000 compared to On-Demand pricing.

Migration Evaluator analysis compared the existing on-premises estate with the target AWS architecture. Results demonstrated a projected 67% reduction in total cost of ownership through improved utilisation, managed services, Auto Scaling, and reduced infrastructure operations requirements.

These financial controls ensure that the FinTrust platform remains both technically scalable and economically sustainable.

## Day 2 - FinOps and Cost Governance

FinTrust expanded its financial governance model using Cost Explorer, AWS Budgets, Cost and Usage Reports, Athena and QuickSight.

AWS Budgets were configured for each major business unit with alerts at 80%, 90% and 100% utilisation. Budget notifications are delivered through SNS and collaboration channels to ensure timely intervention.

The Cost and Usage Report pipeline delivers detailed billing data into S3 where Athena and QuickSight provide enterprise cost analytics and chargeback reporting.

Compute Optimizer recommendations identified over-provisioned compute resources throughout the environment and provided opportunities for right-sizing workloads while maintaining performance objectives.

These controls ensure that FinTrust maintains visibility, accountability and governance across its multi-account AWS estate.

## Day 3 - Governance and Migration Strategy

FinTrust strengthened governance controls through AWS Service Catalog and organisation-wide tagging enforcement.

Service Catalog portfolios provide approved deployment patterns for data, infrastructure and banking workloads while enforcing mandatory CostCentre, Team and Environment tags.

Tag auditing was automated using the Resource Groups Tagging API, enabling continuous compliance monitoring and supporting internal chargeback reporting.

Migration planning activities classified the 2,847-server estate using the AWS 7Rs framework. Workloads were categorised for retirement, retention, rehosting, replatforming, repurchasing or refactoring based on business value, technical complexity and long-term strategic goals.

Migration Hub was adopted as the central programme tracking platform for all migration workstreams.

## Day 4 - Migration Execution and Resilience

FinTrust entered the migration execution phase during Week 9.

Oracle core banking databases were migrated from Oracle 19c to Aurora PostgreSQL using AWS Schema Conversion Tool and AWS Database Migration Service. DMS Full Load and CDC enabled near-zero downtime migration with only eight minutes of cutover impact.

Application workloads classified as Rehost were migrated through AWS Application Migration Service using continuous block replication and staged cutovers.

The organisation's 3 PB regulatory archive was transferred using 38 Snowball Edge Storage Optimized devices rather than internet transfer, reducing migration time from approximately 277 days to a few weeks.

Disaster recovery strategy was aligned to workload criticality. Retail payments adopted a Multi-Site Active-Active architecture, FCA reporting adopted Warm Standby, and internal services relied on Backup and Restore.

AWS Resilience Hub and AWS Fault Injection Simulator validate recovery objectives and operational resilience.