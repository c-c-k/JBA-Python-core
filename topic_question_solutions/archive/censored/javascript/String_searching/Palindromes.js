/* Jet Brains Academy topic question solution.

Topic category: Computer science  -> Programming languages  -> Java -> Script  -> Working with data  -> Strings
Topic name: String searching
Question name: Palindromes
Question rating: Medium

-=- QUESTION BODY -=-
Question text censored.
-=- QUESTION BODY -=-
*/
// -=- QUESTION SOLUTION -=-
// -=- ANSWER CODE START -=-
function isPalindrome(userStr) {
    for (let letter = 0; letter < userStr.length / 2; letter++) {
        if (userStr.charAt(letter) !== userStr.charAt(userStr.length - letter - 1)) {
            return false;
        }
    }
    return true;
}

console.log(isPalindrome("racecar"));
console.log(isPalindrome("javascript"));
// -=- ANSWER CODE END -=-
/* -=- SAMPLE IO -=-
Sample Input 1:

Sample Output 1:

true
false
*/
