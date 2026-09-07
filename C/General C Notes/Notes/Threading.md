You'd use the library `pthread.h`:

```C
#define THREAD_COUNT 4

...

pthread_t threads[THREAD_COUNT];
for (int i = 0; i < THREAD_COUNT; i++) {
	pthread_create(&thread[i], nullptr, function, arguments);
}

for (int i = 0; i < THREAD_COUNT; i++) {
	pthread_join(thread[i], nullptr); // wait for them to terminate
}

```

The function should have a return type of `void *` and returns `NULL`, and you'd use [[Atomic]] with threads and stuff, and btw to set a condition on which the thread gets terminated do:

```C

#define TASK_COUNT x

...

if (someVariable >= TASK_COUNT) {
	return NULL;
}

```

The function should look something like this:

```C

void *function(void *args) {... return NULL;}

```