/* Jet Brains Academy topic question solution.

Topic category: Computer science  -> Programming languages  -> Java -> Script  -> Basics  -> Loops
Topic name: Break and Continue
Question name: The sum of numbers
Question rating: Hard

-=- QUESTION BODY -=-
Question text censored.
-=- QUESTION BODY -=-
*/
// -=- QUESTION SOLUTION -=-
// -=- ANSWER CODE START -=-
function sum(numbers) {
    let currentSum = 0;
    for (const number of numbers) {
      if (number !== 0) {
        currentSum += number;
      } else {
        break;
      }
    }
    return currentSum;
}
// -=- ANSWER CODE END -=-
/* -=- SAMPLE IO -=-
Sample Input 1:

11 12 15 10 0 100

Sample Output 1:

48

Sample Input 2:

100 0 100

Sample Output 2:

100
*/
