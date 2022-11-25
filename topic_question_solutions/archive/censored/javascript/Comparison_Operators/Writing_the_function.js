/* Jet Brains Academy topic question solution.

Topic category: Computer science -> Programming languages -> Java -> Script -> Basics -> Operations
Topic name: Comparison Operators
Question name: Writing the function
Question rating: Medium

-=- QUESTION BODY -=-
Question text censored.
-=- QUESTION BODY -=-
*/
// -=- QUESTION SOLUTION -=-
// -=- ANSWER CODE START -=-
const strict = value => Number(value) === String(value);
let printStrict = function(value) {
    console.log(strict(value));
};
printStrict(5);
// -=- ANSWER CODE END -=-
/* -=- SAMPLE IO -=-

*/
