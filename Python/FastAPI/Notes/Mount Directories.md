To use files/directories that are independent from the app, but are needed:

```Python

app.mount("/file", name="app")

```

And in case they are static files:

```Python

from fastapi.staticfiles import StaticFiles

app.mount("/dir", StaticFiles(directory="static"), name="static")
```