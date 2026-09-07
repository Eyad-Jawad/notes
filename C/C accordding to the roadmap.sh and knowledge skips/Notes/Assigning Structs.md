You can assign the struct values in many ways:

```C

// zero initilaization
struct something x = {0}; // assign everything to 0
// positional initilaization
struct something y = {1, 2, "something"}; // assign attributes
// designated initilaization
struct something z = {
	.x = 1,
	.y = 2,
	.z = "something",
};

```
