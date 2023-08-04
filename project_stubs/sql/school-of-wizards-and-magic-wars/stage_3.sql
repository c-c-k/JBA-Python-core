/*
table names:

    - Achievement
    - Student_Achievement
    - Subject
    - Department
    - Student_Subject
    - Department_Subject
    - Students

stage 3:
   Output: student names is alphabetical order + 'best' column.
           'best' column contains 'above average' if average result 
           is above 3.5 and 'below average' otherwise.
*/
-- average_student = "
SELECT
    name,
    CASE
        WHEN avg(result) > 3.5 THEN 'above average' 
        ELSE 'below average' 
    END best
FROM
    Students
INNER JOIN 
    Student_Subject USING (student_id)
GROUP BY
    student_id
ORDER BY
    name
;
-- "
