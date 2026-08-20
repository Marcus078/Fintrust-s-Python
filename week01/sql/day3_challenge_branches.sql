/*

FinTrust Bank - Branches Challenge Solution


Design Decisions:
1. branch_id is the primary key and auto-increments for uniqueness.
2. branch_name stores the official branch name.
3. province allows province-level reporting and analytics.
4. city provides more detailed location information.
5. created_at automatically records when the branch record was created.
6. branch_id in accounts is nullable because some accounts may be
   opened online and therefore not linked to a physical branch.
7. A foreign key ensures referential integrity between accounts
   and branches.
*/

-- Create Branches table
CREATE TABLE IF NOT EXISTS branches (
    branch_id INT PRIMARY KEY AUTO_INCREMENT,
    branch_name VARCHAR(150) NOT NULL,
    province VARCHAR(50) NOT NULL,
    city VARCHAR(100) NOT NULL,
    created_at DATETIME DEFAULT CURRENT_TIMESTAMP
);

-- Add branch_id column to accounts table
ALTER TABLE accounts
ADD COLUMN branch_id INT NULL,
ADD CONSTRAINT fk_accounts_branches
    FOREIGN KEY (branch_id)
    REFERENCES branches(branch_id);

-- Insert sample branches
INSERT INTO branches
    (branch_name, province, city)
VALUES
    ('Sandton City Branch', 'Gauteng', 'Johannesburg'),
    ('Cape Town CBD Branch', 'Western Cape', 'Cape Town'),
    ('Gateway Branch', 'KwaZulu-Natal', 'Durban');

-- Update two existing accounts to reference branches
UPDATE accounts
SET branch_id = 1
WHERE account_id = 1;

UPDATE accounts
SET branch_id = 2
WHERE account_id = 6;

-- Verify results
SELECT
    a.account_id,
    a.account_number,
    a.account_type,
    b.branch_name,
    b.city,
    b.province
FROM accounts a
LEFT JOIN branches b
    ON a.branch_id = b.branch_id;