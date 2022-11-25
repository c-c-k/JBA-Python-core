/* Jet Brains Academy topic question solution.

Topic category: Computer science -> Programming languages -> Java -> Script -> Basics -> Functions
Topic name: Scope of variables
Question name: Your own function
Question rating: Medium

-=- QUESTION BODY -=-
Question text censored.
-=- QUESTION BODY -=-
*/
// -=- QUESTION SOLUTION -=-
// -=- ANSWER CODE START -=-
let myFunc = () => {
    for (let i = 1; i <= 5; i++) {
        console.log(i ** 3);
    }
};
/*
let myFunc = () => {for (let i = 1; i <= 5; i++) { console.log(i**3);}};
*/
// -=- ANSWER CODE END -=-
myFunc();
/* -=- SAMPLE IO -=-
Sample Input 1:

Sample Output 1:

1
8
27
64
125
*/
