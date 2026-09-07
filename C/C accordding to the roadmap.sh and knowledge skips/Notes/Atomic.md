[this](https://andrewjohnson4.substack.com/p/understanding-_atomic-types-in-c?utm_campaign=post-expanded-share&utm_medium=web) is actually quite the good read on this subject matter. 

then we have `_Atomic`
available in `stdatomic.h`
can be used as a: 
type specifier `_Atomic (type-name)`
type qualifier `_Atomic type-name`

atomic operations are indivisible and uninterruptable operations, means that they are guarnteed to be completed and won't be interruptted by other threads, it has some unique functions that you can use to manipulate them, like `atomic_fetch_add`, and others

then atomic, there are two ways to declare an atomic, btw it's used to avoid race condition by threads

```C

_Atomic int x;
atomic_int x;

```

both ways are valid
and it really is meant to be used with threads, that's why you won't understand it otherwise

```C

_Atomic(int) *ptr; // use this to say that the pointer points to an atomic int
				   // and that the pointer is not an atomic itself

```


C11 provides several atomic operations in the `<stdatomic.h>` header:
- `atomic_store()` and `atomic_load()` — For storing and loading values atomically.
- `atomic_fetch_add()` and `atomic_fetch_sub()` — For atomic addition and subtraction.
- `atomic_compare_exchange_strong()` and `atomic_compare_exchange_weak()` — For atomic compare-and-swap

example of using `atomic_compare_exchange_strong()`:

```C

_Atomic int value = 3;
int expected = 3;
int desired = 12;

if(atomic_compare_exchange_strong(&value, &expected, desired)) {
	printf("Value updated to %d\n", value);
} else {
	printf("Failed to update value, value is %d\n", value);
}

```

`atomic_compare_exchange_strong()` checks if `value` is equal to `expected`. If true, it updates `value` to `desired`. This is useful for implementing lock-free algorithms.

Atomic operations in C11 also support memory ordering, which controls how operations on memory are perceived by other threads. The following memory orders are available:
- `memory_order_relaxed`
- `memory_order_consume`
- `memory_order_acquire`
- `memory_order_release`
- `memory_order_acq_rel`
- `memory_order_seq_cst`

EX: `atomic_store_exiplicit(&x, 1, memory_order_release);`