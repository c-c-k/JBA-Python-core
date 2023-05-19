/* Jet Brains Academy topic question solution.

Topic category: Computer science -> Fundamentals  -> Databases and  -> SQL  -> Basics  -> SQL  -> Retrieving  -> Data
Topic name: Special WHERE operators
Question name: Cats and dogs
Question rating: Hard

-=- QUESTION BODY -=-
Question text censored.
-=- QUESTION BODY -=-
*/
-- -=- QUESTION SOLUTION -=-
-- -=- ANSWER CODE START -=-
SELECT DISTINCT
    owner
FROM
    animal_owners as cat_owners
WHERE
    animal_kind = "cat"
    AND EXISTS (
        SELECT
            owner
        FROM
            animal_owners
        WHERE
                animal_kind = "dog"
                AND owner = cat_owners.owner
    )
;

-- -=- ANSWER CODE END -=-
/* -=- SAMPLE IO -=-

*/
