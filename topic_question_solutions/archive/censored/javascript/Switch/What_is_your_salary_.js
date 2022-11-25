/* Jet Brains Academy topic question solution.

Topic category: Computer science -> Programming languages -> Java -> Script -> Basics -> Conditions
Topic name: Switch
Question name: What is your salary?
Question rating: Medium

-=- QUESTION BODY -=-
Question text censored.
-=- QUESTION BODY -=-
*/
// -=- QUESTION SOLUTION -=-
// -=- ANSWER CODE START -=-
function getSalary(value){
  let salary;
  switch (value) {
    case "Bootstrap":
      salary = 15;
      break;
    case "Chrome Extension":
      salary = 20;
      break;
    case "React":
      salary = 30;
      break;
    default:
      salary = 25;
      break;
  }
  console.log(`$${salary} per hour`);
}
// -=- ANSWER CODE END -=-
getSalary("django")
/* -=- SAMPLE IO -=-
Sample Input 1:

Bootstrap

Sample Output 1:

$15 per hour
*/
