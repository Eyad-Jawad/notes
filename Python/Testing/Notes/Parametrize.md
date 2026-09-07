`parametrize`, as the name suggests, parametrizes the parametrize of a test, so you can make many tests of one test only:

```Python

import pytest


@pytest.mark.parametrize(
    "input, output",
    [
        ("1", "2"), # This can be any iterable
        ("2", "1"),
    ]
)
def test_some_func(input, output):
    assert some_func(input) == output

```
