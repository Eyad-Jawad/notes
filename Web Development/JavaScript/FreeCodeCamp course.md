### Variable decleration
you can declare a variable saying :
```javascript
var a = 0; /* this will declare the variable in the function scope, 
the whole function */
let a = 0; /* unlike this that will narrow its 
scope to the {} it's in, the current block */
const a = 0; // like let, but const
a = 0; // this will declare it globally, to the whole file
```
Data Types: undefined, boolean, null, string, number, symbol, and object
you can also declare a variable then assign a value to it later

NOTE: The semicolon ";" is not necessary, but you should very well use it

console.log() is like print in other languages, in a website however, it'll show stuff in the console when you click inspect the code or something idk
```javascript
console.log("lol");
```

to run a JS file you could do:
```bash
node file.js
```

for strings we have:
```javascript
let somethingLength = "Something".length;
```
you can treat strings in JS just like you do in C, aka; use [], but if you remember, strings are consts, you can change the whole string, but not only a part of it

Function:
```javascript
function example(someInputNumber) {
	someInputNumber--;
	return someInputNumber;
}
```

arrays in JS can be anything:
```javascript
var ex = ["lol", 32, [3]];
```
you can modify an array's elements in JS:
```javascript
ex[1] = 33;
```
you can append elements to an array using the push method:
```javascript
ex.push(33);
lastElement = ex.pop();
firstElement = ex.shift();
ex.unshift("Lol"); // I think it's clear what this does
```

``` javascript
console.log(JSON.stringify([1, 2, 3]));
```

```javascript
if (idkWhat == 1) {
	console.log("lol, idk");
}
```
the equality operator == in JS will sometimes convert the values into a common type, the strict equality operator will not:
```javascript
a = 3 == '3'  // true
b = 3 === '3' // false
```
it's better to just use === all of the time
same with inequality:
```javascript
a = 3 != '3'  // false
b = 3 !== '3' // true
```
other than that, logical operators are identical to C (since it's based on it)
```javascript
if (something) {
	console.log("lol");
} else if (idk) {
	console.log("lol, idk");
}
```
the shorthand if is also the same, (here it is if you can't reacall it):
``` javascript
(idkWhat) ? doIfTrue() : doIfFalse();
```

the switch-case syntax is also identical, and it uses the strict equality

```javascript
let something = {
	"Laugh": "lol",
	"Laugh Hard": "LMAO",
	idkWhat: "Idk what sir"
};
console.log(something.Laugh); // can also be used to add an element
console.log(something["Laugh Hard]");
delete something.Laugh;
if (!something.hasOwnProperty("Laugh")) {
	console.log("It was deleted"); // this will print
}
```
a way to copy an object:
```javascript
let somethingTwo = JSON.parse(JSON.stringify(something));
```
while, do while, and for loops are nearly identical with of C except that you say var (or let) instead of int in for loops

to convert string to an int, use :
```javascript
let num = parseInt("23");
let binaryToInt = parseInt("1011", 2);
```

you can write "use strict" plainly in a JS file to let the compiler catch even the smallest errors and bugs
```Javascript
"use strict";
```

you can't change a const array, however, you could change every element in it individually and mutate the array, to prevent that we can do:
```javascript
Object.freeze(something);
```

you can assign function to variables to do cool things (they say):
```javascript
let thisGuy = function() {
	return true;
}

let thatguy = () => {
	return true;
}
// those two above are identical
// and if you have a function that returns one thing only you could do this:
let lastGuy = () => true;
```

in JS there's something called the rest operator, which takes the input and puts them into an array, when the input is changing in size:
```javascript
const sum = (() => {
	return function sum(...args) {
		return args.reduce((a, b) => a + b, 0);
	};
}) ();
console.log(sum(1, 2 ,3 ,4 ,5));
console.log(sum(32, 2));
```

chat gpt says that when you use {} with an arrow function, it turns it into an expression, and that () at the end calls the function immediately after, and this design quirck is called **IIFE** (Immediately Invoked Function Expression).

we can use something called the spraed operator to copy arrays:
```javascript
arr2 = [...arr1]; // this will have the same problems that 
// require deep copy in Python
```

we can do this in C (I think):
```C
int a, b, c = obj.x, obj.y, obj.z;
```
in JS we can do this:
```javascript
const {x : a, y : b, z : c} = obj;
```
this is called destructuring, we can do this as well:
```javascript
const [a, , , b] = [1, 2, 3, 4]; // a = 1, b = 4
[a, b] = [b, a]; // you could also swap vars using it
```

you can use the stuff above inside function parameters, or with one and another to do cool stuff, idk
```javascript
const idk = function({x, y}) {
	return x + y;
}
console.log(obj); // some onject with many attrs, but we only 
// needed and used two of them
```

we can use backticks as a text formatter in JS with multiline stuff and variables:
```javascript
let guy = {name: "homan", age: 88};
const greet = `I'm "${guy.name}"
I come to conquer this planet before I turn 100 in ${100 - guy.age} years!`;
console.log(greet);
```

if you do return {varName} it'll return an obj with the key varName and value as its value
you could also do it when declaring an obj, or when at that, one of the keys is a function you could ignore setting a function, as you would do in an array

you can export {aFunction} in some file to import {aFunction} from "thatFile"
```javascript
import a* as idkWhat from "file.js";
```
there's also default import/export



### Math
we have a lot of interseting math function:
```javascript
Math.round(3.8);
Math.floor(3.3);
Math.random(); // we can use some tricks with this btw
```


