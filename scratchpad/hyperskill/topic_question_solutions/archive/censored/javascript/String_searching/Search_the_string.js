/* Jet Brains Academy topic question solution.

Topic category: Computer science  -> Programming languages  -> Java -> Script  -> Working with data  -> Strings
Topic name: String searching
Question name: Search the string
Question rating: Medium

-=- QUESTION BODY -=-
Question text censored.
-=- QUESTION BODY -=-
*/
// -=- QUESTION SOLUTION -=-
// -=- ANSWER CODE START -=-
function searchFruit(fruitOne, fruitTwo) {
  let text = `My favorite fruit is grapes. Because with grapes, you always
    get another chance. 'Cause, you know, if you have a crappy apple or a peach,
    you're stuck with that crappy piece of fruit.
    But if you have a crappy grape, no problem - just move on to the next.
    'Grapes: The Fruit of Hope.'`;
  console.log(text.includes(fruitOne));
  console.log(text.includes(fruitTwo, 50));
}

let fruitOne = "apple";
let fruitTwo = "grapes";
// Call the function here with the arguments
searchFruit(fruitOne, fruitTwo);
// -=- ANSWER CODE END -=-
/* -=- SAMPLE IO -=-
Sample Input 1:

Sample Output 1:

true
false
*/
