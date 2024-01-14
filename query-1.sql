SELECT s.fullname as Student_name, ROUND(AVG(grade), 2) as Average_grade 
FROM grades g 
LEFT JOIN students s ON s.id = g.student_id 
GROUP BY student_id 
ORDER BY average_grade DESC 
LIMIT 5;