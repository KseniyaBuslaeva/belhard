"""выбрать продукты которые не были заказаны и отсортировать по title"""
SELECT title, description
FROM products
WHERE products.id NOT IN (SELECT DISTINCT orders_items.product_id FROM orders_items)
ORDER BY title ASC