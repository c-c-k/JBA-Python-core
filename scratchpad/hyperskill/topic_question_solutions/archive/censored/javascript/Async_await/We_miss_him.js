/* Jet Brains Academy topic question solution.

Topic category: Computer science  -> Programming languages  -> Java -> Script  -> Basics  -> Functions
Topic name: Async/await
Question name: We miss him
Question rating: Medium

-=- QUESTION BODY -=-
Question text censored.
-=- QUESTION BODY -=-
*/
// -=- QUESTION SOLUTION -=-
// -=- ANSWER CODE START -=-
async function rockBand(bandName) {
    return new Promise(function(resolve, reject) {
      if (bandName === 'Linkin Park') {
          return resolve('Chester, we miss you!');
      } else {
          return reject('No matter the band we miss him anyway!');
      }
    });
}
// -=- ANSWER CODE END -=-
/* -=- SAMPLE IO -=-
Sample Input 1:

Linkin Park

Sample Output 1:

Chester, we miss you!
*/
