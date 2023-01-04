"""статусы которые не фигурируют в заказах"""
SELECT name
FROM statuses
WHERE id NOT IN (SELECT DISTINCT status_id FROM orders);