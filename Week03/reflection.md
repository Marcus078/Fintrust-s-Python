# Week 3 Reflection

## 1. Storage Service Choice

For FinTrust's compliance archive with a 5-year POPIA retention requirement, I would use an Amazon S3 bucket with Versioning enabled, SSE-KMS encryption, and Object Lock in Compliance mode. Compliance mode ensures that no user, including the root account, can modify or delete records before the retention period expires. I would apply a lifecycle policy that transitions older records to S3 Glacier Flexible Retrieval because compliance data is rarely accessed but must be retrievable within hours for audits. SSE-KMS also provides CloudTrail audit logs showing who accessed encryption keys, which supports regulatory requirements.

## 2. Most Challenging Python Concept

The hardest Python concept this week was working with modules and separating code into reusable functions. At first I found it confusing to decide which logic belonged in `fintrust_utils.py` and which logic belonged in the main script. I got past it by testing each function individually and reviewing the examples that showed how to import specific functions from a module. Once I understood imports and function reuse, the code became easier to maintain and test.

## 3. Real-Project Application

If I started a cloud project tomorrow, I would first apply structured S3 storage design with lifecycle policies and proper encryption. The FinTrust scenario showed how storage requirements, compliance rules, and access patterns affect architectural decisions. I would use versioning, SSE-KMS encryption, and lifecycle transitions from Standard storage to Glacier tiers to reduce costs while maintaining security and compliance. These practices are directly applicable to real-world cloud environments and align with AWS best practices.