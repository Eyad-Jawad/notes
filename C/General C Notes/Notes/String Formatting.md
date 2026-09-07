Besides (or as well as) the `printf` string formatting ([[Printf()]]), there are ways to format a string itself, not while printing it:

### sprintf

This function is under the `stdio.h` library, and it takes care of the formatting only:

```C

char buf[256];
sprintf(buf, "string %s\n", "messi");

```

### asprintf

This function takes care of the allocation as well as the formatting, you'd do:

```C

#define GNU_SOURCE
#include <stdio.h>

char *buf = nullptr;

int len = asprintf(&buf, "string %s", "messi");
if (len == -1) {
	printf("error occurred");
	free(buf);
	return nullptr;
}

return name;

```

know that you need to `free()` it later after you're done with it, because it's dynamically allocated