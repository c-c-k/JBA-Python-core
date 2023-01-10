/* Jet Brains Academy topic question solution.

Topic category: Computer science  -> Programming languages  -> Java -> Script  -> Working with data  -> Arrays
Topic name: Array reducing
Question name: Calculate Savings
Question rating: Medium

-=- QUESTION BODY -=-
Question text censored.
-=- QUESTION BODY -=-
*/
// -=- QUESTION SOLUTION -=-
// -=- ANSWER CODE START -=-
const salary = 25000;

function getSalary(expenses) {
    let remainingSalary = expenses.reduce((remainingSalary, expense) => remainingSalary - expense, salary);
    console.log(remainingSalary);
}
// -=- ANSWER CODE END -=-
/* -=- SAMPLE IO -=-
Sample Input 1:

200 1000 300 550

Sample Output 1:

22950
*/
