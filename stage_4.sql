/*
table names:

    - Achievement
    - Student_Achievement
    - Subject
    - Department
    - Student_Subject
    - Department_Subject
    - Students

stage 4:
    Output: student names in alphabetical order + department name
    Filter: average result above 4.5
*/
-- best_of_department = "
SELECT
    name,
    avg(result),
    department_name
FROM
    Students
INNER JOIN 
    Student_Subject USING (student_id)
INNER JOIN 
    Department_Subject USING (subject_id)
INNER JOIN 
    Department USING (department_id)
GROUP BY
    student_id
HAVING
    avg(result) > 4.6
ORDER BY
    name
;
-- "
