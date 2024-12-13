SELECT DISTINCT subj.name AS course_name
FROM grades gr
JOIN subjects subj ON gr.subject_id = subj.id
JOIN students s ON gr.student_id = s.id
WHERE s.name = 'Chelsea Carpenter';
