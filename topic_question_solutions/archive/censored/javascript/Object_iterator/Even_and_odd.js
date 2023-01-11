/* Jet Brains Academy topic question solution.

Topic category: Computer science  -> Programming languages  -> Java -> Script  -> Working with data  -> Objects
Topic name: Object iterator
Question name: Even and odd
Question rating: Hard

-=- QUESTION BODY -=-
Question text censored.
-=- QUESTION BODY -=-
*/
// -=- QUESTION SOLUTION -=-
// -=- ANSWER CODE START -=-
function sumTheArrays(naturalNumbers) {
  oddEven = Object.values(naturalNumbers);
  let summed = [];
  for (let i = 0 ; i < oddEven[0].length; i++) {
    summed[i] = oddEven[0][i] + oddEven[1][i];
  }
  return summed;
}
// -=- ANSWER CODE END -=-
/* -=- SAMPLE IO -=-
Sample Input 1:

{"even":[2,4,6,8,10],"odd":[1,3,5,7,9]}

Sample Output 1:

[ 3, 7, 11, 15, 19 ]
*/
