To hide routes from the auto-generated docs in `FastAPI`, you only need to pass one argument:

```Python

@app.get("/", response_class=HTMLResponse, include_in_schema=False)
def get_root():
	return 1

```

You can notice that I have also passed [[Response Class|response_class=HTMLResponse]], that's because you'd typically hide user targeted routes from the docs, and `HTML` is typically for users.
