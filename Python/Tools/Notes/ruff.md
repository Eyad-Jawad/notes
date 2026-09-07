`ruff` is a linter, that checks for style, potential bugs, and errors according to some rules it has, it generally replaces [[black]], and matches the style output, and being faster, install it via `pip` or `uv`, and to use it:

```Bash

ruff check .
ruff check --fix .

uv ruff check .
uv ruff check --fix .

```

You can also chagne the line length default:

```toml

# pyproject.toml

[tool.ruff]
line-length = 80

```