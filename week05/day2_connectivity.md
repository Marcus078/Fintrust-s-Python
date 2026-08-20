# Week 5 Day 2: Load Balancers and Connectivity

## Overview

Today's session focused on advanced VPC networking, connectivity options, and Elastic Load Balancers. Using the FinTrust Bank scenario, we explored how AWS services connect applications, VPCs, on-premises environments, and third-party services while maintaining security, scalability, and high availability.

---

## AM Session: Advanced VPC and Connectivity

### Topics Covered

- NAT Gateway High Availability (HA) Design
- NACL Statelessness
- Ephemeral Ports
- Traffic Evaluation Order
- VPC Peering
- AWS Transit Gateway
- AWS PrivateLink
- AWS Site-to-Site VPN
- AWS Client VPN
- AWS Direct Connect
- Application Load Balancer (ALB)
- Network Load Balancer (NLB)
- Gateway Load Balancer (GWLB)

### Key Takeaways

- NAT Gateways are Availability Zone specific.
- High availability requires one NAT Gateway per Availability Zone.
- VPC Peering is suitable for small-scale VPC connectivity.
- Transit Gateway provides centralized routing for multiple VPCs.
- PrivateLink provides private access to specific services without exposing an entire VPC.
- Direct Connect provides dedicated private connectivity between on-premises environments and AWS.

---

## Load Balancer Selection

### Application Load Balancer (ALB)

Used for:

- HTTP and HTTPS traffic
- Path-based routing
- Host-based routing
- Microservices architectures
- TLS termination

### Network Load Balancer (NLB)

Used for:

- TCP and UDP traffic
- Static IP requirements
- Source IP preservation
- Ultra-low latency workloads

### Gateway Load Balancer (GWLB)

Used for:

- Firewalls
- Intrusion Detection Systems (IDS)
- Intrusion Prevention Systems (IPS)
- Deep packet inspection solutions

---

## FinTrust Load Balancer Decision

FinTrust selected an **Application Load Balancer (ALB)** because the application requires path-based routing.

### Routing Rules

```text
/api/*      → API Service
/portal/*   → Customer Portal
Default     → Portal Service
```

---

## PM Session: ALB and Connectivity Design Lab

During the practical session, I configured an Application Load Balancer and completed a connectivity architecture exercise.

### ALB Configuration

**Load Balancer**

```text
fintrust-alb
```

**Target Groups**

```text
api-targets
portal-targets
```

**Listener Rules**

```text
/api/*     → api-targets
/portal/*  → portal-targets
```

---

## Connectivity Architecture Decisions

### Connect Production, Development, and Audit VPCs

**Selected Service:** AWS Transit Gateway

**Reason:** Centralized routing with transitive connectivity across multiple VPCs.

### Private Access to a Compliance SaaS API

**Selected Service:** AWS PrivateLink

**Reason:** Provides private access to a specific service without exposing the VPC.

### Connect FinTrust Mainframe to AWS

**Selected Service:** AWS Direct Connect

**Reason:** Dedicated private connection with predictable performance and latency.

### Remote Access for DevOps Engineers

**Selected Service:** AWS Client VPN

**Reason:** Secure remote connectivity for individual users.

---

## Request Path Walkthrough

A customer accesses the following URL:

```text
https://fintrust.co.za/api/transfer
```

Traffic flow:

```text
User Browser
    ↓
Route 53
    ↓
Application Load Balancer
    ↓
Listener Rule (/api/*)
    ↓
api-targets
    ↓
ECS Container
    ↓
Application Service
    ↓
Database Layer
```

---

## Reflection

Today's session deepened my understanding of AWS networking and connectivity. I learned how different connectivity services address different business requirements and why it is important to select the correct load balancer based on the application's protocol and routing needs.

The most valuable lesson was understanding the difference between Transit Gateway and PrivateLink. Transit Gateway connects multiple networks, while PrivateLink securely exposes a specific service. I also gained practical experience configuring path-based routing with an Application Load Balancer, which is an important component of the FinTrust architecture.