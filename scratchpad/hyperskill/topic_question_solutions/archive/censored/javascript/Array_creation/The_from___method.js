/* Jet Brains Academy topic question solution.

Topic category: Computer science  -> Programming languages  -> Java -> Script  -> Working with data  -> Arrays
Topic name: Array creation
Question name: The from() method
Question rating: Hard

-=- QUESTION BODY -=-
Question text censored.
-=- QUESTION BODY -=-
*/
// -=- QUESTION SOLUTION -=-
// -=- ANSWER CODE START -=-
function getArrayWithLength(string) {
  return Array(Array.from(string));
}
// -=- ANSWER CODE END -=-
/* -=- SAMPLE IO -=-
Sample Input 1:

Hello JS Arrays

Sample Output 1:

[ [ 'H', 'e', 'l', 'l', 'o', ' ', 'J', 'S', ' ', 'A', 'r', 'r', 'a', 'y', 's' ] ]
*/
