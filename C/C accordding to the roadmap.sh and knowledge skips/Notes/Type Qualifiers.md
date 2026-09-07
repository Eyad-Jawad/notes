there are three type qualifiers:
`const`, `volatile`, and `restrict`

in type qualifiers,
you can: `const int A, B;`
you can't: `int a, const B;`

```C

int const *p_ci;      // Pointer to constant int
int const (*p_ci);   // Pointer to constant int
int *const CP_I;     // Constant pointer to int
int (*const CP_I);   // Constant pointer to int
int volatile vint;     // Volatile integer

```

in `const`, variables are placed in a read-only area of the memory, in `volatile` however, the compiler assumes that the variable can be changed at anytime without its knowledge or understanding, so it has to read it each time, `volatile a; // int`.
an item can be both a `const` and `volatile`, which means it cannot be changed by its own program, but other unknown processes can change it

use `volatile` when dealing with interrupts, memory-mapped I/O, or even multithreading.

lastly, `restrict` is a qualifeir for the pointer, it means there's no other pointer that points to this memory location, nor to any of the derived locations, the ones you get from `pointer + 1`, it allows the compiler to optimize, if you do however, point to it, undefinined results may occurr.
an example on where it'd be used:

```C

void test(int* restrict first, int* restrict second, int* val)
{
    *first += *val;
    *second += *val;
}

int main()
{
    int i = 1, j = 2, k = 3;
    test(&i, &j, &k);

    return 0;
}

// Marking union members restrict tells the compiler that
// only z.x or z.y will be accessed in any scope, which allows
// the compiler to optimize access to the members.
union z 
{
    int* restrict x;
    double* restrict y;
};

```


and [[Atomic]], there are also `_Thread_local`, `_Alignas`, `_Noreturn`, and etc.
