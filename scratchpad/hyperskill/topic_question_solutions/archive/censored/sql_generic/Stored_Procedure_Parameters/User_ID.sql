/* Jet Brains Academy topic question solution.

Topic category: Computer science -> Fundamentals  -> Databases and  -> SQL  -> DBMS  -> My -> SQL  -> DB objects
Topic name: Stored Procedure Parameters
Question name: User ID
Question rating: Medium

-=- QUESTION BODY -=-
Question text censored.
-=- QUESTION BODY -=-
*/
-- -=- QUESTION SOLUTION -=-
-- -=- ANSWER CODE START -=-
CREATE PROCEDURE GetUserByID(
    IN InputID INT
)
BEGIN
    SELECT *
    FROM users
    WHERE user_id = InputID;
END;
-- -=- ANSWER CODE END -=-
/* -=- SAMPLE IO -=-

*/
