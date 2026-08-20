# FinTrust IAM Architecture

## Overview

FinTrust uses AWS Identity and Access Management (IAM) services to securely manage access for employees, customers, and technical teams. The architecture follows AWS best practices by eliminating long-term credentials wherever possible and relying on temporary credentials through AWS Security Token Service (STS).

---

## Employee Console Access (300 Employees)

FinTrust has approximately 300 employees who require access to AWS accounts for development, operations, reporting, and administration.

Rather than creating individual IAM users for every employee, FinTrust uses **IAM Identity Center** integrated with the company's **Active Directory (AD)** environment.

### Employee Access Flow

```text
Employee
    ↓
Active Directory
    ↓
IAM Identity Center
    ↓
Permission Set
    ↓
STS Temporary Credentials
    ↓
AWS Management Console
```

### Benefits

- Single Sign-On (SSO) experience
- Employees use existing AD credentials
- No IAM users required in AWS accounts
- Centralized access management
- Easier onboarding and offboarding
- Temporary credentials improve security

Permission Sets determine which AWS accounts and services each employee can access. For example, developers may receive access only to development accounts, while administrators receive broader permissions within the limits defined by organizational controls.

---

## Customer Access (100,000 Banking Customers)

FinTrust's mobile and web applications serve more than 100,000 customers. Creating IAM users for every customer would be impractical and difficult to manage.

Instead, FinTrust uses **Amazon Cognito**.

### Customer Access Flow

```text
Customer
    ↓
Cognito User Pool
(Authentication)
    ↓
JWT Token
    ↓
Cognito Identity Pool
(Authorization)
    ↓
STS AssumeRoleWithWebIdentity
    ↓
Temporary AWS Credentials
    ↓
S3 Access
```

### How It Works

1. The customer authenticates through the FinTrust application.
2. Cognito User Pool verifies identity.
3. Cognito generates a JWT token.
4. The Identity Pool exchanges the token for temporary AWS credentials.
5. STS issues temporary credentials.
6. The customer is granted access only to their own S3 objects.

### Benefits

- Scales to hundreds of thousands of users
- No IAM user creation required
- Temporary credentials automatically expire
- Fine-grained access control
- Secure access to AWS services

Each customer can only access their own documents, statements, and uploaded files stored in S3.

---

## DevOps Team Protection Using Permission Boundaries

FinTrust allows its DevOps team to create roles for services such as:

- Lambda
- ECS
- EC2
- CloudWatch
- Systems Manager

However, allowing unrestricted IAM permissions creates the risk of **privilege escalation**.

### Example Risk

A developer with:

```text
IAM:CreateRole
IAM:AttachRolePolicy
```

could create a role with:

```text
AdministratorAccess
```

and gain full administrative control of the AWS environment.

### Solution: Permission Boundaries

FinTrust attaches Permission Boundaries to all DevOps roles.

### Example

Identity Policy:

```text
EC2:*
S3:*
CloudWatch:*
IAM:CreateRole
```

Permission Boundary:

```text
EC2:*
S3:*
CloudWatch:*
```

Effective Permissions:

```text
EC2:*
S3:*
CloudWatch:*
```

Blocked:

```text
IAM:CreateRole
```

Permission Boundaries act as a maximum permission ceiling and prevent developers from granting themselves elevated privileges.

### Benefits

- Prevents privilege escalation
- Supports self-service role creation
- Improves security governance
- Maintains least-privilege access

---

## IAM Policy Evaluation Chain

When AWS evaluates a request, multiple policy layers are checked.

### Evaluation Order

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

If any policy layer contains an explicit deny, access is refused regardless of any allow statements elsewhere.

### Example

```text
Identity Policy = Allow S3:DeleteObject

Permission Boundary = Allow S3:*

Resource Policy = Allow

SCP = Deny S3:DeleteObject
```

Result:

```text
Access Denied
```

The SCP deny overrides all other permissions.

---

## Conclusion

FinTrust uses IAM Identity Center with Active Directory to provide secure console access for employees, Amazon Cognito with Identity Pools to securely manage access for over 100,000 customers, and Permission Boundaries to prevent privilege escalation within the DevOps team. Together with SCPs, STS temporary credentials, and AWS policy evaluation controls, this architecture delivers a scalable, secure, and enterprise-ready access management solution.