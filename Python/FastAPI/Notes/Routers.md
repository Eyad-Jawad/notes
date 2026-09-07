A router is dead simple, it allows you to write methods across multiple files, without prompting circular dependency error:

```Python

from fastapi import APIRouter

router = APIRouter()

@router.get("/")
async def get_root():
    return "Ok"

```

Then, where the `app` is located write:

```Python

import module

app = FastAPI()
app.include_router(module.router, tags="router")

```
