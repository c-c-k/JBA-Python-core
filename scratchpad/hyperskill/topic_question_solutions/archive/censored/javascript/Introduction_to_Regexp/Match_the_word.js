/* Jet Brains Academy topic question solution.

Topic category: Computer science  -> Programming languages  -> Java -> Script  -> Working with data  -> Strings
Topic name: Introduction to Regexp
Question name: Match the word
Question rating: Medium

-=- QUESTION BODY -=-
Question text censored.
-=- QUESTION BODY -=-
*/
// -=- QUESTION SOLUTION -=-
// -=- ANSWER CODE START -=-
function matchTheWord(word) {
  return /tion/i.test(word);
}
// -=- ANSWER CODE END -=-
console.log(matchTheWord("prediction"))
/* -=- SAMPLE IO -=-
Sample Input 1:

prediction

Sample Output 1:

true
*/
