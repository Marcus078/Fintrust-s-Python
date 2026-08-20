# Week 6 FinTrust Security Architecture Summary

## Executive Summary

FinTrust has implemented a layered AWS security architecture designed to deliver high availability, secure identity management, continuous compliance, proactive threat detection, and automated incident response. The architecture follows AWS Well-Architected Framework principles and security best practices while supporting POPIA compliance requirements. Each layer complements the others, creating a resilient and secure cloud platform capable of supporting both internal employees and external banking customers at scale.

---

## High Availability Layer

The foundation of the FinTrust environment is a highly available infrastructure spanning multiple Availability Zones. Public-facing applications run behind Application Load Balancers and Auto Scaling Groups to automatically distribute traffic and recover from instance failures. Critical databases use Amazon RDS Multi-AZ deployments to provide automatic failover and high availability. Customer-facing content is distributed globally through Amazon CloudFront, reducing latency and improving resilience. This architecture eliminates single points of failure and ensures that services remain available even during infrastructure outages, supporting FinTrust's operational and customer service objectives.

---

## Identity and Access Management Layer

FinTrust manages workforce access through IAM Identity Center integrated with Active Directory, allowing more than 300 employees to securely access AWS using their existing corporate credentials without creating individual IAM users. Customer authentication is handled through Amazon Cognito, where User Pools provide authentication and Identity Pools exchange JWT tokens for temporary AWS credentials using STS. More than 100,000 customers can securely access their own S3 resources without requiring AWS accounts. Permission Boundaries are applied to DevOps roles to prevent privilege escalation while still enabling developers to create service roles. Together, these controls enforce least-privilege access and eliminate the risks associated with long-term credentials.

---

## Security Services Layer

FinTrust uses AWS Config to continuously assess compliance against security requirements such as encryption, public access restrictions, and MFA enforcement. CloudTrail records all management and S3 data events, creating a complete audit trail of account activity. Secrets Manager securely stores database credentials and API keys with automatic rotation policies, while Parameter Store manages non-sensitive application configuration. AWS Certificate Manager provides automated certificate management for CloudFront and Application Load Balancers. AWS WAF protects applications against SQL injection, XSS, and brute-force attacks, while Shield Standard provides always-on DDoS protection. Systems Manager Session Manager replaces traditional SSH and bastion hosts, significantly reducing administrative attack surfaces while providing fully audited access to EC2 instances.

---

## Threat Detection and Incident Response Layer

FinTrust's threat detection capability combines CloudTrail, VPC Flow Logs, GuardDuty, Macie, Inspector, and Detective into a unified security monitoring platform. GuardDuty continuously analyzes activity across CloudTrail logs, DNS logs, and VPC Flow Logs to identify suspicious behavior such as compromised instances, malicious IP communication, and cryptocurrency mining activity. Macie performs scheduled scans of S3 buckets to discover and classify sensitive customer information for POPIA compliance. Inspector continuously assesses EC2 instances and container images for known software vulnerabilities and CVEs. When GuardDuty generates a high-severity finding, EventBridge automatically triggers a Lambda function that isolates the affected EC2 instance by attaching an isolation Security Group and notifying the Security Operations team through SNS. Amazon Detective provides investigators with a correlated view of events, reducing time-to-investigation and accelerating root cause analysis.

---

## Conclusion

The FinTrust AWS architecture delivers security through multiple integrated layers. High availability services keep systems operational, IAM controls ensure secure access, security services enforce governance and compliance, and automated threat detection rapidly identifies and contains security incidents. By combining identity federation, least-privilege access, compliance monitoring, automated remediation, and continuous threat intelligence, FinTrust has established a scalable, secure, and enterprise-ready cloud environment suitable for a modern financial services organization.