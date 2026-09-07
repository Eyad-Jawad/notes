Black is a format checker, and a formatter as well, which means it only checks for style, it follows some `PEP 8` rules, rewrites the lines to make them shorter, and who knows what, anyway, there are many ways you can use it:

```Bash

black .
black --check .

uv run black .
uv run black --check . 

```

Of course, that is after you've installed it through `pip` or `uv`, if it is the latter, add it as a dev dependency:

```Bash

uv add --dev black

```

There isn't much to configure, but you can change the line length, the default is `88`, and the target version (newer targer versions may break compatibility with older versions)

```toml

# pyproject.toml

[tool.black]
line-length = 80
targer-version = ["py311"]

```