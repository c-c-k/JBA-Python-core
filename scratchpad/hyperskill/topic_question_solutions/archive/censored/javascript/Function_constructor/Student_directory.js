/* Jet Brains Academy topic question solution.

Topic category: Computer science  -> Programming languages  -> Java -> Script  -> Basics  -> Functions
Topic name: Function constructor
Question name: Student directory
Question rating: Medium

-=- QUESTION BODY -=-
Question text censored.
-=- QUESTION BODY -=-
*/
// -=- QUESTION SOLUTION -=-
// -=- ANSWER CODE START -=-
function Student(name, surname, age) {
  this.name = name;
  this.surname = surname;
  this.age = age;

  // write your function here
  this.getStudent = function () {
    console.log(
        `Student name: ${this.name}, `
        + `student surname: ${this.surname}, `
        + `student age: ${this.age}`
    );
  }
}

const student = new Student("Alex", "Brown", 28);
// -=- ANSWER CODE END -=-
/* -=- SAMPLE IO -=-
Sample Input 1:

Sample Output 1:

Student name: Alex, student surname: Brown, student age: 28
*/
