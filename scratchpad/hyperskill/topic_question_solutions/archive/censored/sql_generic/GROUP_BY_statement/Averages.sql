/* Jet Brains Academy topic question solution.

Topic category: Computer science -> Fundamentals  -> Databases and  -> SQL  -> Basics  -> SQL  -> Retrieving  -> Data
Topic name: GROUP BY statement
Question name: Averages
Question rating: Hard

-=- QUESTION BODY -=-
Question text censored.
-=- QUESTION BODY -=-
*/
-- -=- QUESTION SOLUTION -=-
-- -=- ANSWER CODE START -=-
SELECT
    release_year,
    AVG(budget),
    AVG(box_office)
FROM
    movies
GROUP BY
    release_year
ORDER BY
    release_year
;
-- -=- ANSWER CODE END -=-
/* -=- SAMPLE IO -=-

*/
