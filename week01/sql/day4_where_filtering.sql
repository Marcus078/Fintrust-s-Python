-- Find all Gauteng customers for a regional marketing campaign
SELECT customer_id,
       first_name,
       last_name,
       email
FROM customers
WHERE province = 'Gauteng'
      -- Only return customers whose province is Gauteng
ORDER BY last_name;


-- Accounts with balance greater than R10,000
SELECT account_id,
       account_number,
       account_type,
       balance
FROM accounts
WHERE balance > 10000
      -- Return only accounts whose current balance exceeds R10,000
ORDER BY balance DESC;


-- All SAVINGS accounts for the product update rollout
SELECT account_id,
       customer_id,
       account_number,
       balance
FROM accounts
WHERE account_type = 'SAVINGS'
      -- Only include accounts classified as SAVINGS
ORDER BY balance DESC;


-- Transactions above R500 in the Groceries category
SELECT transaction_id,
       account_id,
       amount,
       transaction_type,
       transaction_date
FROM transactions
WHERE merchant_category = 'Groceries'
      -- Restrict results to grocery-related transactions
  AND amount > 500
      -- Only include transactions greater than R500
ORDER BY amount DESC;


-- Customers whose email address contains 'gmail'
SELECT first_name,
       last_name,
       email
FROM customers
WHERE email LIKE '%gmail%'
      -- Match any email address that contains the word 'gmail'
ORDER BY last_name;