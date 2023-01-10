/* Jet Brains Academy topic question solution.

Topic category: Computer science  -> Programming languages  -> Java -> Script  -> Basics  -> Functions
Topic name: Function constructor
Question name: Let's study birds
Question rating: Medium

-=- QUESTION BODY -=-
Question text censored.
-=- QUESTION BODY -=-
*/
// -=- QUESTION SOLUTION -=-
// -=- ANSWER CODE START -=-
function Bird(name, color, size) {
  this.name = name;
  this.color = color;
  this.size = size;
}

const amazonParrot = new Bird(name = "Amazon parrot", color = "green", size = "medium");
const canary = new Bird(name = "Canary", color = "orange, red, yellow", size = "small");
// -=- ANSWER CODE END -=-
/* -=- SAMPLE IO -=-
Sample Input 1:

Sample Output 1:

Bird { name: 'Amazon parrot', color: 'green', size: 'medium' }
Bird { name: 'Canary', color: 'orange, red, yellow', size: 'small' }
*/
