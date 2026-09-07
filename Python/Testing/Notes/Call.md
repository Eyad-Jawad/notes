You can find `call` in the built-in `unittest.mock`, it can be used to test for function calls, when a [[Patch|patched function]] or a [[MagicMock|mocked object]], is called more than once, `assert_called_once_with(args)` will not work, so we need `call` to test it:

```Python

from unittest.mock improt MagicMock, call


def test_some_func():
    arg = MagicMock()
    arg.method.side_effect = [1, 2, 3]

    some_func(arg)

    assert arg.method.call_count == 3
    assert arg.method.call_args_list == [
        call(1),
        call(2),
        call(3),
    ]

```

You can also use it with [[Patch]], and [[AsyncMock]], but for the latter you need to substitute the word `call`, with `await`:

```Python

assert args.method.await_count == 3
assert args.method.await_args_list == [...]

```