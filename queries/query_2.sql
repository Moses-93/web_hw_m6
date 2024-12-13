SELECT s.name, AVG(g.grade) AS avg_grade
FROM students s
JOIN grades g ON s.id = g.student_id
JOIN subjects subj ON g.subject_id = subj.id
WHERE subj.name = 'Math'
GROUP BY s.id
ORDER BY avg_grade DESC
LIMIT 1;
