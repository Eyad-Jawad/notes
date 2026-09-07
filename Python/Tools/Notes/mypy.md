`mypy` is a static type checker, means it doesn't execute the prorgam while checking for types, it will not allow type casting to the same variable, redefinitions, or wrong type hints, to you use it you have to install it via `pip` or `uv`.

```bash

mypy .
uv run mypy .

```

### Some Errors

Sometimes if some import type when immmported will cause porblems, you can do:

```Python

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    import module

```

### pyproject.toml Configuration

You can configure it to target a specific version:

```toml

pyproject.toml:

[tool.mypy]
python_version = "3.11"

```
