/* Jet Brains Academy topic question solution.

Topic category: Computer science -> Fundamentals  -> Databases and  -> SQL  -> Basics  -> SQL  -> Data  -> Modification  -> Language
Topic name: Inserting selected rows
Question name: Make it work
Question rating: Medium

-=- QUESTION BODY -=-
Question text censored.
-=- QUESTION BODY -=-
*/
-- -=- QUESTION SOLUTION -=-
-- -=- ANSWER CODE START -=-
INSERT INTO furniture (product_name, inventory_number)
SELECT chair_name, inventory_number
FROM chairs
;
-- -=- ANSWER CODE END -=-
/* -=- SAMPLE IO -=-

*/
