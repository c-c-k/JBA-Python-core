/* Jet Brains Academy topic question solution.

Topic category: Computer science  -> Programming languages  -> Java -> Script  -> Working with data  -> Arrays
Topic name: Array transforming
Question name: Convert to number
Question rating: Medium

-=- QUESTION BODY -=-
Question text censored.
-=- QUESTION BODY -=-
*/
// -=- QUESTION SOLUTION -=-
// -=- ANSWER CODE START -=-
function convertToNumber(arrayOfString) {
   return arrayOfString.map((numStr) => Number(numStr));
}
// -=- ANSWER CODE END -=-
/* -=- SAMPLE IO -=-
Sample Input 1:

1 3 5 7 9

Sample Output 1:

[ 1, 3, 5, 7, 9 ]
*/
