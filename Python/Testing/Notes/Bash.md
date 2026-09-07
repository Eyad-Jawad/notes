You can use a bash script to run, say, an integration test, and check its return value with a normal python test:

```Pyhton

import subprocess


def test_integration():
    result = subprocess.run(
        ["bash", "path/to/script.sh"], 
        capture_out=True, 
        text=True,
        check=False, # This makes it so it doesn't crash right away if the script doesn't return 0
    )

    assert result.returncode == 0, result.stderr

```

writing `, result.stderr` is a neat little trick that will print the error if this specific line fails.