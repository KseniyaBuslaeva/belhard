"""заказы которые имеют статус ordered"""
SELECT o.id
FROM orders o
JOIN statuses s ON(o.status_id = s.id )
WHERE s."name" = 'ordered';