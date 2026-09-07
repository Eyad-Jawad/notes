to start do:

```python

from fastapi import FastAPI

app = FastAPI()

@app.get("/")
def get_root():
	return {"Message" : "Hello"}

```

then do this to use it:

```bash

fastapi dev

```

to recieve from the user do:

```python

from fastapi.params import Body

@app.post("/")
def post(payload: dict = Body(...)):
	return {"State" : "recieved"}

```

then we can use cURL to post:

```bash

curl -X POST https://127.0.0.1:8000/ \
	-H "Content-Type: application/json" \
	-d '{"key" : "value"}'
	
```

if you want to ensure the that the user doesn't send anything you don't want them to send, do:

```python

from pydantic import BaseModel

class data(BaesModel):
	name: str
	age: int

@app.post("/")
def post(post: data):
	print(post)
	return {"State" : post.dict()}

```

HTTPS methods:
	CRUD: create, read, update, delete; post, get, put/patch, delete

put changes the enitre thing, patch changes a specific part of it only

to return error code, or status code use this:

```python

from fastapi import Response, status, HTTPException

...
def post(..., response: Repsonse)
	if does_not_exist:
		response.status_code = status.HTTP_404_NOT_FOUND
		# Or:
		raise HTTPException(status.HTTP_404_NOT_FOUND, detail="Lol")

```

and in functions the status code should be matching the operation, and to do that you do:

```python 

@app...(..., status_code=HTTP_201_CREATED)
def post(...)

```

and it'll return that status code on successs

in fastapi delete method, you'd return status code 204 from the arguments, and you'd use response for that as well 