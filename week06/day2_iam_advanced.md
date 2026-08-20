# Week 6 Day 2: IAM Advanced and SQL Window Functions

## Overview

Today's sessions covered advanced AWS Identity and Access Management (IAM) concepts used in enterprise environments, including policy evaluation, permission boundaries, IAM roles, AWS STS, federation, IAM Identity Center, and Service Control Policies (SCPs).

The afternoon session focused on SQL Window Functions, including ranking functions, running totals, and period-over-period analysis using LAG and LEAD.

---

# AM Session: IAM Advanced

## Topics Covered

- IAM Policy Types
- Policy Evaluation Order
- Explicit Deny
- Permission Boundaries
- IAM Roles
- Cross-Account Access
- AWS Security Token Service (STS)
- Temporary Credentials
- SAML Federation
- Web Identity Federation
- Amazon Cognito
- IAM Identity Center
- Service Control Policies (SCPs)
- Shared Responsibility Model

---

# IAM Policy Evaluation Order

AWS evaluates permissions using multiple policy layers.

## Evaluation Chain

```text
Explicit Deny
      ↓
Service Control Policy (SCP)
      ↓
Permission Boundary
      ↓
Identity Policy
      ↓
Resource Policy
```

### Important Rule

```text
Explicit Deny Always Wins
```

If any layer contains an explicit deny, access is denied regardless of any allow statements elsewhere.

---

# IAM Policy Types

## Identity Policies

Attached to:

- Users
- Groups
- Roles

Purpose:

```text
Defines what an identity can do
```

Examples:

- AmazonS3ReadOnlyAccess
- PowerUserAccess

---

## Resource Policies

Attached to:

- S3 Buckets
- SQS Queues
- KMS Keys

Purpose:

```text
Defines who can access the resource
```

Common use case:

```text
Cross-account access
```

---

## Permission Boundaries

Purpose:

```text
Maximum permissions an identity can ever receive
```

Permission boundaries do not grant permissions.

They limit permissions.

---

## Service Control Policies (SCPs)

Purpose:

```text
Maximum permissions available within AWS Accounts
```

Applied through:

```text
AWS Organizations
```

---

# Permission Boundaries

## Problem Solved

A developer may have:

```text
IAM:CreateRole
IAM:AttachRolePolicy
```

Without controls they could create:

```text
AdministratorAccess
```

roles and elevate privileges.

---

## Solution

Use Permission Boundaries.

### Example

Identity Policy:

```text
S3:*
EC2:*
IAM:CreateRole
```

Permission Boundary:

```text
S3:*
EC2:*
```

Effective Permissions:

```text
S3:*
EC2:*
```

Blocked:

```text
IAM:CreateRole
```

This follows the:

```text
Intersection Model
```

---

# IAM Roles

IAM Roles provide temporary credentials.

They do not have permanent access keys.

---

## EC2 Instance Roles

Use case:

```text
Applications running on EC2
```

Benefits:

- No hardcoded credentials
- Automatic credential rotation
- Secure access to AWS services

Credentials are delivered through:

```text
Instance Metadata Service (IMDS)
```

---

## Cross-Account Roles

Use case:

```text
Account A accessing Account B
```

Controlled through:

```text
Trust Policies
```

---

## Service Roles

Examples:

```text
Lambda Execution Role
ECS Task Role
CodePipeline Role
```

Allows AWS services to perform actions on your behalf.

---

# AWS STS

## Purpose

AWS Security Token Service issues temporary credentials.

---

## STS Credential Components

Every temporary credential includes:

```text
Access Key ID
Secret Access Key
Session Token
```

All three are required.

Missing a Session Token causes:

```text
Authentication Failure
```

---

## Important STS API Calls

### AssumeRole

Used for:

```text
Cross-account access
```

---

### AssumeRoleWithSAML

Used for:

```text
Corporate users
Active Directory
Azure AD
Okta
ADFS
```

---

### AssumeRoleWithWebIdentity

Used for:

```text
Google Login
Facebook Login
Amazon Cognito
Mobile Applications
```

---

# Identity Federation

Federation allows users to access AWS without creating IAM users.

---

## SAML Federation

Used for:

```text
Corporate Employees
```

Examples:

- Active Directory
- Okta
- ADFS

Flow:

```text
Corporate Identity Provider
        ↓
SAML Assertion
        ↓
STS AssumeRoleWithSAML
        ↓
Temporary AWS Access
```

---

## Web Identity Federation

Used for:

```text
Application Users
```

Examples:

- Google Login
- Facebook Login
- Apple Login

Flow:

```text
Social Login
       ↓
Cognito
       ↓
STS AssumeRoleWithWebIdentity
       ↓
Temporary AWS Credentials
```

---

# Cognito Components

## User Pool

Handles:

```text
Authentication
```

Functions:

- Sign Up
- Sign In
- MFA
- Social Login

Issues:

```text
JWT Tokens
```

---

## Identity Pool

Handles:

```text
Authorization
```

Purpose:

```text
Exchange JWT Tokens for AWS Credentials
```

---

# IAM Identity Center

Formerly:

```text
AWS Single Sign-On
```

Use case:

```text
Manage access across multiple AWS accounts
```

Benefits:

- Centralized access management
- Active Directory integration
- Permission Sets
- Single Sign-On

---

## FinTrust Example

```text
200 Employees
        ↓
Active Directory
        ↓
IAM Identity Center
        ↓
Access to AWS Accounts
```

No IAM users required.

---

# Service Control Policies (SCPs)

## Key Rules

### Rule 1

```text
SCPs NEVER grant permissions
```

They only restrict.

---

### Rule 2

```text
SCPs apply to Member Accounts
```

---

### Rule 3

```text
Management Account is exempt
```

Very important exam trap.

---

### Rule 4

```text
Member Account Root Users ARE affected
```

---

### Rule 5

```text
Explicit Deny cannot be overridden
```

---

# Shared Responsibility Model

## EC2

### AWS Responsibilities

- Physical servers
- Networking
- Hypervisor

### Customer Responsibilities

- Operating system patching
- Applications
- Data
- IAM
- Security Groups

---

## RDS

### AWS Responsibilities

- Operating system
- Database engine patching

### Customer Responsibilities

- Data
- Encryption
- Access controls

---

## S3

### AWS Responsibilities

- Storage durability
- Infrastructure

### Customer Responsibilities

- Bucket policies
- Encryption
- Public access settings

---

# PM Session: SQL Window Functions

## Topics Covered

- OVER Clause
- PARTITION BY
- Window Frames
- ROW_NUMBER
- RANK
- DENSE_RANK
- LAG
- LEAD
- Running Totals
- Ranking Functions

---

# Window Functions

Window functions perform calculations across related rows without collapsing results.

Unlike:

```sql
GROUP BY
```

Window functions still return every row.

---

# Anatomy of a Window Function

```sql
SUM(amount) OVER (
    PARTITION BY customer_id
    ORDER BY transaction_date
)
```

## Components

### PARTITION BY

Groups rows into windows.

---

### ORDER BY

Defines order inside each window.

---

### Frame

Determines which rows are included in the calculation.

Example:

```sql
ROWS BETWEEN UNBOUNDED PRECEDING
AND CURRENT ROW
```

---

# Ranking Functions

## ROW_NUMBER()

Every row receives a unique number.

Example:

```text
1000 → 1
900  → 2
900  → 3
```

---

## RANK()

Ties share rank.

Gaps exist.

Example:

```text
1000 → 1
900  → 2
900  → 2
800  → 4
```

---

## DENSE_RANK()

Ties share rank.

No gaps.

Example:

```text
1000 → 1
900  → 2
900  → 2
800  → 3
```

---

# Running Totals

Example:

```sql
SUM(amount) OVER (
    PARTITION BY branch_code
    ORDER BY transaction_date
)
```

Use cases:

- Fraud monitoring
- Revenue tracking
- Account balances

---

# LAG()

Reads previous row values.

Example:

```sql
LAG(total_amount)
OVER (
    PARTITION BY branch_code
    ORDER BY month_start
)
```

Use cases:

- Month-over-month comparison
- Change detection
- Trend analysis

---

# LEAD()

Reads future row values.

Example:

```sql
LEAD(total_amount)
OVER (
    PARTITION BY branch_code
    ORDER BY month_start
)
```

Use cases:

- Forecasting
- Future comparisons

---

# Key Window Function Rule

Window functions cannot be used directly inside:

```sql
WHERE
```

Correct approach:

```sql
WITH ranked_data AS (
   ...
)
SELECT *
FROM ranked_data
WHERE rank <= 3;
```

---

# Knowledge Check Answers

### Policy Evaluation

✅ **Answer: B**

```text
Service Control Policies (SCPs)
```

---

### Permission Boundaries

✅ **Answer: B**

```text
S3:* and EC2:* only
```

---

### Shared Responsibility

✅ **Answer: B**

```text
AWS patches RDS database engines
```

---

# Reflection

Today's IAM session helped me understand how enterprise-scale AWS environments securely manage user access without creating thousands of IAM users. The concepts of Permission Boundaries, STS temporary credentials, SCPs, and IAM Identity Center are essential for building secure multi-account AWS architectures.

The SQL session introduced powerful analytical tools such as DENSE_RANK(), LAG(), and running totals. Window functions allow detailed row-level analysis while still providing summary information, making them significantly more flexible than traditional GROUP BY queries in reporting and analytics scenarios.

## Exam Signals to Remember

```text
Corporate Employees → IAM Identity Center + SAML

Google/Facebook Login → Cognito + Web Identity Federation

Developer Privilege Escalation → Permission Boundaries

Cross-Account Access → AssumeRole

Temporary Credentials → Access Key + Secret Key + Session Token

Management Account → Not affected by SCPs

Explicit Deny → Always Wins

TCP + Static IP → NLB

Path-Based Routing → ALB

Firewall Inspection → GWLB
```