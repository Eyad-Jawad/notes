To do that in C you do:

```C
#include <sys/type.h>
#include <sys/stat.h>
#include <errno.h>

if (mkdir("direcory", 0755) == -1) {
	if (errno == EEXIST) {
		printf("The directory already exists\n");
	} else {
		perror("mkdir");
	}
}

```

`0755` is the mode of the directory, which I think was write, read, and execute, for the errors, there are many else but it is not quite relavent at the moment