/* Jet Brains Academy topic question solution.

Topic category: Computer science  -> Programming languages  -> Java -> Script  -> Working with data  -> Strings
Topic name: String transforming
Question name: Substrings
Question rating: Hard

-=- QUESTION BODY -=-
Question text censored.
-=- QUESTION BODY -=-
*/
// -=- QUESTION SOLUTION -=-
// -=- ANSWER CODE START -=-
function greeting(line) {
    let name = line.substring(0, 10).trim();
    let job = line.substring(20).trim();
    return ("My name is " + name + " and I'm a " + job + ".");
}
// -=- ANSWER CODE END -=-
console.log(greeting("John      john2000  frontend developer"));
/* -=- SAMPLE IO -=-
Sample Input 1:

John      john2000  frontend developer

Sample Output 1:

My name is John and I'm a frontend developer.
*/
