redis in python is fairly straightforward:

```Python

import redis

r = redis.Redis()

key = "Name"
period = 10 # s

current_value = r.incr(key)
r.expire(key, period)

```

That's it for now.