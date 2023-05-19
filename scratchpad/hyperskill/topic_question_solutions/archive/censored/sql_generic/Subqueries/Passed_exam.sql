/* Jet Brains Academy topic question solution.

Topic category: Computer science -> Fundamentals  -> Databases and  -> SQL  -> Basics  -> SQL  -> Subqueries
Topic name: Subqueries
Question name: Passed exam
Question rating: Hard

-=- QUESTION BODY -=-
Question text censored.
-=- QUESTION BODY -=-
*/
-- -=- QUESTION SOLUTION -=-
-- -=- ANSWER CODE START -=-
DELETE FROM students
WHERE id IN (
    SELECT student_id
    FROM exam_results
    WHERE percentage < (
        SELECT AVG(percentage)
        FROM exam_results
        )
    )
;
-- -=- ANSWER CODE END -=-
/* -=- SAMPLE IO -=-

*/
