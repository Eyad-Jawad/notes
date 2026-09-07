It is a tool that reports the coverage of tests in `pytest`, to use it you have to install `pytest-cov` via `pip` or `uv`, then you can configure it in `pyproject.toml`:

```toml

[tool.pytest.ini_options]
testpaths = ["src/tests"]
addopts = "--cov=."

[tool.coverage.run]
source = ["."]
omit = ["src/tests/*"]

```
