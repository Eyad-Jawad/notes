You use `url_for` to reference to routes and avoid hardcoding them, you can use fastapi function names, or the names you set for some routes.

## For Functions

```Python

@app.get("/route")
def func():
	return 1

```

Then in the `HTML` files:

```HTML

<a href="{{ url_for('func') }}"> something </a>

```

Be careful with the quotes, there another case where two routes share the same function:

```Python

@app.get("/route1)
@app.get("/route2)  # <-- Takes precedence
def func():
	return 1

```

To just avoid cases such as these and make things clear, do pass a `name` to the decorators:

```Python

@app.get("/route1", name="func")  # <-- Now this takes precedence
@app.get("/route2", name="func1)
def func():
	return 1

```

## For Directories

You can also use it for directories on the app, but you must [[Mount Directories|mount]] them first:

```HTML

<a href="{{ url_for('/some_dir', path='another_dir/file.ico') }}></a>

```
