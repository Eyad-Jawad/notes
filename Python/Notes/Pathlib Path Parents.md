A `parent` is just the directory above the current one, you can use `parents[i]` to get the i-th parent and avoid a long chain of parent:

```Python

from pathlib import Path


dir = Path(__file__).resolve().parent
higher_dir = dir.parents[2]

```
