SELECT s.fullname as Student_name, t.fullname as Teacher_name, s2.name as Subject
FROM grades g
JOIN students s ON s.id = g.student_id
JOIN subjects s2 ON s2.id = g.subject_id 
JOIN teachers t ON t.id = s2.teacher_id
WHERE s.id = 1 and t.id = 2
GROUP BY subject_id ;