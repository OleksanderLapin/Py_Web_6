SELECT s2.name as Subject, s.fullname as Student_name, ROUND(AVG(grade), 2) as Average_grade 
FROM grades g
JOIN students s ON s.id = g.student_id
JOIN subjects s2 ON s2.id = g.subject_id 
WHERE s2.id = <subject_id> 
GROUP BY student_id 
ORDER BY Average_grade DESC 
LIMIT 1;