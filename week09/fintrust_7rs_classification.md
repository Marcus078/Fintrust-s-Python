# FinTrust 7Rs Migration Classification

| Workload Group | Count | Strategy | Justification |
|---------------|--------|----------|---------------|
| Legacy Reporting Servers | 312 | Retire | Replaced by QuickSight analytics platform |
| Mainframe Dependency Systems | 89 | Retain | Compliance and HSM dependencies require on-prem retention |
| Standard Application Servers | 1847 | Rehost | Fastest migration path using AWS MGN |
| Database and App Platform Servers | 234 | Replatform | Move to Amazon RDS and ECS with minimal code changes |
| CRM Platform | 12 | Repurchase | Replace with SaaS solution such as Salesforce |
| Core Banking Modernization Services | 365 | Refactor | Strategic move to Lambda and ECS microservices |
| VMware Workloads | 0 | Relocate | Not used in FinTrust migration program |