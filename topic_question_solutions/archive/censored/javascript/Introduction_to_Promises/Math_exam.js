/* Jet Brains Academy topic question solution.

Topic category: Computer science  -> Programming languages  -> Java -> Script  -> Advanced features  -> Promise
Topic name: Introduction to Promises
Question name: Math exam
Question rating: Medium

-=- QUESTION BODY -=-
Question text censored.
-=- QUESTION BODY -=-
*/
// -=- QUESTION SOLUTION -=-
// -=- ANSWER CODE START -=-
function passingExam (myPoints) {
	return new Promise(function(resolve, reject) {
    if (myPoints >= 90) {
      resolve("You are enrolled!")
    } else {
      reject ("Sorry, you haven't passed the Math exam")
    }
  });
}
// -=- ANSWER CODE END -=-
/* -=- SAMPLE IO -=-
Sample Input 1:

80

Sample Output 1:

Sorry, you haven't passed the Math exam
*/
