/* 
   Exercise 1
   Count transactions per customer

   Show each customer's name, province, total number of
   transactions, and total transaction amount.

   INNER JOINs are used because only customers with
   matching accounts and transactions should be included.
   */

SELECT
    c.first_name,
    c.last_name,
    c.province,
    COUNT(t.transaction_id) AS total_transactions,
    SUM(t.amount) AS total_transaction_amount
FROM customers c
INNER JOIN accounts a
    ON c.customer_id = a.customer_id
INNER JOIN transactions t
    ON a.account_id = t.account_id
GROUP BY
    c.customer_id,
    c.first_name,
    c.last_name,
    c.province
ORDER BY total_transaction_amount DESC;


/*
   Exercise 2
   Average balance by account type

   Show each account type, number of accounts, and
   average balance.

   No JOIN is required because all required data exists
   in the accounts table.
  */

SELECT
    account_type,
    COUNT(account_id) AS number_of_accounts,
    AVG(balance) AS average_balance
FROM accounts
GROUP BY account_type
ORDER BY average_balance DESC;


/* 
   Exercise 3
   HAVING filter

   Find provinces where total credit transactions exceed
   R100,000.

   WHERE filters individual transaction rows.
   HAVING filters aggregated province totals.
 */

SELECT
    c.province,
    SUM(t.amount) AS total_deposit_amount,
    COUNT(t.transaction_id) AS credit_transaction_count
FROM customers c
INNER JOIN accounts a
    ON c.customer_id = a.customer_id
INNER JOIN transactions t
    ON a.account_id = t.account_id
WHERE t.transaction_type = 'credit'
GROUP BY c.province
HAVING SUM(t.amount) > 100000
ORDER BY total_deposit_amount DESC;


/* 
   Exercise 4
   Monthly summary

   Show total transaction count and amount per month.

   YEAR() and MONTH() are used to group transactions into
   monthly reporting periods.
*/

SELECT
    YEAR(transaction_date) AS transaction_year,
    MONTH(transaction_date) AS transaction_month,
    COUNT(transaction_id) AS transaction_count,
    SUM(amount) AS total_transaction_amount
FROM transactions
GROUP BY
    YEAR(transaction_date),
    MONTH(transaction_date)
ORDER BY
    transaction_year,
    transaction_month;


/* ==========================================================
   Exercise 5
   Fraud signal
   Find customers who made more than 3 debit transactions on the same day.
   */

SELECT
    CONCAT(c.first_name, ' ', c.last_name) AS customer_name,
    DATE(t.transaction_date) AS transaction_date,
    COUNT(t.transaction_id) AS debit_count
FROM customers c
INNER JOIN accounts a
    ON c.customer_id = a.customer_id
INNER JOIN transactions t
    ON a.account_id = t.account_id
WHERE t.transaction_type = 'debit'
GROUP BY
    c.customer_id,
    c.first_name,
    c.last_name,
    DATE(t.transaction_date)
HAVING COUNT(t.transaction_id) > 3
ORDER BY
    debit_count DESC,
    transaction_date;