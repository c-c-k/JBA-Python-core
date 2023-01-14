/* Jet Brains Academy topic question solution.

Topic category: Computer science -> Fundamentals  -> Databases and  -> SQL  -> Basics  -> SQL  -> Subqueries
Topic name: Subqueries
Question name: Stocks
Question rating: Hard

-=- QUESTION BODY -=-
Question text censored.
-=- QUESTION BODY -=-
*/
-- -=- QUESTION SOLUTION -=-
-- -=- ANSWER CODE START -=-
SELECT SUM(accrual)
FROM dividends
WHERE stockholder_id = (
    SELECT id
    FROM stockholders
    WHERE name = "Henry Richards"
    )
;
-- -=- ANSWER CODE END -=-
/* -=- SAMPLE IO -=-

*/
