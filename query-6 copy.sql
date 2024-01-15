SELECT g.name as Group_name, s.fullname as Student_name 
FROM students s 
JOIN groups g ON g.id = s.group_id 
WHERE g.id = <group_id>;