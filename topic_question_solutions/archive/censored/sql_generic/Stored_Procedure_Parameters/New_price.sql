/* Jet Brains Academy topic question solution.

Topic category: Computer science -> Fundamentals  -> Databases and  -> SQL  -> DBMS  -> My -> SQL  -> DB objects
Topic name: Stored Procedure Parameters
Question name: New price
Question rating: Hard

-=- QUESTION BODY -=-
Question text censored.
-=- QUESTION BODY -=-
*/
-- -=- QUESTION SOLUTION -=-
-- -=- ANSWER CODE START -=-
CREATE PROCEDURE PriceUpdater(
    IN input_name VARCHAR(255),
    IN input_price INT
)
BEGIN
    UPDATE products
    SET price = input_price
    WHERE name = input_name;
END;
-- -=- ANSWER CODE END -=-
/* -=- SAMPLE IO -=-

*/
