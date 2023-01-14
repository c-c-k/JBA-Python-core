/* Jet Brains Academy topic question solution.

Topic category: Computer science -> Fundamentals  -> Databases and  -> SQL  -> Basics  -> SQL  -> Data  -> Modification  -> Language
Topic name: Updating selected rows
Question name: Agents
Question rating: Hard

-=- QUESTION BODY -=-
Question text censored.
-=- QUESTION BODY -=-
*/
-- -=- QUESTION SOLUTION -=-
-- -=- ANSWER CODE START -=-
UPDATE agents
SET
    current_location = 'Istanbul',
    missions = missions + 1
WHERE
    (missions > 10)
    AND (knows_languages > 3)
;
-- -=- ANSWER CODE END -=-
SELECT * FROM agents;
/* -=- SAMPLE IO -=-

*/
