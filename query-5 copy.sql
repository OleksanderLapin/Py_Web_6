SELECT s.name as Subject, t.fullname as Teacher_name 
FROM subjects s
JOIN teachers t  ON t.id = s.teacher_id
WHERE teacher_id = <teacher_id>;