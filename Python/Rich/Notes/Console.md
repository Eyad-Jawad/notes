The console is like the `stdout` stream

## Initialization

```Python

from rich.console import Console

console = Console()

```

## Methods

There are many methods, but these are the most important ones:

```Python

console.print("Hello World") # Literally just a print
console.clear() # Clears the terminal 

```

## Attributes

There are two useful attributes:

```Python

console.height
console.width

```

## String Formatting

You can color strings like this:

```Python

s = "[color]Colored Text[/color]"
s = "[color]Colored Text[/]"
s = "[color on color ]Highlighted Colored Text[/]"
s = "[bold color on color ]Bold Highlighted Colored Text[/]"

```

And so on.