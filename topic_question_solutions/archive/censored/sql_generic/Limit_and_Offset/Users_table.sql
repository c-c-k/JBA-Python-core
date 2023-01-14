/* Jet Brains Academy topic question solution.

Topic category: Computer science -> Fundamentals  -> Databases and  -> SQL  -> Basics  -> SQL  -> Retrieving  -> Data
Topic name: Limit and Offset
Question name: Users table
Question rating: Medium

-=- QUESTION BODY -=-
Question text censored.
-=- QUESTION BODY -=-
*/
-- -=- QUESTION SOLUTION -=-
-- -=- ANSWER CODE START -=-
SELECT name, registered_at
FROM users
ORDER BY registered_at DESC
LIMIT 5
;
-- -=- ANSWER CODE END -=-
/* -=- SAMPLE IO -=-

*/
