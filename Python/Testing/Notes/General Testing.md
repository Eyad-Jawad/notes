To make a test you need 3 things, or sometimes 2, first you need the file to start with: `test_`, or end with `_test.py`, otherwise it won't work, second, the test function needs to start with `test` as well, the third thing is not obligatory, but you need to use the keyword `assert`, that checks if a case holds true and crashesh otherwise.
A test can for example run a function to solely check that it doesn't crash, without ever using the keyword `assert`.

```Python

# tests/test_something.py

import pytest # Not necessary in this specific case


def test_something():
    assert some_func() == "Result"


def test_func_no_crash():
    some_func()

```

And then to run the tests, execute:

```Bash

pytest

```

Sometimes you need to add `python -m` before the word `pytest`, I advise you use `uv`:

```Bash

uv run pytest

```

