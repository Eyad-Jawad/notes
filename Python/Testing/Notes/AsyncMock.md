You can find `AsyncMock` in the built-in `unittest.mock`, it is failry similar to [[MagicMock]], but async, some function call async functions, or methods, that's why you need `AsyncMock`, the only difference between `AsyncMock` and [[MagicMock]] is in the `assert` statements:

```Python

from unittest.mock import AsyncMock


@pytest.mark.asyncio 
async def test_some_func():
    arg = AsyncMock()

    """
        After some stuff
    """
    await some_func(arg)

    arg.method.assert_awaited_once()
    arg.other_method.assert_awaited_once_with(1)
    arg.random_method.assert_not_awaited

```

And of course, since you will be calling an `async` function, you need the test to be `async` itself: [[Async Testing]]
As it is the case with [[MagicMock]], all the leading methods are `AsyncMock`