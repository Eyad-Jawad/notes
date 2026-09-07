It is a function that returns a pointer to the first occurrence of the provided string

```C

char *ptr = strstr(string, "something");
if (ptr == NULL) {
	printf("The string wasn't found");
}

```