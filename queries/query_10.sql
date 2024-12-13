SELECT subj.name AS course_name
FROM grades gr
JOIN subjects subj ON gr.subject_id = subj.id
JOIN teachers t ON subj.teacher_id = t.id
JOIN students s ON gr.student_id = s.id
WHERE s.name = 'Emily Harrison' -- Ім'я студента
  AND t.name = 'Cynthia Mclean'; -- ім'я викладача
