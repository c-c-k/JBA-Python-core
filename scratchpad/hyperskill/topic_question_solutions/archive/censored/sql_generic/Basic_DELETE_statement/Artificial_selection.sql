/* Jet Brains Academy topic question solution.

Topic category: Computer science -> Fundamentals  -> Databases and  -> SQL  -> Basics  -> SQL  -> Data  -> Modification  -> Language
Topic name: Basic DELETE statement
Question name: Artificial selection
Question rating: Medium

-=- QUESTION BODY -=-
Question text censored.
-=- QUESTION BODY -=-
*/
-- -=- QUESTION SOLUTION -=-
-- -=- ANSWER CODE START -=-
DELETE FROM movies
WHERE
    (year >= 1980)
    AND (rating < 8.5)
;
-- -=- ANSWER CODE END -=-
/* -=- SAMPLE IO -=-

*/
