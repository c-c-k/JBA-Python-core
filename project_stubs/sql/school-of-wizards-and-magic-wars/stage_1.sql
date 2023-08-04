/*
table names:

    - Achievement
    - Student_Achievement
    - Subject
    - Department
    - Student_Subject
    - Department_Subject
    - Students

stage 1:
   Output: student names is alphabetical order
   Filter: 3'rd years with with 5 points in all their courses
*/
-- best_student = "
SELECT
    name
FROM
    Students
INNER JOIN 
    Student_Subject USING (student_id)
WHERE
    Students.grade = 3
GROUP BY
    student_id
HAVING
    min(result) = 5
ORDER BY
    name
;
-- "
