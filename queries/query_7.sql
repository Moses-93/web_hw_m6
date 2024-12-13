SELECT s.name AS student_name, gr.grade
FROM students s
JOIN grades gr ON s.id = gr.student_id
JOIN groups g ON s.group_id = g.id
JOIN subjects subj ON gr.subject_id = subj.id
WHERE g.name = 'Group A'
  AND subj.name = 'Math';
