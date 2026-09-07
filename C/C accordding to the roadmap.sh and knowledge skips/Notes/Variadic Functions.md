Variadic functions are functions that accept a varying number of arugments, like `pirntf` and `scanf`
You need to include `stdarg.h` which provides the macros:

| Methods                                                                                             | Description                                                                                                                  |
| --------------------------------------------------------------------------------------------------- | ---------------------------------------------------------------------------------------------------------------------------- |
| [va_start](https://www.tutorialspoint.com/c_standard_library/c_macro_va_start.htm)(va_list ap, arg) | Arguments after the last fixed argument are stored in the va_list.                                                           |
| [va_arg](https://www.tutorialspoint.com/c_standard_library/c_macro_va_arg.htm)(va_list ap, type)    | Each time, the next argument in the variable list va_list and coverts it to the given type, till it reaches the end of list. |
| va_copy(va_list dest, va_list src)                                                                  | This creates a copy of the arguments in va_list                                                                              |
| [va_end](https://www.tutorialspoint.com/c_standard_library/c_macro_va_end.htm)(va_list ap)          | This ends the traversal of the variadic function arguments. As the end of va_list is reached, the list object is cleaned up. |

So, a function would look something like this:

```C

int sum(int n, ...) {
	va_list args;
	int s = 0;
	
	va_start(args, n);
	
	for (int i = 0; i < n; i++) {
		s += va_arg(args, int);
	}
	
	va_end(args);
	
	return s;
}

```

`n` in the function's parameters is the numer of arguments that will be passed