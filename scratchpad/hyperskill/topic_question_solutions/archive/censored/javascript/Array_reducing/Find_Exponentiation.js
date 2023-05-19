/* Jet Brains Academy topic question solution.

Topic category: Computer science  -> Programming languages  -> Java -> Script  -> Working with data  -> Arrays
Topic name: Array reducing
Question name: Find Exponentiation
Question rating: Hard

-=- QUESTION BODY -=-
Question text censored.
-=- QUESTION BODY -=-
*/
// -=- QUESTION SOLUTION -=-
// -=- ANSWER CODE START -=-
function calculateExp(numbers){
    let result = numbers.reduceRight((exponent, base) => Math.pow(base, exponent));
    console.log(result);
}
// -=- ANSWER CODE END -=-
/* -=- SAMPLE IO -=-
Sample Input 1:

1 2 3

Sample Output 1:

1

Sample Input 2:

2 1 2

Sample Output 2:

2

Sample Input 3:

2 2 1

Sample Output 3:

4
*/
