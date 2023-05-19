/* Jet Brains Academy topic question solution.

Topic category: Computer science  -> Programming languages  -> Java -> Script  -> Advanced features  -> Promise
Topic name: "then", "catch" and "finally" methods
Question name: Oops! We have a problem
Question rating: Medium

-=- QUESTION BODY -=-
Question text censored.
-=- QUESTION BODY -=-
*/
// -=- QUESTION SOLUTION -=-
// -=- ANSWER CODE START -=-
function hasDownloaded (value) {
    const promise = new Promise(function(resolve, reject){
        if (value === "true"){
            resolve("Now you can watch the video!");
        } else {
            reject("Oops! An error occurs");
        }
    });

    promise
        .then(function (okMessage) {
            console.log(okMessage)
        })
        .catch(function (errMessage) {
            console.log(errMessage)
        });
}
// -=- ANSWER CODE END -=-
/* -=- SAMPLE IO -=-
Sample Input 1:

false

Sample Output 1:

Oops! An error occurs

Sample Input 2:

true

Sample Output 2:

Now you can watch the video!
*/
