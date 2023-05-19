/* Jet Brains Academy topic question solution.

Topic category: Computer science -> Fundamentals  -> Databases and  -> SQL  -> Basics  -> SQL  -> Retrieving  -> Data
Topic name: GROUP BY statement
Question name: Racing
Question rating: Hard

-=- QUESTION BODY -=-
Question text censored.
-=- QUESTION BODY -=-
*/
-- -=- QUESTION SOLUTION -=-
-- -=- ANSWER CODE START -=-
SELECT
    racer_id,
    segment_id,
    MIN(time)
FROM
    racing
GROUP BY
    racer_id,
    segment_id
ORDER BY
    MIN(time)
;
-- -=- ANSWER CODE END -=-
/* -=- SAMPLE IO -=-

*/
