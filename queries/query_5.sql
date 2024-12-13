SELECT subj.name AS course_name
FROM subjects subj
JOIN teachers t ON subj.teacher_id = t.id
WHERE t.name = 'Gabrielle Lewis';
