-- Create the Assets table
CREATE TABLE IF NOT EXISTS assets (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    name VARCHAR(255),
    type VARCHAR(255),
    quantity NUMERIC,
    value NUMERIC,
    purchase_on DATE,
    created_on DATE DEFAULT CURRENT_DATE
);

-- Create the Transactions table
CREATE TABLE IF NOT EXISTS transactions (
    ID INTEGER PRIMARY KEY AUTOINCREMENT,
    user_id INTEGER,
    asset_id INTEGER,
    type VARCHAR(255), 
    quantity NUMERIC,
    created_on DATE DEFAULT CURRENT_DATE,
    updated_on DATE,
    price NUMERIC 
);

-- Insert example record into the Assets table
INSERT INTO assets (user_id, name, type, quantity, value, purchase_on)
VALUES (1, 'AAPL', 'stock', 100, 150.25, '2023-09-15');

-- Insert example record into the Transactions table
INSERT INTO transactions (user_id, asset_id, type, quantity, price)
VALUES (1, 1, 'buy', 50, 150.25);
