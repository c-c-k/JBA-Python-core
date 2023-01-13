/* Jet Brains Academy topic question solution.

Topic category: Computer science -> Fundamentals  -> Databases and  -> SQL  -> Basics  -> SQL  -> Retrieving  -> Data
Topic name: SELECT FROM statement
Question name: Titanic
Question rating: Hard

-=- QUESTION BODY -=-
Question text censored.
-=- QUESTION BODY -=-
*/
-- -=- QUESTION SOLUTION -=-
-- -=- ANSWER CODE START -=-
SELECT
    CONCAT(CONCAT(first_name, ' '), last_name) AS 'full name',
    (1912 - age) AS 'year of birth',
    passenger_class AS 'passenger''s class'
FROM
    Titanic_passengers
;
-- -=- ANSWER CODE END -=-
/* -=- SAMPLE IO -=-

*/
