/
   Challenge 1
   Find all customers who have a cheque account with a
   balance below R1,000.

   INNER JOIN is used because we only want customers who
   actually have matching account records.
   */

SELECT
    c.first_name,
    c.last_name,
    c.province,
    a.balance
FROM customers c
INNER JOIN accounts a
    ON c.customer_id = a.customer_id
WHERE a.account_type = 'cheque'
  AND a.balance < 1000
ORDER BY a.balance ASC;


/''
   Challenge 2
   List all transactions made by customers from Western Cape.

   INNER JOIN is used between all three tables because we
   only want rows where a customer has an account and that
   account has recorded transactions. */

SELECT
    CONCAT(c.first_name, ' ', c.last_name) AS customer_name,
    t.amount,
    t.transaction_type,
    t.transaction_date
FROM customers c
INNER JOIN accounts a
    ON c.customer_id = a.customer_id
INNER JOIN transactions t
    ON a.account_id = t.account_id
WHERE c.province = 'Western Cape'
ORDER BY t.transaction_date DESC;


/*
   Challenge 3
   Find all accounts that have no transactions recorded.

   LEFT JOIN is used from accounts to transactions so that
   all accounts are returned, including those without a
   matching transaction. Accounts with no transactions
   will have NULL values in the transactions table.
 */

SELECT
    a.account_id,
    a.account_type,
    a.balance,
    CONCAT(c.first_name, ' ', c.last_name) AS customer_name
FROM accounts a
INNER JOIN customers c
    ON a.customer_id = c.customer_id
LEFT JOIN transactions t
    ON a.account_id = t.account_id
WHERE t.transaction_id IS NULL
ORDER BY a.account_id;