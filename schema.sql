CREATE DATABASE order_book;
USE order_book;

CREATE TABLE orders (
    id integer PRIMARY KEY AUTO_INCREMENT,
    symbol VARCHAR(255) NOT NULL,
    epoch BIGINT NOT NULL,
    b4q integer,
    b4p REAL,
    b3q integer,
    b3p REAL,
    b2q integer,
    b2p REAL,
    b1q integer,
    b1p REAL,
    b0q integer,
    b0p REAL,
    a0q integer,
    a0p REAL,
    a1q integer,
    a1p REAL,
    a2q integer,
    a2p REAL,
    a3q integer,
    a3p REAL,
    a4q integer,
    a4p REAL,
    trade_price REAL,
    trade_quantity integer
);

-- INSERT INTO orders (symbol, epoch, b4q, b4p, b3q, b3p, b2q, b2p, b1q, b1p, b0q, b0p, a0q, a0p, a1q, a1p, a2q, a2p, a3q, a3p, a4q, a4p, trade_price, trade_quantity) 
-- VALUES
-- ("VOO", 1609722840030034727, 53, 476.18, 2, 476.19, 6, 476.2, 1, 476.21, 2, 476.22, 1, 476.27, 1, 476.28, 4, 476.29, 3, 476.33, 1, 476.34, NULL, NULL);

