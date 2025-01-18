CREATE TABLE IF NOT EXISTS crypto_prices (
    id VARCHAR(50),
    current_price DOUBLE PRECISION,
    market_cap DOUBLE PRECISION,
    price_change_percentage_24h DOUBLE PRECISION,
    timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
