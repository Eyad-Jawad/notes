
One of many JavaScript HTML methods is `getElementById()`.
The example below "finds" an HTML element (with id="demo"), and changes the element content (innerHTML) to "Hello JavaScript":
``` javascript
document.getElementById("demo").innerHTML = "Hello JavaScript";
```
to hide elements in javascript change the display value of the element to 'none', and to show it change it to block
```javascript
document.getElementById("demo").style.display = "none";
```
A JavaScript `function` is a block of JavaScript code, that can be executed when "called" for.
``` html
<script>  
function myFunction() {  
  document.getElementById("demo").innerHTML = "Paragraph changed.";  
}  
</script>
```
then in another place:
```html
<button type="button" onclick="myFunction()">Try it</button>
```
to reference to external js code:
```html
<script src="myScript.js"></script>
```

JavaScript can "display" data in different ways:
- Writing into an HTML element, using `innerHTML` or `innerText`.
- Writing into the HTML output using `document.write()`.
- Writing into an alert box, using `window.alert()`.
- Writing into the browser console, using `console.log()`.

you can pass an unspecified amount of arguments and it'll be passed as an array:

```javascript
function something() {
	let n = arguments.length;
}
```

you can use it to access excess arguments, or pass them as :
```javascript
function something(...args) {
	let n = args.length;
}
```

```javascript
const idkwhat = function() { return 1; };
```

this is called function expression.

The difference between them and regular functions is that you cannot call them before 
declaration, you can do that with regular fucntions (it appears).

they say: Function declarations are "hoisted" to the top of their scope. This means you can call a function before it is defined in the code.

Arrow functions are a shorthand for expression functions and the modern way to write the latter:

```javascript
const idkwhat = (a, b) => a + b;
```

You can skip the {} if the function is as short as that.
you can also skip the () if it's one argument you're passing, exactly 1, and not 0

arrow functions do not have their `this` value, they only inherit it from surronding code, and using `this` will result in undefined behavior


### Objects
Weirdly enough, object in JS are dictionaries:
```javascript
const obj = {
	idkWhat: true, // property
	idkingWhat: function (isLol) {return !isLol;} // method
};
```

you can acess them using the dot operator, or brackets, you can also make new properties or methods using that

objects that are simple, and not declared using the `new` keyword are called object literalls

you can use `this` with the objects' methods

![[Pasted image 20260428100335.png]]

Primitivies are : string, Nnumber, boolean, bigInt, null, undefined, symbol

```javascript
delete obj.idkWhat; // deletes both key and value
```

To check whether a property exists in an object you can say:
```javascript
if ("idkWhat" in obj) {...}
```

You can do nested objects btw

Btw, for each loops from C++ are for in here:

```javascript
for (let x in idkwat) {...}
```

And you can use it with objects:

```javascript
for (let [key, value] in Object.entries(obj)) {...}
```

to make an array out of an object's values you can do:
```javascript
cosnt vals = Object.values(obj);
```

You can also print an object that'll look funky:
```javascript
console.log(JSON.stringify(obj));
```

To make a constructer  in an object you can do:

```javascript
fucntion Obj(idkWhat) {
	this.idkWhat = idkWhat;
}

const idkWhatting = new Obj("idkWhat");
```

Idk what but I think that you can't use the variable `idkWhatting` to make a method in it, so you should use Obj, but Obj is a constructer, so to add a method do:
```javascript
Obj.prototype.idkWhatting = function() {
	return "lol";
}
```

Built in constructers:

```javascript
new Object()   // A new Object object  
new Array()    // A new Array object  
new Map()      // A new Map object  
new Set()      // A new Set object  
new Date()     // A new Date object  
new RegExp()   // A new RegExp object  
new Function() // A new Function object
			   // (please don't use those)

"";            // primitive string  
0;             // primitive number  
false;         // primitive boolean  
  
{};            // object object  
[];            // array object  
/()/           // regexp object  
function(){};  // function
```

Global variables defined with the `var` keyword belong to the window object

Code blocks that exist independently are called standalone block:

```javascript
{
	let idkWhat = "lol";
}
```

var declared variables are - weirdly enough - hoisted, which means that you can assign and eseentially use a variable then declare it after a that, it'll be function scoped of course

To use strict mode just write `"use strict";` in any scope, and many of the weird things like previously discussed undecalred variables will prompt an error, you also can't delete objects or functions, octal literals or escape characters are also not allowed, you also can't read a set only or set a get only property, you can't use `with (module)...`, you can't use some keywords for variable names, you can't use the variables from `eval`:
```javascript
eval("x = 2");
console.log(x); // error
```

The syntax, for declaring strict mode, was designed to be compatible with older versions of JavaScript. Compiling a numeric literal (4 + 5;) or a string literal ("John Doe";) in a JavaScript program has no side effects. It simply compiles to a non existing variable and dies.

## Array

you can convet an array to a comma spearated string using the method:

``` javascript
let things = arr.toString();
```

you can use another method if you want to separate them with something else:
```javascript
let things = arr.join(" ");
```

Array methods:
```javascript
let idkWhat = arr.length;
arr.sort();
arr.at(idx) = "idkWhat";
arr4 = arr1.concat(arr2, arr3);
arr5 = arr.with(2, "lol"); // changes an element and returns a new array
arr.copyWithin(2, 0, 2); // Copy to index 2, the elements from index 0 to 2, the third argument is optional
arr = arr.flat(2); // you can give how many layers to flat? idk

// ways to add elements:
const newLength = arr.push("idkWhat");
const newLength = arr.unshift("firstIdkWhat");
arr[arr.length] = "idkWhat";

// ways to delete an element:
let idkWhat = arr.pop();
let firstIdkWhat = arr.shift();

// ways to identify arrays:
if (Array.isArray(arr))
if (arr instantof Array)
```

you can also subtitute `for in` with:
```javascript
arr.forEach(someFunction);
function someFunction(value, index, array) {...}
```

```javascript
const arr = new Array(5); // this will create an array of size 5 
```


The `flatMap()` method first maps all elements of an array and then creates a new array by flattening the array:
```javascript
const myArr = [1, 2, 3, 4, 5, 6];  
const newArr = myArr.flatMap(x => [x, x * 10]);
// terminal:
// [1, 10, 2, 20, 3, 30, 4, 40, 5, 50, 6, 60]
```

The `splice` method can be used to delete items without leaving a hole, and replace them as well

```javascript
arr.splice(0, 2, "lol", "idkWhat"); // replace the first two items with these
arr.splice(3, 1); // delete element at 3
arr.splice(startFrom, deleteThisMuch);
```

The method `tospliced` is the same, but it makes a new array instead of editing the original

The method `slice` is like in python, if you do `arr.slice(1);` it'll make a new array starting from 1, if you give another parameter `arr.slice(1, 4);` it'll make a slice from 1 to 4

to search for an item's index:

```javascript
arr.indexOf(item, start);
// returns the first match if it exists
// return -1 on fail
// input can be negative in start
arr.lastIndexOf(item, start)
// same as above but returns the first match
```

the equavilant of `in` in python:

```javascript
arr.includes(item);
```

The `find()` method returns the value of the first array element that passes a test function:

```javascript
arr.find(func)
function func(value, index, array) {
	return value === 0;
}
```

another method `findIndex` works the same but returns the index, so does `findLast` and `findLastIndex`
you can abbreviate it using an arrow function:

```javascript
arr.find(x => x === 0);
```

we have methods for sorting, which are:

```javascript
arr.sort();      // alphabetically sort it
arr.reverse();

const newArr = arr.toSorted(); // makes a new array without altering the original one
const newerArr = newArr.toReversed();
```

the method `sort` sorts arrays as strings, that's why we can't use it to sort numbers, but we can feed it a function:

```javascript
arr.sort((x, y) => { return x - y; });
```

you can feed it many other things, a way to shuffle an array is to feed it this:

```javascript
arr.sort(() => { return 0.5 - Math.random(); });
```

but this method is inaccurate, so we'd use a method called the Fisher Yates method:

```javascript
const arr = [...];

for (let i = arr.lenght - 1; i > 0; i--) {
	let idx = Math.floor(Math.random() * (i + a));
	let c = arr[idx];
	arr[idx] = arr[i];
	arr[i] = c;
}
```

to find the minimum of maximum value in an array, use:

```javascript
const max = Math.max.apply(null, arr);
const min = Math.min.apply(null, arr);
```

The `map` method runs a function on each array and makes a new array out of it:

```javascript
arr.map(func);
function func(value, index, array) {...}
```

we also have `flatMap` that maps then flats an array to a new one, there's also the `filter` method that makes a new array accordding to a filter:

```javascript
arr.filter(func);
```

The `reduce` method runs a function on each array element to produce a single value, it runs from left to right, `reduceRight` runs the other way:

```javascript
const sum = arr.reduce(func);
function func(total, value, index, array) {
	return total + value;
}
```

you can also pass an intial value:

```javascript
const sum = arr.reduce(func, 10);
```

The `every()` method checks if all array values pass a test
while the `some()` method checks if some array values pass a test.

```javascript
if (arr.every(func)) {...}
```

the method `from` makes an array from anything, as long as it has length and iterable, it also accepts a function:

```javascript
const k = Array.from(arr, x => x * 2);
```

there's also the spread operator that treats each elements as an array I think?

```javascript
console.log(...arr);
```

The rest operator (...) allows us to destruct an array and collect the leftovers:

```javascript
let a, b, c;
[a, b, ...c] = arr;
```

## Set

to make a set you'd do:

```javascript
const set = new Set();
const anotherSet = new Set(arr);

let length = set.size;

set.add(1);
set.clear();
set.delete(1);

if (set.has(1)) {...}

set.forEach(func);

const set3 = set.union(set2);
const set3 = set.intersection(set2);
const set3 = set.difference(set2);
const set3 = set.symmetricDifference(set2);

if (set.isDisJointForm(set2)) {...}
if (set.isSubsetOf(set2)) {...}
if (set.isSupersetOf(set2)) {...}
```

you can also do `values`, `keys`, and `entries` 
there's also `weakSet`, where the elements are objects
![[Pasted image 20260504183746.png]]

## Map

```javascript
const map = new Map();
const map2 = new Map(arr);  // the array must be like this:
							// [[1, 2], [1, 2]...]

map.set("name", "lol");
const ans = map.get("name");
map.delete("name");
map.clear();

let length = map.size;
map.forEach(func);

if(map.has("name")) {...}
```

there's a method `groupBy` that I'm not sure how it works cuz it's very new; 24
you can also use `values`, `keys`, and `entries` method

![[Pasted image 20260504184402.png]]

there's also `weakMap` that's values are objects

## Iterators
![[Pasted image 20260504185624.png]]

```javascript
for (let key in obj) {
	console.log(obj[key]);
}
```

there's a method called `next` that acts like python's `yeild`, you can do it without using Symbol.iterator, but with it you'll be able to use `for ... of...`

```javascript
const obj = {};

obj[Symbol.iterator] = function() { // must
	let something = 0;
	let done = false; // must
	return {
		next() { // msut
			something += 2;
			if (something == 10) { done : true };
			return {value : something, done : done}; // must
		}
	};
}
```

`value` is the iteratd value, and `done` is the state of the iterator; done or not

![[Pasted image 20260505102516.png]]

to make an iterator out of an existing thing you do:

```javascript
const iter = Iterator.from([1, 2, 3]);
iter.drop(1);
const iter2 = iter.take(2);

if (iter.every(func)) {...}
if (iter.some(func)) {...}

cosnt iter2 = iter.filter(func);
const iter2 = iter.map(func);
const iter2 = iter.flatMap(func);
iter.forEach(func);

const something = iter.reduce(func);

const arr = iter.find(func);
```

Javascript also has `yeild`, but it acts a little differently, or not, when you say `yeild`, the execution stops to return the value, and can be resumed, until you say `return`, it'll keep generating values:

```javascript
function* gen() {
	yeild 1;  // done : false
	yeild 2;  // done : false
	return 3; // done : true
}
let generator = gen();
for (let val of generator) {...}
```

![[Pasted image 20260505103839.png]]

Built in objects:
![[Pasted image 20260515213221.png]]

## Math
```javascript
Math.E        // returns Euler's number  
Math.PI       // returns PI  
Math.SQRT2    // returns the square root of 2  
Math.SQRT1_2  // returns the square root of 1/2  
Math.LN2      // returns the natural logarithm of 2  
Math.LN10     // returns the natural logarithm of 10  
Math.LOG2E    // returns base 2 logarithm of E  
Math.LOG10E   // returns base 10 logarithm of E

Math.round(x) // Returns x rounded to its nearest integer
Math.ceil(x)  // Returns x rounded up to its nearest integer
Math.floor(x) // Returns x rounded down to its nearest integer
Math.trunc(x) // Returns the integer part of x
Math.sign(x)  // return the sign of the number

Math.pow(x, y);
Math.sqrt(x);
Math.abs(x);
Math.log(x);
Math.log2(x);
Math.log10(x);

Math.sin(x);
Math.cos(x);

Math.min(x, ...);
Math.max(x, ...);
Math.random();

// for more functions: https://www.w3schools.com/js/js_math_reference.asp
```

you can also use an integer than is not size limited two ways:
```javascript
const a = BigInt(1);
const a = 1n;
```

You can use the scientific e notation in javascript number:
```javascript
const n = 5e9
```
## Reg Ex
You can find it in [[RegEx]]














































































































