let counter = 0;
// console.log(++counter + " " + a);  // doesn't work due to "a" not having been evaluated yet.
a = "a";  // "a" is implicitly assumed to be a property of the global object.
console.log(++counter + " " + a); // works because "a" is implicitly assumed to be a property of the global object.
console.log(++counter + " " + b); // works but prints "undefined" because the declaration "var b" is hoisted to the top of the script but the assignment 'b=\"b\"' is not.
var b = "b";  // normal global scope variable declaration with var.
console.log(++counter + " " + b);  // normal global variable access.
// console.log(++counter + " " + aa);  // doesn't work due to "aa" not having been evaluated yet.
// console.log(++counter + " " + bb);  // doesn't work due to 'var bb' having a function scope and thus not being visible in the global scope.
function func() {
  var bb = "bb";  // normal function scope variable declaration with var.
  aa = "aa";  // "a" is implicitly assumed to be a property of the global object.
}
func();
console.log(++counter + " " + aa); // works because "aa" is implicitly assumed to be a property of the global object.
// console.log(++counter + " " + bb);  // doesn't work due to 'var bb' having a function scope and thus not being visible in the global scope.
