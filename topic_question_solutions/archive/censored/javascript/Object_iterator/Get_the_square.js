/* Jet Brains Academy topic question solution.

Topic category: Computer science  -> Programming languages  -> Java -> Script  -> Working with data  -> Objects
Topic name: Object iterator
Question name: Get the square
Question rating: Hard

-=- QUESTION BODY -=-
Question text censored.
-=- QUESTION BODY -=-
*/
// -=- QUESTION SOLUTION -=-
// -=- ANSWER CODE START -=-
function getTheSquare(arrayOfObjects) {
    for (item of arrayOfObjects) {
        item["square"] = Math.sqrt(item["source"]);
    }
    return arrayOfObjects;
}
// -=- ANSWER CODE END -=-
console.log(getTheSquare([{"source":16,"square":null},{"source":64,"square":null},{"source":121,"square":null}]))
/* -=- SAMPLE IO -=-
Sample Input 1:

[{"source":16,"square":null},{"source":64,"square":null},{"source":121,"square":null}]

Sample Output 1:

[ { source: 16, square: 4 },
  { source: 64, square: 8 },
  { source: 121, square: 11 } ]
*/
