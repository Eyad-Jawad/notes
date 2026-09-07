In C, I have come to know the hard way that something like this:

```C

int *x; // 0x00
int *y = x + 1; // 0x04

```

Now you might ask why is `+ 1` adds 4? because the size of an `int` is 4, I dunno that's how it is.
To add 1 only you can cast `char *` or `void *` onto it and then do the increment:

```C

int *x;
int *y = (void *) x + 1;

```

but there's another reason why that won't work, which is [[Memory Alignment]]