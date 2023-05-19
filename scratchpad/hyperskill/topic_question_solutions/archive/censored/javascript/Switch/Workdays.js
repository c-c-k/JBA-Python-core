/* Jet Brains Academy topic question_text solution.

Topic category: Computer science -> Programming languages -> Java -> Script -> Basics -> Conditions
Topic name: Switch
Question name: Workdays
Question rating: Hard

-=- QUESTION BODY -=-
Question text censored.
-=- QUESTION BODY -=-
*/
// -=- QUESTION SOLUTION -=-
// -=- ANSWER CODE START -=-
function checkTheDate(value){
    switch (value) {
      case 1:
      case 2:
      case 3:
      case 4:
      case 5:
        console.log("Yes, you should go to work");
        break;
      default:
        console.log("No, this is your well-deserved weekend!");
        break;
	}
}
// -=- ANSWER CODE END -=-
/* -=- SAMPLE IO -=-
Sample Input 1:

1

Sample Output 1:

Yes, you should go to work
*/
