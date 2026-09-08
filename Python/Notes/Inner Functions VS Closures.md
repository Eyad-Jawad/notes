An inner function is a function defined + executed inside another function, while a closure is a function that returns an inner function:

```Python

# Normal inner-outer function relationship
def outer():
	name = "scope to function only"
	
	def inner():
		print(f"Good name: {name}")
		
	inner()

# Closure
def outer():
	name = "scope to function only"
	
	def inner():
		print(f"Good name: {name}")
		
	return inner

```

in the first example, calling the outer function will call the inner function, in the second example however, calling the outer function will return the inner function, where you'll call the retunr value to get an output:

```Python

var = outer()

var() # terminal: Good name: scope to function only

```

A closure in this case is useful, becaue it'll remember variables and things from the outer function, while the first case is just a scope case (to my knowledge so far), a closure can also update variables from the outer scope even after the outer function has returned.
A closure is used in a factory pattern as well.
You can use `lambda` to make a closure as well, where the return value of the outer function is the `lambda` function.
To update a variable that points to an immutable variable you should use the `nonlocal` keyword:

```Python

def outer():
	def closure():
		nonlocal count
		count += 1
		return count
		
	count = 1  # yes you can do this, 
			   # define a function after the closure 
			   # and the closure can very well remember it
			   
	return closure

```

You can also achive encapsulation using closures:

```Python

def Stack():
	_items = []
	
	def push(item):
		_items.append(item)
		
	def pop():
		return _item.pop()
		
	def closure():
		pass
	
	closure.push = push
	closure.pop = pop
	
	return closure

s = Stack()
s.push(1)
print(s.pop())

print(s._items) # ERROR!

```

The same as a class would let you be able to access `_items`, you could still access it though:

```Python

print(Stack.push.__closure__[0].cell_contents)

```

you can implement `__call__()` in classes to get the same function as a closure
