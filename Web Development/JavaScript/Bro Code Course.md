4:11:00

to output text type:
```javascript
console.log(`text`); // the back tick is preferred as a place holder
```
this will appear in the console in the "Inspect"
the back tick in this paticular situation is called a template literal that holds or could hold variables

to show something on the window we'd use:
```javascript
window.alert(`lol`);
```

to grab and modify something by id from the HTML file:
```javascript
document.getElementById("id") ///...
```

EX:

```javascript
document.getElementById("textBox").textContent = `lol`;
```

variables:

```javascript
let x; // declaration
x = 10; // assignment 
let x; // error! you cannot declare a variable twice
```

to know the type of a variable use:
```javascript
console.log(typeof(x));
```
there are :
number, string, boolean, and many other types

```javascript
let twoTo10 = 2 ** 10;
```

##### User Input
To take user input you can do:

```javascript
let isGay = window.prompt(`Are you gay?`);
```


```html
<label>Something</label>
<input id="somethingBox">
<button id="somethingButton">submit</button>
```

```javascript
document.getElementById("somethingButton").onclick = function() {
	let something = document.getElementById("somethingBox").value;
	// ... idk what else
}
```
to convert from string to number do:

```javascript
let some = Number(thing);
```

const in JS is a normal const
```javascript
const SOMETHING = 0;
```
the uppercassing practice doesn't include const strings

Or we can use :
- [ ] 
in HTML:
```html
<input type="checkbox" id="idkwhat" />
<label for="idkwhat">idk what</label>
```
the `for` means that the checkbox will  be clicked even if you click on the label instead 

Another kind of button is :

```html
<input type="radio", id="idkwhat" name="idkWhatButtons>
```

which is not check but selected among other similar buttons, and we use the name attribute for many radio buttons to group them so you can select only one of them
After that you can do JS shananigans with it:

```javascript
checkbox.checked
sumbit.onclick
```


### If statements
It is precisely like C/C++




## The Math Library

```javascript
Math.PI;
Math.E;

Math.round();
Math.floor();
Math.trunc()
Math.ceil();

Math.pow();
Math.sqrt();
Math.log(); // Ln

Math.sin();
Math.cos();
Math.tan();

Math.abs();
Math.sign();
Math.max();
Math.min();
```

### Random Numbers

```javascript
Math.random() // 0...1
Math.random() * Number // 0...Number
Math.floor(Math.random() * Number) + 1; // 1...Number
Math.floor(Math.random() * (max - min)) + min; // min...max
```