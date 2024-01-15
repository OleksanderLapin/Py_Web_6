SELECT g2.name as Group_name, s2.name as Subject,  ROUND(AVG(grade), 2) as Average_grade 
FROM grades g
JOIN students s ON s.id = g.student_id
JOIN subjects s2 ON s2.id = g.subject_id 
JOIN groups g2 ON g2.id = s.group_id 
WHERE s2.id = <subject_id> 
GROUP BY group_id 
ORDER BY Average_grade DESC;