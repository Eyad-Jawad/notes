`MagicMock` is a class from the built-in `unittest.mock`, it can act as a mocker, as the name suggests, it has every attribute you ask for, and every method you need, of course, the return values are wonky if you don't actually configure it: 

```Python

from unittest.mock import MagicMock


def test_something():
    arg = MagicMock()
    arg.attribute = "xyz"
    arg.method.return_value = "zyx"
    arg.generator.side_effect = [1, 2, 3] # For multiple calls return vallues
    arg.other_method.side_effect = ValueError("Some error") # For errors, to check how they are handled

    some_func(arg)

    arg.method.assert_called_once()
    arg.other_method.assert_not_called_once()
    arg.generator.assert_called_once_with(1)

```

By the way, all the leading methods are `MagicMock` themselves, so if you don't configure something, and the function calls something like `MagicMock.not_configured_method()`, `type(not_configured_method) = MagicMock`.

You can combine it with [[Patch]], [[Call]], and [[AsyncMock]] to create many other things as well.