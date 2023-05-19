/* Jet Brains Academy topic question solution.

Topic category: Computer science -> Fundamentals  -> Databases and  -> SQL  -> Basics  -> SQL  -> Data  -> Modification  -> Language
Topic name: Inserting selected rows
Question name: New job
Question rating: Medium

-=- QUESTION BODY -=-
Question text censored.
-=- QUESTION BODY -=-
*/
-- -=- QUESTION SOLUTION -=-
-- -=- ANSWER CODE START -=-
INSERT INTO managers
    (name, surname, manager_email)
SELECT
    name, surname, seller_email
FROM sellers
WHERE CONCAT(name, surname) = "JohnMarley"
;
-- -=- ANSWER CODE END -=-
/* -=- SAMPLE IO -=-

*/
