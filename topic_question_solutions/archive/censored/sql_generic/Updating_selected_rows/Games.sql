/* Jet Brains Academy topic question solution.

Topic category: Computer science -> Fundamentals  -> Databases and  -> SQL  -> Basics  -> SQL  -> Data  -> Modification  -> Language
Topic name: Updating selected rows
Question name: Games
Question rating: Hard

-=- QUESTION BODY -=-
Question text censored.
-=- QUESTION BODY -=-
*/
-- -=- QUESTION SOLUTION -=-
-- -=- ANSWER CODE START -=-
UPDATE games
SET
    publisher = "Macrofiber",
    users_rating = users_rating - 2.5
WHERE
    title In ("Bridges", "Ship Simulator 2")
;
-- -=- ANSWER CODE END -=-
/* -=- SAMPLE IO -=-

*/
