In GNU C you can do this:

```C

switch (x) {
	case 1 ... 5:
		print("In range of 1...5\n");
		break
	default:
		print("dunno");
}
```