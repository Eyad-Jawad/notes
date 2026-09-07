Rate limits in `FastAPI` calls a function that has internal logs, if the logs say a user requested more than the limit, an error is raised. We can use [[Redis]] for this, alongside some basic code:

```Python

import time
import redis

from fastapi import HTTPException, Request, status

r = redis.Redis()

def rate_limiter(
    limit: int = 30,
    window: int = 60,  # seconds
):
    async def dependency(request: Request):
        api_key = request.headers.get("access_key") # if the user has some kind of key
        identifier = api_key or ( # else provide a fallback: IP address
            request.client.host if request.client else None # Which can be None
        )
        if identifier is None:
            raise HTTPException(
                status_code=status.HTTP_401_UNAUTHORIZED,
                detail="User has no ip or token.",
            )

        now = int(time.time())
        window_start = now - (now % window)

        key = f"rl:{identifier}:{window_start}"
        current = r.incr(key)

        if current == 1:
            r.expire(key, window)

        elif current > limit:
            raise HTTPException(
                status_code=status.HTTP_429_TOO_MANY_REQUESTS,
                detail="Rate limit exceeded, please try again later.",
            )

    return dependency

```

And to use the function above:

```Python

from fastapi import Depends


app.get("/", dependencies=[Depends(rate_limiter())])

```