CREATE TABLE IF NOT EXISTS orders_items(
id SERIAL PRIMARY KEY,
order_id INTEGER NOT NULL,
product_id INTEGER NOT NULL,
FOREIGN KEY (order_id) REFERENCES orders(id) ON UPDATE CASCADE ON DELETE RESTRICT,
FOREIGN KEY (product_id) REFERENCES products(id) ON UPDATE CASCADE ON DELETE RESTRICT
);