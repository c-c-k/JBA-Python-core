/* Jet Brains Academy topic question solution.

Topic category: Computer science -> Fundamentals  -> Databases and  -> SQL  -> Basics  -> SQL  -> Subqueries
Topic name: Subqueries
Question name: The oldest one
Question rating: Medium

-=- QUESTION BODY -=-
Question text censored.
-=- QUESTION BODY -=-
*/
-- -=- QUESTION SOLUTION -=-
-- -=- ANSWER CODE START -=-
SELECT *
FROM persons
WHERE age = (
    SELECT MAX(age)
    FROM persons
    )
;
-- -=- ANSWER CODE END -=-
/* -=- SAMPLE IO -=-

*/
