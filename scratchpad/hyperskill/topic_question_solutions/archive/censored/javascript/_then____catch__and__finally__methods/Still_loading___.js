/* Jet Brains Academy topic question solution.

Topic category: Computer science  -> Programming languages  -> Java -> Script  -> Advanced features  -> Promise
Topic name: "then", "catch" and "finally" methods
Question name: Still loading...
Question rating: Medium

-=- QUESTION BODY -=-
Question text censored.
-=- QUESTION BODY -=-
*/
// -=- QUESTION SOLUTION -=-
// -=- ANSWER CODE START -=-
function loader(value) {
    const promise = new Promise(function(resolve, reject){
        if (value === "true"){
            resolve();
        } else {
            reject();
        }
    });

    promise
        .then(() => console.log("The info has loaded."))
        .catch(() => console.log("Please, try again later."))
        .finally(() => console.log("Hello, Mr. Smith!"));
}
// -=- ANSWER CODE END -=-
/* -=- SAMPLE IO -=-
Sample Input 1:

true

Sample Output 1:

The info has loaded.
Hello, Mr. Smith!
*/
