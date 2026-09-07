You can find `patch` in the built-in `unittest.mock`, `patch` is used to patch functions, as the name suggests, as well as variables, you can use it to modify the return value of some functions, or change the value of some values for some reason:

```Python

from unittest.mock improt patch


@patch("package.module.function")
def test_some_func(patched_function):
    patched_function.return_value = 1

    some_func()

    patched.function.assert_called_once()

```

If you do `print(type(patched_function))` it will print [[MagicMock]], so you can use whatever you want with it, another way to use `patch` is as a context manager:

```Python

from unittest.mock improt patch


def test_some_func():
    with patch("package.module.function") as patched_function:
        patched_function.return_value = 1

        some_func()

        patched.function.assert_called_once()

```

To achieve [[Async Testing]], you just need to supply one argument to `patch`:

```Python

import pytest

from unittest.mock improt patch, AsyncMock


@pytest.mark.asyncio
@patch("package.module.function", new_callable=AsyncMock)
async def test_some_func(patched_function):
    patched_function.return_value = 1

    await some_func()

    patched.function.assert_awaited_once()

```

As you can see, its type is [[AsyncMock]].

You can also pathc variable:

```Python

@patch("module.variable", "New value")
def test_some_func():
    ...

```

### Important Note

If a module imports a function like this:

```Python

from package import module

module.function

```

you `patch` it like this:

```Python

@patch("package.module.functin")

```

However, if a module imports a function like this:

```Python

# file.py

from package.module import function

function()

```

You `patch` it like this:

```Python

@patch("file.function")

```

One last thing, if you use more than one patch the close the patching line to the function, the close it is to be the first argument:

```Python

@patch("file.function1")
@patch("file.function2")
def test_some_func(func2, func2):
    ...

```

And if you want to pass [[Fixtures]] as well, you need to put them at the end of the arguments:

```Python

@patch("file.function1")
@patch("file.function2")
def test_some_func(func2, func2, fixture1, fixture2):
    ...


```