SELECT  g2.name as Group_name, s2.name as Subject_name,s.fullname as Student_name, g.grade as Grade 
FROM grades g
JOIN students s ON s.id = g.student_id
JOIN subjects s2 ON s2.id = g.subject_id 
JOIN groups g2 ON g2.id = s.group_id 
WHERE s2.id = 1 and g2.id = 1;