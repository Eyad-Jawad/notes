If you want to change something about the `Path` object without creating a new one, or using `rename()` which changes the actual file, you can use `with_`, there are many of them:

```Python

path = path.with_stem("filename")
path = path.with_suffix(".py")
path = paht.with_name = "main.py"

```
