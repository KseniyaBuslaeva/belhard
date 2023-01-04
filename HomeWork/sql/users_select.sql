"""пользователи которые делали заказы"""
SELECT DISTINCT name, email
FROM users u
JOIN orders o ON(u.id = o.user_id );