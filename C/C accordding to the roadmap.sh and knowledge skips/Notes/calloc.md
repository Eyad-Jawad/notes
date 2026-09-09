`calloc()` is like malloc but it takes `amount`, as well as `size`, the latter is the size of each chunk of `amount`, it also initializes the allocated memory to `0`:

```C

#include <stdio.h>
#include <stdlib.h>

int *x = calloc(1, sizeof(int));
if (x == NULL) return 1;

printf("%d\n", *x); // will print 0
free(x);

```
