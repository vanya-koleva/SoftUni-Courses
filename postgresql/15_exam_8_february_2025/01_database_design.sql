CREATE TABLE brands(
    id SERIAL PRIMARY KEY,
    name varchar(50) NOT NULL UNIQUE
);

CREATE TABLE classifications(
    id SERIAL PRIMARY KEY,
    name varchar(30) NOT NULL UNIQUE
);

CREATE TABLE customers(
    id SERIAL PRIMARY KEY,
    first_name varchar(30) NOT NULL,
    last_name varchar(30) NOT NULL,
    address varchar(150) NOT NULL,
    phone varchar(30) NOT NULL UNIQUE ,
    loyalty_card BOOLEAN NOT NULL DEFAULT FALSE
);

CREATE TABLE items(
    id SERIAL PRIMARY KEY,
    name varchar(50) NOT NULL,
    quantity INT NOT NULL CHECK ( quantity >= 0 ),
    price DECIMAL(12, 2) NOT NULL CHECK ( price > 0.00 ),
    description TEXT,
    brand_id INT REFERENCES brands ON DELETE CASCADE ON UPDATE CASCADE NOT NULL ,
    classification_id INT REFERENCES classifications ON DELETE CASCADE ON UPDATE CASCADE NOT NULL
);

CREATE TABLE orders(
    id SERIAL PRIMARY KEY,
    created_at TIMESTAMP NOT NULL DEFAULT now(),
    customer_id INT REFERENCES customers ON DELETE CASCADE ON UPDATE CASCADE NOT NULL
);

CREATE TABLE reviews(
    customer_id INT REFERENCES customers ON DELETE CASCADE ON UPDATE CASCADE NOT NULL,
    item_id INT REFERENCES items ON DELETE CASCADE ON UPDATE CASCADE  NOT NULL,
    PRIMARY KEY (customer_id, item_id),
    created_at timestamp NOT NULL DEFAULT now(),
    rating DECIMAL(3, 1) NOT NULL DEFAULT 0.0 CHECK ( rating <= 10.0 )
);

CREATE TABLE orders_items(
    order_id INT REFERENCES orders ON DELETE CASCADE ON UPDATE CASCADE NOT NULL,
    item_id INT REFERENCES items ON DELETE CASCADE ON UPDATE CASCADE NOT NULL,
    PRIMARY KEY (order_id, item_id),
    quantity INT NOT NULL CHECK ( quantity >= 0 )
);
