/* Jet Brains Academy topic question solution.

Topic category: Computer science -> Fundamentals  -> Databases and  -> SQL  -> Basics  -> SQL  -> Retrieving  -> Data
Topic name: Special WHERE operators
Question name: Big cities students
Question rating: Medium

-=- QUESTION BODY -=-
Question text censored.
-=- QUESTION BODY -=-
*/
-- -=- QUESTION SOLUTION -=-
-- -=- ANSWER CODE START -=-
SELECT
    name
FROM
    students
WHERE
    city IN ("Dublin", "London", "Birmingham")
;
-- -=- ANSWER CODE END -=-
/* -=- SAMPLE IO -=-

*/
