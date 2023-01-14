/* Jet Brains Academy topic question solution.

Topic category: Computer science -> Fundamentals  -> Databases and  -> SQL  -> Basics  -> SQL  -> Functions and operations
Topic name: Aggregate functions
Question name: Ratings
Question rating: Medium

-=- QUESTION BODY -=-
Question text censored.
-=- QUESTION BODY -=-
*/
-- -=- QUESTION SOLUTION -=-
-- -=- ANSWER CODE START -=-
SELECT
    AVG(users_rating),
    AVG(critics_rating)
FROM
    games
WHERE
    (users_rating >= 8)
    AND (critics_rating >= 8)
;
-- -=- ANSWER CODE END -=-
/* -=- SAMPLE IO -=-

*/
