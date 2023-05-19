/* Jet Brains Academy topic question solution.

Topic category: Computer science -> Fundamentals  -> Databases and  -> SQL  -> Basics  -> SQL  -> Retrieving  -> Data
Topic name: Logic and comparison expressions
Question name: Library
Question rating: Hard

-=- QUESTION BODY -=-
Question text censored.
-=- QUESTION BODY -=-
*/
-- -=- QUESTION SOLUTION -=-
-- -=- ANSWER CODE START -=-
SELECT id, title, author, rating
FROM
    books
WHERE
    quantity > 0
    AND (
        author = 'Theodore Dreiser'
		OR author = 'Ayn Rand'
		OR author = 'Harper Lee'
		OR author = 'Mark Twain'
    )
;
-- -=- ANSWER CODE END -=-
/* -=- SAMPLE IO -=-

*/
