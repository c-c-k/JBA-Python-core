/* Jet Brains Academy topic question solution.

Topic category: Computer science -> Fundamentals  -> Databases and  -> SQL  -> DBMS  -> My -> SQL  -> DB objects
Topic name: Stored Procedure Parameters
Question name: Geometric progression
Question rating: Hard

-=- QUESTION BODY -=-
Question text censored.
-=- QUESTION BODY -=-
*/
-- -=- QUESTION SOLUTION -=-
-- -=- ANSWER CODE START -=-
CREATE PROCEDURE Progression(
    INOUT a INT,
    IN n INT
)
BEGIN
    SET a = a + n;
END;
-- -=- ANSWER CODE END -=-
/* -=- SAMPLE IO -=-

*/
