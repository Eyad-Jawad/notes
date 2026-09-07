Enums are declared as structs in C, other than that they have the same features as C++ enums:

```C

typedef enum optional_name_here {
	FIRST,
	SECOND,
	FOURTH = 4,
	FIFTH,
} names;

printf("First: %d\n", FIRST);

```
