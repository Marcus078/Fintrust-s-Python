# transaction_flowchart.py
# FinTrust Bank — Automated Transaction Decision Engine

BLOCKED_COUNTRIES = ["KP", "IR", "CU", "SY", "SD"]
DAILY_LIMIT = 50000
ATM_LIMIT = 5000
LARGE_THRESHOLD = 10000
REVIEW_THRESHOLD = 5000


def assess_transaction(tx_id, customer, amount, destination, is_trusted_device):
    """
    Evaluate a FinTrust Bank transaction and return a decision.

    Args:
        tx_id (str): Unique transaction reference
        customer (str): Customer full name
        amount (float): Transaction amount in ZAR
        destination (str): ISO 3166-1 alpha-2 country code
        is_trusted_device (bool): True if device is registered

    Returns:
        dict
    """

    # 1. Blocked destination check (highest priority)
    if destination in BLOCKED_COUNTRIES:
        return {
            "tx_id": tx_id,
            "customer": customer,
            "status": "BLOCKED",
            "reason": f"Transfer to {destination} is not permitted"
        }

    # 2. Daily transaction limit
    if amount > DAILY_LIMIT:
        return {
            "tx_id": tx_id,
            "customer": customer,
            "status": "BLOCKED",
            "reason": f"Amount exceeds daily limit of R{DAILY_LIMIT:,}"
        }

    # 3. Invalid amount check
    if amount <= 0:
        return {
            "tx_id": tx_id,
            "customer": customer,
            "status": "BLOCKED",
            "reason": "Invalid transaction amount"
        }

    # 4. Large transaction handling
    if amount > LARGE_THRESHOLD:
        if is_trusted_device:
            return {
                "tx_id": tx_id,
                "customer": customer,
                "status": "PENDING",
                "reason": "Large transfer — OTP verification required"
            }
        else:
            return {
                "tx_id": tx_id,
                "customer": customer,
                "status": "REVIEW",
                "reason": "Large transfer from unrecognised device"
            }

    # 5. Medium-risk transaction
    if amount > REVIEW_THRESHOLD and not is_trusted_device:
        return {
            "tx_id": tx_id,
            "customer": customer,
            "status": "REVIEW",
            "reason": "Moderate amount from unrecognised device"
        }

    # 6. Default approval
    return {
        "tx_id": tx_id,
        "customer": customer,
        "status": "APPROVED",
        "reason": "All checks passed"
    }


# --- Test Cases ---
test_cases = [
    # (tx_id, customer, amount, destination, is_trusted_device)
    ("TX001", "Thabo Nkosi", 500.00, "ZA", True),
    ("TX002", "Amahle Dlamini", 15000.00, "ZA", True),
    ("TX003", "Sipho Mokoena", 8000.00, "ZA", False),
    ("TX004", "Lerato Sithole", 200.00, "IR", True),
    ("TX005", "Nomvula Dube", 75000.00, "ZA", True),
]

print("=" * 65)
print(f"{'TX ID':<8} {'Customer':<18} {'Status':<10} Reason")
print("=" * 65)

for tc in test_cases:
    result = assess_transaction(*tc)

    print(
        f"{result['tx_id']:<8} "
        f"{result['customer']:<18} "
        f"{result['status']:<10} "
        f"{result['reason']}"
    )