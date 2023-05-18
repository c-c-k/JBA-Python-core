/*
table names:

    - Achievement
    - Student_Achievement
    - Subject
    - Department
    - Student_Subject
    - Department_Subject
    - Students

stage 2:
   Output: student names and bonus points sorted by descending bonus points
   Filter: top 4 students by bonus points
*/
-- achievement_point = "
SELECT
    name, sum(bonus) as [bonus point]
FROM
    Students
INNER JOIN 
    Student_Achievement USING (student_id)
INNER JOIN 
    Achievement USING (achievement_id)
GROUP BY
    student_id
ORDER BY
    [bonus point] DESC
LIMIT
    4
;
-- "
