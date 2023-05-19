/* Jet Brains Academy topic question solution.

Topic category: Computer science -> Fundamentals  -> Databases and  -> SQL  -> Basics  -> SQL  -> Functions and operations
Topic name: Window functions
Question name: Applying a window function
Question rating: Medium

-=- QUESTION BODY -=-
Question text censored.
-=- QUESTION BODY -=-
*/
-- -=- QUESTION SOLUTION -=-
-- -=- ANSWER CODE START -=-
SELECT
    name,
    SUM(sales) OVER(PARTITION BY color) AS sale
FROM
    chocolate_sales
;
-- -=- ANSWER CODE END -=-
/* -=- SAMPLE IO -=-

*/
