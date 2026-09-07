Unions are exactly like struct, only you use the keyword `union` instead of `struct`, unions are variables that share the same address in memory, which means a union can hold either one but not both at the same time:

```C

typedef union optional_name {
	int x;
	unsigned int y;
} name;


name obj = {.x = 1};
printf("name: %d\n", obj.x);

```

know that they can lead to undefinined behaivor
