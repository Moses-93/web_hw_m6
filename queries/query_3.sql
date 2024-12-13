SELECT g.name AS group_name, AVG(gr.grade) AS avg_grade
FROM groups g
JOIN students s ON g.id = s.group_id
JOIN grades gr ON s.id = gr.student_id
JOIN subjects subj ON gr.subject_id = subj.id
WHERE subj.name = 'Math'
GROUP BY g.id;
