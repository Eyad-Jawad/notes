### The Test Function

The main, basic, and general way to do testing in Criterion is to include the header and do:

```C
#include <criterion/criterion.h>

Test(suite_name, test_name) {
	.
	.
	.
}

```

### The Functions

There are many functions you could use for testing, but they are all a variant of two ones:

1. `cr_expect`
2. `cr_assert`

The first one will not stop the test if it fails, the other one however, will stop the test if it fails.