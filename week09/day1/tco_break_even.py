def tco_break_even(
        on_prem_annual_cost,
        aws_monthly_cost,
        migration_one_time_cost,
        onprem_inflation_pct=0.03
):

    break_even = None

    for month in range(1, 61):

        year = ((month - 1) // 12)

        annual_cost = (
            on_prem_annual_cost *
            ((1 + onprem_inflation_pct)
             ** year)
        )

        onprem_monthly = (
            annual_cost / 12
        )

        onprem_total = (
            onprem_monthly *
            month
        )

        aws_total = (
            migration_one_time_cost +
            (aws_monthly_cost * month)
        )

        if (
            break_even is None
            and
            aws_total < onprem_total
        ):
            break_even = month

    return break_even


month = tco_break_even(
    on_prem_annual_cost=4200000,
    aws_monthly_cost=248000,
    migration_one_time_cost=850000
)

print(
    f"Break-even month: {month}"
)