A fixture in Python-Pytest is a function that can kind of wrap around a test, it can execute code before a test and return a value, or even `yield` that value instead and it can execute code after a test:

## Sync Fixtures

```Python

import pytest


@pytest.fixture
def mock_name():
    name = "Name"

    yield name

    delete name


def test_something(mock_name):
    assert name == "Name

```

Of course this is an extremely simple example, but you get the idea, 

## Async Fixtures

`pytest` does not support async fixtures, or at least the standard package, that's why you typically need `pytest-asyncio` for async fixtures, you also need to intall it via `pip`, or `uv`:

```Python

import pytest
import pytest_asyncio


@pytest_asyncio.fixture
async def mock_name():
    name = await some_async_func()

    return name


@pytest.mark.asyncio
async def test_name(mock_name):
    assert mock_name == "Name"

```

And of course the test needs to be an [[Async Testing]]