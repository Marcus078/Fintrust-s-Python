# FinTrust Migration Automation Package

## Overview

The `fintrust_migration` package provides reusable AWS migration automation tools developed during Week 10.

The package supports:

- 6Rs migration classification
- AWS DMS task monitoring
- CDC cutover readiness checks
- AWS DataSync task execution
- Dynamic DataSync bandwidth throttling
- Centralised boto3 session management

---

## Package Structure

```text
fintrust_migration/
│
├── __init__.py
│
├── utils/
│   └── sessions.py
│
├── ec2/
│   └── classifier.py
│
├── rds/
│   └── dms_helpers.py
│
└── s3/
    └── sync_helpers.py
```

---

## Features

### EC2 Migration Classification

Classifies EC2 instances using migration tags:

- migration:strategy
- migration:wave

Supported strategies:

- Rehost
- Replatform
- Refactor
- Repurchase
- Retire
- Retain

Example:

```python
from fintrust_migration import classify_instances

portfolio, untagged = classify_instances()
```

### DMS Monitoring

Monitor replication tasks and determine cutover readiness.

Example:

```python
from fintrust_migration import is_cutover_ready

ready = is_cutover_ready(
    replication_instance_id,
    task_identifier
)
```

### DataSync Automation

Start DataSync task executions and manage bandwidth throttling.

Example:

```python
from fintrust_migration import (
    start_task_execution,
    set_task_throttle
)

execution_arn = start_task_execution(task_arn)

set_task_throttle(
    task_arn,
    500
)
```

---

## Installation

```bash
pip install -r requirements.txt
```

---

## Import Validation

```bash
python -c "from fintrust_migration import classify_instances, is_cutover_ready, start_task_execution, set_task_throttle; print('Package import OK')"
```

Expected output:

```text
Package import OK
```

---

## AWS Services Used

- Amazon EC2
- AWS DMS
- AWS DataSync
- Amazon CloudWatch
- AWS EventBridge Scheduler
- AWS IAM

---

## FinTrust Migration Programme

This package was developed to support:

- Wave 1 Rehost migrations
- Wave 2 database modernisation
- DMS cutover monitoring
- DataSync archive migration
- Migration reporting and automation