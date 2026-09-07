In the standard package of `pytest`, that's why you typically need the plugin `pytest-asyncio` to make a an async test, which you need to install via `pip` or `uv`:

```Python

import pytest


@pytest.mark.asyncio
async def test_some_async_func():
    assert await some_async_func() == "Result"

```