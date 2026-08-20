# FinTrust Transaction Decision Engine

## What Did I Build?

I built a Python-based Transaction Decision Engine for FinTrust Bank. The application evaluates transactions based on predefined business and fraud detection rules, such as blocked destination countries, transaction limits, transfer amounts, and trusted device status.

The system returns one of four outcomes:

- APPROVED
- PENDING
- REVIEW
- BLOCKED

Each decision includes a clear reason to support auditing and compliance requirements.

---

## What Does It Demonstrate?

This project demonstrates:

- Python functions
- Conditional statements (`if`, `elif`, `else`)
- Boolean logic (`and`, `or`, `not`)
- Membership testing using the `in` operator
- Return values and dictionaries
- Fraud detection decision logic
- Clean and readable code structure
- Real-world banking transaction processing concepts

The solution follows a stateless design pattern similar to logic that could be used in an AWS Lambda function.

---

## How Do I Run It?

### Prerequisites

- Python 3.12 or later
- VS Code (recommended)

### Run the Application

Navigate to the project folder:

```bash
cd week02/python