# Week 11 Reflection

## Reflection 1

The most difficult distinction was Reliability versus Performance Efficiency.

Both pillars often use Auto Scaling, but the deciding factor is the problem being solved.

If Auto Scaling is replacing failed instances or improving availability, it belongs to Reliability.

If Auto Scaling is handling traffic spikes or maintaining response times, it belongs to Performance Efficiency.

My exam rule is:

Failure = Reliability

Slow = Performance Efficiency

---

## Reflection 2

Before this week I could not confidently write queries that calculated running totals, rankings, or month-over-month growth.

I can now use:

- ROW_NUMBER()
- DENSE_RANK()
- LAG()
- PARTITION BY
- CTE chains

The hardest part was combining window functions and CTEs into a single solution.

---

## Reflection 3

In previous AWS exercises I performed API calls sequentially.

Using a retry decorator would improve resilience against transient API failures.

Using ThreadPoolExecutor would improve performance when retrieving metadata from multiple S3 objects.

Combining retries with concurrency would make the data pipeline more reliable and significantly faster.