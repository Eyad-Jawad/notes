If you want two routes to return the same content, like the `/` and and some `/root` you'd do:

```Python

@app.get("/")
@app.get("/root")
def get_root():
	return 1

```