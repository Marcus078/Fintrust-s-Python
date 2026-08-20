# Week 5 Mock Exam Review

## Exam Summary

**Mock Exam:** AWS Solutions Architect Associate Practice Exam 2  
**Score Achieved:** Approximately 37%  
**Overall Result:** Needs Improvement

This mock exam highlighted several weak areas in AWS architecture design, particularly around networking, storage services, database services, migration tools, high availability, disaster recovery, and caching solutions.

My strongest areas were:

- EBS and Storage
- Security Groups
- DynamoDB
- Route 53 basics
- RDS Multi-AZ concepts
- EFS lifecycle policies

Areas requiring additional revision:

- Networking and Hybrid Connectivity
- Disaster Recovery Architectures
- Route 53 Advanced Features
- CloudFront and Edge Services
- AWS Migration Services
- Database Caching Solutions
- Auto Scaling Strategies
- VPC Endpoints
- FSx Storage Services
- EKS Scaling

---

# Questions I Got Correct

| Question | Topic |
|----------|--------|
| Q1 | RDS Multi-AZ Migration |
| Q6 | Security Groups |
| Q8 | EFS Lifecycle Policies |
| Q9 | EBS Snapshots |
| Q12 | S3 Lifecycle |
| Q13 | EBS Throughput Optimized HDD |
| Q14 | Provisioned IOPS SSD |
| Q20 | EBS Snapshots |
| Q23 | Bastion Host Architecture |
| Q26 | EC2 Block Device Mapping |
| Q30 | Virtual Private Gateway |
| Q33 | ECS Event Processing |
| Q35 | DynamoDB |
| Q36 | DynamoDB |
| Q43 | Amazon EFS |
| Q44 | S3 Object Lock |
| Q48 | CloudFront + DAX |
| Q49 | Security Groups |
| Q50 | DynamoDB Sessions |
| Q51 | CloudFront |
| Q52 | VPC Sharing |
| Q54 | CloudFront + S3 |

---

# Questions I Struggled With

## Networking

### Q2
**Topic:** Site-to-Site VPN High Availability

**Key Learning:**

When an on-premises environment uses a single customer gateway device, it becomes a single point of failure.

Correct solution:

```text
Add a second customer gateway device
Create additional VPN connections
```

**Exam Signal Words:**

- Single point of failure
- VPN resilience
- Customer gateway failure

---

### Q21

**Topic:** Direct Connect Gateway

**Revision Note:**

A Direct Connect Gateway can be associated with multiple Virtual Private Gateways across multiple VPCs.

Remember:

```text
Direct Connect Gateway
          ↓
Virtual Private Gateways
          ↓
Multiple VPCs
```

---

### Q37

**Topic:** S3 VPC Endpoints

**Revision Note:**

For private access to S3:

```text
Gateway Endpoint
```

Requirements:

- Traffic stays on AWS network
- No public internet
- Use bucket policies to restrict access

---

### Q41

**Topic:** NAT Gateway

**Key Rule**

```text
Private Subnet
      ↓
NAT Gateway
      ↓
Internet Gateway
      ↓
Internet
```

For outbound-only internet access:

- NAT Gateway required
- Internet Gateway required
- No public IPs needed

---

### Q62

**Topic:** NAT High Availability

**Must Memorise**

```text
One NAT Gateway per AZ
```

This removes single points of failure.

---

### Q63

**Topic:** NACLs vs Security Groups

**Important Difference**

Security Groups:

```text
Allow only
```

NACLs:

```text
Allow
Deny
```

Block CIDR traffic:

```text
Use NACL DENY rule
```

---

# Route 53 and CloudFront

---

### Q42

**Topic:** CloudFront + Route 53

**Correct Pattern**

```text
Route 53 Alias Record
        ↓
CloudFront Distribution
        ↓
S3 Bucket
```

Remember:

```text
Root domain = Alias
NOT CNAME
```

---

### Route 53 Revision Checklist

I need to revisit:

- Weighted Routing
- Failover Routing
- Geolocation Routing
- Latency Routing
- Alias vs CNAME
- Health Checks
- CloudFront Integration

---

# Load Balancers

---

### Q15

**Topic:** ALB vs NLB

**Correct Answer**

```text
TCP
Ultra Low Latency
Millions of Requests
Static IPs

= NLB
```

**Exam Signals**

```text
HTTP/HTTPS = ALB

TCP/UDP = NLB

Firewalls = GWLB
```

---

# Database Services

---

### Q24

**Topic:** Memcached vs Redis

**Memcached**

Use when:

- Simple caching
- Multi-threaded
- No replication

**Redis**

Use when:

- High availability
- Replication
- Persistence

---

### Q29

**Topic:** Redis

**Exam Signal**

```text
In-memory database
Replication
High performance
```

Answer:

```text
ElastiCache for Redis
```

---

### Q40

**Topic:** Database Caching

Need sub-millisecond reads:

```text
ElastiCache
```

Not:

```text
Read Replica
```

Read replicas improve read scaling but not caching.

---

### Q55

**Topic:** Aurora

When asked:

```text
Highest availability
Lowest administration
Read scaling
```

Answer:

```text
Aurora + Aurora Replicas
```

---

# Disaster Recovery

---

### Q17

**Topic:** Pilot Light

Cost-effective DR solution:

```text
AMIs
     ↓
Copy to Second Region
     ↓
CloudFormation
     ↓
Launch During Disaster
```

Important:

CloudFormation is preferred over custom Lambda scripts.

---

### Q25

**Topic:** Aurora Global Database

Revision:

For global database failover:

```text
Aurora Global Database
```

Benefits:

- Cross-region replication
- Fast failover
- Global availability

---

### Q27

**Topic:** Global DR

Question asked:

```text
RPO = 1 second
RTO = 1 minute
```

Answer:

```text
Aurora Global Database
```

---

### Q53

**Topic:** Cross-Region Recovery

Remember:

```text
Create AMIs
Copy AMIs to Region B
```

Then launch infrastructure from those AMIs.

---

# Migration Services

---

### Q4

**Topic:** DataSync

Need:

- Managed migration
- On-premises to S3
- Direct Connect
- Private transfer

Answer:

```text
AWS DataSync
+ VPC Endpoint
```

---

### Q5

**Topic:** DFS Namespace

Answer:

```text
AWS DataSync
+
FSx Windows File Server
```

---

### Q47

**Topic:** SMB File Shares

SMB workload:

```text
FSx for Windows File Server
```

Migration:

```text
AWS DataSync
```

---

# EKS and Auto Scaling

---

### Q10

Need:

```text
Pod Scaling
+
Node Scaling
```

Answer:

```text
Cluster Autoscaler
+
Metrics Server
+
Horizontal Pod Autoscaler
```

Remember:

- HPA scales Pods
- Cluster Autoscaler scales Nodes

---

### Q34

**Topic:** Predictable Workloads

Exam Signal:

```text
Every month
Same day
Same time
```

Answer:

```text
Scheduled Scaling
```

Not dynamic scaling.

---

### Q56

**Topic:** Cost Optimization

Predictable demand:

```text
On-Demand
+
Spot Instances
```

Provides lowest cost.

---

# Storage Services

---

### Q32

**Topic:** S3 Lifecycle**

Need retrieval within minutes after 3 months.

Correct storage:

```text
S3 Glacier Flexible Retrieval
```

Remember:

```text
Minutes Retrieval
=
Glacier
```

---

### Q45

**Topic:** Automatic Deletion

Need deletion after 60 days.

Answer:

```text
Lifecycle Policy
+
Expiration
```

---

### Q61

**Topic:** RDS Storage Growth

Least operational overhead:

```text
Storage Auto Scaling
```

---

# FSx Services Revision

Need additional revision on:

```text
FSx for Windows File Server
FSx for Lustre
FSx for OpenZFS
FSx for NetApp ONTAP
```

### Quick Memory Guide

```text
Windows SMB
    ↓
FSx Windows

Linux NFS
    ↓
EFS

HPC
    ↓
FSx Lustre

Enterprise NAS
    ↓
FSx ONTAP
```

---

# Study Plan Before Next Mock

## Priority 1

- Route 53
- CloudFront
- Global Accelerator
- Load Balancers

## Priority 2

- Disaster Recovery
- Aurora Global Database
- Direct Connect
- Transit Gateway

## Priority 3

- Migration Services
- DataSync
- FSx
- Storage Gateway

## Priority 4

- EKS
- ECS
- Auto Scaling
- ElastiCache

---

## Final Reflection

Although my score was only **37%**, the exam clearly identified the areas I need to improve. Most of my incorrect answers came from networking, disaster recovery, caching, migration, and advanced AWS managed services rather than core compute or storage concepts. My goal before the next mock exam is to strengthen these weak areas, especially Route 53, CloudFront, Direct Connect, Aurora Global Database, NAT Gateway design, and ElastiCache, as these topics appear frequently in AWS Solutions Architect Associate exam scenarios.