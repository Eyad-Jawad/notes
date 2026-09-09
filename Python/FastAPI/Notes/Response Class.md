You can use `response_class` in  `FastAPI` to tell it how to contruct the return value, the default is `json`, but you can also return html:

```Python

from fastapi.responses import HTMLResponse


@app.get("/")
def get_root():
	return "<h1>Hi</h1>"

```
