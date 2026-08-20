# Week 5 Day 4: Route 53 Failover and CloudFront

## Overview

Today's sessions focused on Route 53 Failover Routing, CloudFront distributions, Origin Access Control (OAC), caching strategies, and content delivery architecture.

Using the FinTrust Bank scenario, we explored how AWS improves application availability through DNS failover and how CloudFront securely delivers content from private S3 buckets while improving performance through global edge locations.

---

## AM Session: Route 53 Failover and CloudFront Fundamentals

### Topics Covered

- Route 53 Failover Routing
- Route 53 Health Checks
- Active-Passive Disaster Recovery
- CloudFront Distributions
- CloudFront Origins
- Cache Behaviours
- Origin Access Control (OAC)
- Signed URLs
- Signed Cookies
- CloudFront Caching
- Cache Invalidation
- AWS WAF Integration
- AWS Shield Standard

---

## Route 53 Failover Routing

Failover Routing provides automatic disaster recovery using a primary and secondary endpoint.

### Primary Endpoint

- Active endpoint
- Receives all traffic while healthy
- Requires an attached health check

### Secondary Endpoint

- Standby endpoint
- Receives traffic only when the primary endpoint becomes unhealthy

### Failover Process

```text
Primary Endpoint Fails
        ↓
Health Check Detects Failure
        ↓
Route 53 Marks Endpoint Unhealthy
        ↓
DNS Responses Switch to Secondary Endpoint
        ↓
Clients Connect to Secondary Environment
```

### Key Learning

A health check is mandatory for the primary record.

Without a health check, Route 53 cannot detect failures and failover will never occur.

---

## Route 53 Health Check Types

### Endpoint Health Check

Monitors:

- HTTP
- HTTPS
- TCP endpoints

### CloudWatch Alarm Health Check

Used for:

- Private VPC resources
- Internal applications
- Private databases

### Calculated Health Check

Combines multiple health checks into a single result.

---

## CloudFront Fundamentals

CloudFront is AWS's Content Delivery Network (CDN).

Its purpose is to:

- Reduce latency
- Improve user experience
- Cache content at edge locations
- Reduce load on backend resources
- Improve application security

---

## CloudFront Components

### Distribution

The CloudFront configuration that serves content globally.

### Origin

The source of content:

- Amazon S3
- Application Load Balancer
- EC2
- API Gateway

### Cache Behaviour

Rules that determine:

- Which origin handles requests
- Cache settings
- TTL values

### Edge Locations

Global locations used to cache content closer to users.

---

## OAC vs OAI

### Origin Access Control (OAC)

Current AWS recommended approach.

Benefits:

- Supports AWS KMS encrypted buckets
- Uses SigV4 request signing
- Better security model
- Recommended for all new deployments

### Origin Access Identity (OAI)

Legacy approach.

Limitations:

- Older implementation
- No support for KMS encrypted buckets
- Being replaced by OAC

### Why OAC is Preferred

OAC provides stronger security, supports modern AWS features, and integrates directly with CloudFront request signing.

---

## Signed URLs vs Signed Cookies

### Signed URLs

Best used when:

- Access is granted to a single file
- Temporary downloads are required
- Individual documents are protected

FinTrust Example:

```text
Monthly Bank Statement PDF
```

Each customer receives a unique URL that expires after a set period.

---

### Signed Cookies

Best used when:

- Access is required to multiple files
- Subscription content is provided
- Streaming platforms are used

Example:

```text
Premium Customer Portal
```

One cookie grants access to multiple protected resources.

---

## PM Session: CloudFront Distribution Lab

### Lab Objective

Create a CloudFront distribution in front of a private S3 bucket and secure access using OAC.

---

## Distribution Configuration

### S3 Bucket

```text
fintrust-portal-assets
```

Configuration:

- Block all public access enabled
- Static website assets uploaded
- Direct public access disabled

---

### CloudFront Distribution

Configuration:

```text
Origin: S3 Bucket
OAC: Enabled
Protocol Policy: Redirect HTTP to HTTPS
Default Root Object: index.html
```

---

### Cache Behaviour

#### Static Content

```text
/static/*
```

Configuration:

```text
Long TTL
Caching Enabled
```

Used for:

- Images
- CSS
- JavaScript

---

#### Dynamic Content

```text
/api/*
```

Configuration:

```text
CachingDisabled
TTL = 0
```

Used for:

- API requests
- Dynamic responses
- Banking transactions

---

## Route 53 Failover Activity

During the lab, failover routing was tested between two servers.

### Results

1. Primary server was healthy.
2. DNS resolved to the primary endpoint.
3. Primary service was stopped.
4. Health check became unhealthy.
5. Route 53 began serving the secondary endpoint.
6. DNS traffic automatically failed over.
7. Primary service was restored.
8. Traffic returned to the primary endpoint.

### Key Observation

TTL controls how quickly users receive updated DNS results.

Recommended Failover TTL:

```text
30–60 seconds
```

---

## FinTrust Architecture Review

By the end of Week 5, the FinTrust environment includes:

### Networking

- Amazon VPC
- Public and Private Subnets
- Route Tables
- Internet Gateway
- NAT Gateways
- Security Groups

### Connectivity

- Transit Gateway
- VPC Peering concepts
- PrivateLink
- Direct Connect

### Load Balancing

- Application Load Balancer
- Path-Based Routing

### DNS

- Route 53 Hosted Zones
- Alias Records
- Weighted Routing
- Failover Routing
- Health Checks

### Content Delivery

- CloudFront Distribution
- OAC-Protected S3 Origin
- Cache Behaviours
- Signed URLs
- Signed Cookies

---

## Reflection

Today's sessions demonstrated how DNS, content delivery, and disaster recovery work together within a cloud architecture. I learned that Route 53 failover depends on both health checks and TTL values, making DNS an important component of high availability planning.

The most valuable lesson was understanding the difference between OAC and OAI. OAC is the modern and more secure approach because it supports request signing and KMS-encrypted S3 buckets. I also gained practical experience building a CloudFront distribution and securing a private S3 bucket so that content can only be accessed through CloudFront.

Another important takeaway was learning how cache behaviours allow different content types to be handled differently. Static content benefits from long cache durations, while dynamic API traffic should not be cached. This provides a balance between performance, security, and application functionality.