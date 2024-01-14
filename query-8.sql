SELECT t.fullname as Teacher_name, ROUND(AVG(grade), 2) as Average_grade
FROM grades g
JOIN students s ON s.id = g.student_id
JOIN subjects s2 ON s2.id = g.subject_id 
JOIN groups g2 ON g2.id = s.group_id 
JOIN teachers t ON t.id = s2.teacher_id
WHERE t.id = 2;