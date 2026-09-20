WITH recent_activity AS (

    SELECT
        account_id,
        COUNT(*) AS txn_count_30d,
        SUM(amount) AS total_30d
    FROM transactions
    WHERE transaction_date >= CURRENT_DATE - INTERVAL '30 days'
    GROUP BY account_id

),

avg_velocity AS (

    SELECT
        AVG(txn_count_30d) AS avg_count,
        STDDEV(txn_count_30d) AS stddev_count
    FROM recent_activity

),

flagged_accounts AS (

    SELECT
        r.account_id,
        r.txn_count_30d,
        r.total_30d
    FROM recent_activity r
    CROSS JOIN avg_velocity a
    WHERE r.txn_count_30d >
          a.avg_count + (2 * a.stddev_count)

)

SELECT
    account_id,
    txn_count_30d,
    total_30d
FROM flagged_accounts
ORDER BY txn_count_30d DESC;