from decimal import Decimal
import math


# Exercise 1
# Account Formatter

def format_account_summary(customer_name, account_type, balance):
    """
    Returns a formatted account summary.
    """
    d_balance = Decimal(str(balance))

    return (
        f"Customer: {customer_name.title()}\n"
        f"Account:  {account_type.upper()}\n"
        f"Balance:  R {d_balance:,.2f}\n"
        f"Status:   ACTIVE"
    )


# Test Exercise 1
print("=== Exercise 1 ===")
print(
    format_account_summary(
        "thabo nkosi",
        "savings",
        "52750.00"
    )
)
print()


# Exercise 2
# Compound Interest Calculator
# Formula:
# A = P(1 + r/n)^(nt)

def calculate_compound_interest(principal, annual_rate, years, n=12):
    """
    principal: initial amount (Decimal)
    annual_rate: annual interest rate as decimal
                 e.g. 0.085 = 8.5%
    years: investment period
    n: compounds per year
    """

    p = float(principal)

    amount = p * (1 + annual_rate / n) ** (n * years)
    interest_earned = amount - p

    return (
        Decimal(str(round(amount, 2))),
        Decimal(str(round(interest_earned, 2)))
    )


# Test Exercise 2
print("=== Exercise 2 ===")

principal = Decimal("50000.00")

amount, interest = calculate_compound_interest(
    principal,
    0.085,
    3
)

print(f"Principal:       R {principal:,.2f}")
print(f"Final Amount:    R {amount:,.2f}")
print(f"Interest Earned: R {interest:,.2f}")
print()


# Exercise 3
# Transaction Statistics
# Find:
# - Total
# - Average
# - Largest
# - Smallest
# - Count above R5000

transactions = [
    Decimal("250.00"),
    Decimal("12500.00"),
    Decimal("750.50"),
    Decimal("88000.00"),
    Decimal("1200.00"),
    Decimal("3450.00"),
    Decimal("55000.00"),
    Decimal("125.00"),
    Decimal("9800.00")
]

total = sum(transactions)
average = total / len(transactions)
largest = max(transactions)
smallest = min(transactions)

count_above_5000 = 0

for transaction in transactions:
    if transaction > Decimal("5000"):
        count_above_5000 += 1

print("=== Exercise 3 ===")
print(f"Total:             R {total:,.2f}")
print(f"Average:           R {average:,.2f}")
print(f"Largest:           R {largest:,.2f}")
print(f"Smallest:          R {smallest:,.2f}")
print(f"Above R5,000:      {count_above_5000}")