To compile the tests you need to write all the test files and sources files excluding where the main entry point lies, and add the library flag:

```Bash

gcc -Werror tests/test.c src/source.c -o tests -lcriterion

```

In here, `-Werror` is an example of a flag, and after that is the source files, then at the end the flag of the library