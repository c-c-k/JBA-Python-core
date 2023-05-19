/* Jet Brains Academy topic question solution.

Topic category: Computer science  -> Programming languages  -> Java -> Script  -> Working with data  -> Arrays
Topic name: Array slicing
Question name: Zero tail
Question rating: Hard

-=- QUESTION BODY -=-
Question text censored.
-=- QUESTION BODY -=-
*/
// -=- QUESTION SOLUTION -=-
// -=- ANSWER CODE START -=-
function removeTail(array) {
  array.splice(-2, 2, 0);
  return array;
}
// -=- ANSWER CODE END -=-
/* -=- SAMPLE IO -=-
Sample Input 1:

[ 'may', 'june', 'july', 'august' ]

Sample Output 1:

[ 'may', 'june', 0 ]
*/
