/* 1. Проанализировать запросы, которые выполнялись на занятии, определить возможные корректировки и/или улучшения (JOIN пока не применять). 
Пока сложно что-то сказать, особено что-либо улучшить в запросах, т.к. только начинаю вникать в тему.*/
/* 2. Пусть задан некоторый пользователь. 
Из всех друзей этого пользователя найдите человека, который больше всех общался с нашим пользователем. */

-- Не совсем уверенна в корректности написания данного запроса.
-- Через INSERT написала пару сообщений от user_id = 1 r user_id = 17
INSERT INTO messages (from_user_id, to_user_id, body, status_id)
VALUES (17, 1, 'text2', 1);


SELECT *
FROM 
	profiles
WHERE user_id IN (
	SELECT DISTINCT
		from_user_id
	FROM
		messages 
	WHERE 
	to_user_id IN ( 
		SELECT to_user_id FROM messages WHERE to_user_id = 1
		UNION
		SELECT to_user_id FROM messages WHERE to_user_id = 1
	)
);

-- На выходе получила пользователя с id '17'. Отдельно прогнала просто запрос с UNION и получила того же пользователя (17):
SELECT * FROM messages WHERE to_user_id = 1
UNION
SELECT * FROM messages WHERE to_user_id = 1;

-- Еще вот так проверила
SELECT 
	from_user_id, to_user_id 
FROM 
	messages
ORDER BY 
	to_user_id;

3. Подсчитать общее количество лайков, которые получили 10 самых молодых пользователей.

--Нашла 10 самых молодых пользователей
SELECT
	user_id, birthday 
FROM 
	profiles
ORDER BY 
	birthday DESC
LIMIT 10;

-- HAVING, ODER BY, LIMIT

--Пока дальше не получается обернуть запрос


4. Определить кто больше поставил лайков (всего) - мужчины или женщины?
5. Найти 10 пользователей, которые проявляют наименьшую активность в использовании социальной сети.
