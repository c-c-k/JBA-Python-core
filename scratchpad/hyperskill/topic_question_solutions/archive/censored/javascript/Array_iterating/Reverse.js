/* Jet Brains Academy topic question solution.

Topic category: Computer science  -> Programming languages  -> Java -> Script  -> Working with data  -> Arrays
Topic name: Array iterating
Question name: Reverse
Question rating: Hard

-=- QUESTION BODY -=-
Question text censored.
-=- QUESTION BODY -=-
*/
// -=- QUESTION SOLUTION -=-
// -=- ANSWER CODE START -=-
function reverse(arr) {
    let temp;
    for (let i = 0, j = (arr.length - 1) ; i < j ; i++, j--) {
        temp = arr[i];
        arr[i] = arr[j];
        arr[j] = temp;
    }
    return arr;
}
// -=- ANSWER CODE END -=-
/* -=- SAMPLE IO -=-
Sample Input 1:

[ 'a', 'b', 'c', 'd' ]

Sample Output 1:

[ 'd', 'c', 'b', 'a' ]
*/
