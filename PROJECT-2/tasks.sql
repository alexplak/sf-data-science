--Юнит 2
SELECT max(age) FROM hh.candidate

SELECT min(age) FROM hh.candidate

SELECT age, count(*) FROM hh.candidate GROUP BY age ORDER BY 1 desc

SELECT count(*) FROM hh.candidate WHERE age > 40 AND age < 100


--Юнит 3
SELECT t2.title AS city, count(*) AS cnt FROM hh.candidate AS t1 LEFT JOIN hh.city AS t2 ON t1.city_id = t2.id GROUP BY t2.title ORDER BY 2 desc

SELECT gender, age, desirable_occupation, t2.title AS city, employment_type FROM hh.candidate AS t1 LEFT JOIN hh.city AS t2 ON t1.city_id = t2.id WHERE t2.title = 'Москва' AND t1.employment_type LIKE '%проектная работа%' ORDER BY t1.id

SELECT gender, age, desirable_occupation, t2.title AS city, employment_type FROM hh.candidate AS t1 LEFT JOIN hh.city AS t2 ON t1.city_id = t2.id WHERE t2.title = 'Москва' AND t1.employment_type LIKE '%проектная работа%' AND (lower(desirable_occupation) LIKE '%разработчик%' OR lower(desirable_occupation) LIKE '%аналитик%' OR lower(desirable_occupation) LIKE '%программист%') ORDER BY t1.id

SELECT t1.id, t2.title AS city FROM hh.candidate AS t1 LEFT JOIN hh.city AS t2 ON t1.city_id = t2.id WHERE current_occupation = desirable_occupation ORDER BY 2, 1

SELECT count(*) FROM hh.candidate WHERE (gender = 'M' AND age >= 65) OR (gender = 'F' AND age >= 60)


--Юнит 4
SELECT
    gender, age, desirable_occupation, t2.title AS city, employment_type, t4.title AS timetable_type
FROM
    hh.candidate AS t1 LEFT JOIN hh.city AS t2 ON t1.city_id = t2.id LEFT JOIN hh.candidate_timetable_type AS t3 ON t1.id = t3.candidate_id LEFT JOIN hh.timetable_type AS t4 ON t3.timetable_id = t4.id
WHERE
    t2.title in ('Новосибирск', 'Омск', 'Томск', 'Тюмень')
    AND t4.title = 'вахтовый метод'
ORDER BY
    t2.title, t1.id
    
(SELECT
    t1.desirable_occupation, t1.age
FROM
    hh.candidate AS t1 LEFT JOIN hh.city AS t2 ON t1.city_id = t2.id
WHERE
    t2.title = 'Санкт-Петербург' AND t1.age BETWEEN 16 AND 21
ORDER BY age
LIMIT 10)
UNION ALL
SELECT
    'Total', count(*)
FROM
    hh.candidate AS t1 LEFT JOIN hh.city AS t2 ON t1.city_id = t2.id
WHERE
    t2.title = 'Санкт-Петербург' AND t1.age BETWEEN 16 AND 21