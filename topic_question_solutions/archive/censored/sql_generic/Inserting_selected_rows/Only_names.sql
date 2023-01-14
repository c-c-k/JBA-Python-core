/* Jet Brains Academy topic question solution.

Topic category: Computer science -> Fundamentals  -> Databases and  -> SQL  -> Basics  -> SQL  -> Data  -> Modification  -> Language
Topic name: Inserting selected rows
Question name: Only names
Question rating: Medium

-=- QUESTION BODY -=-
Question text censored.
-=- QUESTION BODY -=-
*/
-- -=- QUESTION SOLUTION -=-
-- -=- ANSWER CODE START -=-
INSERT INTO employees (first_name, last_name)
SELECT name, surname
FROM developers
;
-- -=- ANSWER CODE END -=-
/* -=- SAMPLE IO -=-

*/
