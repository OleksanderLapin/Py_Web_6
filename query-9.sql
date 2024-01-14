SELECT s.fullname as Student_name, s2.name as Subject
FROM grades g
JOIN students s ON s.id = g.student_id
JOIN subjects s2 ON s2.id = g.subject_id 
WHERE s.id = 3
GROUP BY subject_id;