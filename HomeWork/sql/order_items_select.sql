"""заказанные товары из категории mobile phones"""
SELECT oi.id
FROM orders_items oi
JOIN products p ON (p.id = oi.product_id)
JOIN categories c ON (p.category_id = c.id)
WHERE c.name = 'mobile phones';