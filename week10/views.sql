CREATE OR REPLACE VIEW v_customer_accounts AS
SELECT
    c.customer_id,
    c.first_name || ' ' || c.last_name AS full_name,
    c.segment,
    c.region,
    COUNT(a.account_id) AS account_count,
    SUM(a.balance) AS total_balance,
    SUM(
        CASE
            WHEN a.currency = 'ZAR'
            THEN a.balance
            ELSE 0
        END
    ) AS zar_balance,
    MIN(c.onboarded_date) AS onboarded_date
FROM customers c
LEFT JOIN accounts a
    ON c.customer_id =
       a.customer_id
   AND a.status = 'active'
GROUP BY
    c.customer_id,
    c.first_name,
    c.last_name,
    c.segment,
    c.region;

    CREATE OR REPLACE VIEW
v_monthly_txn_summary AS

SELECT
    DATE_TRUNC(
        'month',
        t.txn_date
    ) AS txn_month,

    c.segment,
    t.channel,
    t.txn_type,

    COUNT(*) AS txn_count,

    SUM(t.amount)*        AS total_amount,

    AVG(*.amount)
        AS avg_amount,

 *  MAX(t.amount)
        AS max_amo*nt

FROM transactions t

JOIN acco*nts a
ON t.account_id =
   a.accou*t_id

JOIN customers c
ON a.custom*r_id =
   c.customer_id

GROUP BY
*   DATE_TRUNC(
        'month',
  *     t.txn_date
    ),
    c.segme*t,
    t.channel,
    t.txn_type;
*

CREATE OR REPLACE*VIEW
v_migration_audit AS

SELECT
*   c.customer_id,

    c.first_nam*
      || ' ' ||
    c.last_name
 *    AS full_name,

    a.account_i*,

    ms.source_system,

    ms.v*lidation_state,

    ms.migrated_a*

FROM customers c

JOIN accounts *
ON c.customer_id =
   a.customer_id

JOIN migration_status ms
ON a.account_id =
   ms.asset_id;