This is about RegEx in javascript, on w3schools

RegExp are be used for:
- Text searching
- Text replacing
- Text validation

###### RegEx Syntax
`/pattern/modifier flags;`


![[Pasted image 20260506095003.png]]

```javascript
let idx = str.search(/something/);
let strs = str.match(/something/);
let str2 = str.replace(/something/, "another thing");
```

There's also RegEx alteration, which is simply or ( | ):
```javascript
let idx = str.search(/something|anotherThing|idk/);
```
##### Flags
| Flag | Description                        |
| ---- | ---------------------------------- |
| /g   | Performs a global match (find all) |
| /i   | Performs case-insensitive matching |
| /u   | Enables Unicode support (new 2015) |

![[Pasted image 20260506210213.png]]

```javascript
let ans = str.match(/lol/g);
```
##### Metacharacters 
They are characters with a special meaning.

```
\d : Matches Digits
\D : Matches non-numeric characters
\w : Matches Words (characters, numbers, and underscores)
\W : Matches characters other than the ones above
\s : Matches Spaces
\S : Matches non-space characters
```

###### Quantifiers

```
x*   : Matches zero or more occurrences of x
x+   : Matches one or more occurrences of x
x?   : Matches zero or one occurrences of x
x{n} : Matches n occurences of x
```

`{x, y}` means it occurs `n` times where `n` is in the range of `x, y`
if you do `{n, }` it means that a character must occur n times at least
`{, n}` this is clear I think

`.*x` this is called greedy matching, it'll match everything that ends with x
`.*?x` this is called lazy matching, it'll match the first thing that ends with x only
##### Assertions 
![[Pasted image 20260506100255.png]]
 
these check like, if a string starts with something for `^`, or if it ends with something for `$`, 

if you do `[^xy]` then it'll find everything except for x or y
if you do `^[xy]` it means x or y in the beggining of the character

`$` will check for strings at the end of the expression or string

`x(?=y)` means match x that comes before y
`x(?!y)` means match x that doesn't come beofre y
`(?<=y)x` means match x that comes after y
`(?<!y)x` means match x that doesn't come after y


##### Characters Classes
![[Pasted image 20260506100647.png]]

`[.]` means select every character

##### Grouping
we use `()` for grouping expressions, for many reasons, one reason is referencing, which is like making a variable of that group:
```RegEx
/(lol)-\1 (lmao)-\2/
```
this will match `lol-lol lmao-lmao`, notice that we used `\1` and `\2` as if they were variables

you can prevent capturing by writing `?:` at the beggining:
```RegEx
/(?:lol)/
```

you can use what's called a `pipe character` or simply `|`, with grouping, which from the looks of it is `or`, you can use it without grouping but I don't understand how that works

to use characters that mean something in RegEx, use `\` before them: `\+`, etc.







































