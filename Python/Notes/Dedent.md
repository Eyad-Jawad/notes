Dedent is used in Python to remove tabs from multiline strings:

```Python

from textwrap import dedent

s = dedent("""
	A string
	that is multi-line.
	- Eyad.
""")

print(s)

```

Output:

```Bash

A string
that is multi-line.
- Eyad

```

Without dedent the output would be:

```Bash

	A string
	that is multi-line.
	- Eyad

```

