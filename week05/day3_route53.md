# Week 5 Day 3: Route 53 and Edge Services

## Overview

Today's sessions focused on DNS, traffic management, and edge services in AWS. We learned how Amazon Route 53 routes traffic to applications, how different routing policies support business requirements, and how CloudFront and Global Accelerator improve application performance and availability for global users.

Using the FinTrust Bank scenario, we designed DNS and traffic management solutions to support high availability, disaster recovery, global performance, and canary deployments.

---

## AM Session: Route 53 and Edge Services

### Topics Covered

- Amazon Route 53
- Hosted Zones
- DNS Record Types
- Alias Records
- CNAME Records
- TTL (Time to Live)
- Route 53 Health Checks
- Routing Policies
- Amazon CloudFront
- AWS Global Accelerator
- CloudFront Security Features
- Origin Access Control (OAC)
- AWS WAF and Shield

---

## Key Learning

One of the most important concepts was understanding that Route 53 operates at the DNS layer, while a Load Balancer operates at the application or network layer.

Route 53 decides where traffic should go before a connection is established, whereas a Load Balancer distributes traffic after it arrives.

Another important lesson was the difference between Alias and CNAME records:

- Alias records can point to AWS resources.
- Alias records can be used at the root domain.
- CNAME records can only be used on subdomains.

---

## Route 53 Routing Policies

### Simple Routing

Used when:

- One endpoint exists
- No routing logic is required

### Weighted Routing

Used when:

- Traffic must be split between versions
- Canary deployments are required
- A/B testing is performed

### Latency Routing

Used when:

- Users should be routed to the region with the lowest latency

### Failover Routing

Used when:

- Disaster Recovery (DR) is required
- Automatic failover between primary and secondary environments is needed

### Geolocation Routing

Used when:

- Traffic should be routed based on country or continent
- Compliance requirements apply

### Geoproximity Routing

Used when:

- Traffic needs to be shifted toward a specific region using bias values

### Multivalue Routing

Used when:

- Multiple healthy endpoints should be returned
- Basic DNS-level load balancing is required

---

## CloudFront vs Global Accelerator

### Amazon CloudFront

Best suited for:

- Content delivery
- Website acceleration
- Static content caching
- Images, CSS, JavaScript files
- API acceleration

Benefits:

- Edge caching
- Reduced latency
- Reduced origin load
- AWS WAF integration

### AWS Global Accelerator

Best suited for:

- TCP and UDP applications
- Real-time services
- Trading applications
- Static Anycast IP requirements
- Fast regional failover

Benefits:

- Static IP addresses
- Instant failover
- Uses the AWS global backbone
- Supports non-HTTP traffic

---

## PM Session: Route 53 Hosted Zone Lab

### Hosted Zone Configuration

Created:

```text
fintrust-lab.internal
```

Hosted Zone Type:

```text
Public Hosted Zone
```

AWS automatically created:

```text
NS Records
SOA Record
```

---

## Record Configuration

### Alias Record

```text
app.fintrust-lab.internal
```

Points to:

```text
fintrust-alb
```

Reason:

- Supports AWS resources
- No query cost
- Automatically updates when ALB IPs change

### CNAME Record

```text
api.fintrust-lab.internal
```

Points to:

```text
fintrust-alb DNS Name
```

Reason:

- Suitable for subdomains
- Routes traffic to the ALB

---

## Weighted Routing Configuration

Created two weighted records:

### Production

```text
Weight: 90
```

### Canary

```text
Weight: 10
```

Traffic distribution:

```text
90% → Production
10% → Canary
```

This allows a new version of the application to be tested with a small percentage of users before a full deployment.

---

## Routing Policy Decision Table

| Requirement | Routing Policy |
|------------|----------------|
| Route users by country | Geolocation |
| 80/20 rollout between versions | Weighted |
| Lowest latency region | Latency |
| Automatic disaster recovery failover | Failover |
| Multiple healthy endpoints | Multivalue |
| Single endpoint, no routing rules | Simple |

---

## Canary Deployment Approach

To gradually release a new application version, the routing weights can be adjusted over time:

```text
Production: 100
Canary: 0
```

↓

```text
Production: 90
Canary: 10
```

↓

```text
Production: 50
Canary: 50
```

↓

```text
Production: 0
Canary: 100
```

This approach reduces deployment risk by exposing the new version to a small group of users before full rollout.

---

## Reflection

Today's sessions helped me understand how DNS contributes to application architecture beyond simply translating names into IP addresses. Route 53 can perform intelligent routing decisions that improve availability, performance, and disaster recovery.

The concept I found most valuable was weighted routing because it provides a safe method for gradually deploying new application versions. I also gained a better understanding of the difference between CloudFront and Global Accelerator. CloudFront improves performance through caching, while Global Accelerator improves performance through optimized network routing and fast failover.

Finally, I learned that Route 53 does not replace a Load Balancer. Instead, Route 53 and Load Balancers work together, with Route 53 directing users to the correct endpoint and the Load Balancer distributing traffic across the application resources.