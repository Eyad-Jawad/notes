This function is used to change the allocated size of a previously allocated memory in C, you can use it to request more memory, or less memory, it copies the data of the pointer you pass into the new address:

```C

#include <stdlib.h>

int *ptr = malloc(sizeof(int));
if (ptr == NULL) return 1;

*ptr = 1;

double *new_ptr = realloc(ptr, sizeof(double));
if (new_ptr == NULL) return 1;

*new_ptr = 1.1;

free(new_ptr);
return 0;

```

You must remeber to `free` the reallocated memory, the first memory is "freed", it can be that it has the same address and you can still acess it, but you should think that it is always gone.