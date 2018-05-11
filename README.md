[![](https://img.shields.io/badge/pypi-0.1.0.1-blue.svg)](https://pypi.python.org/pypi/blackdaemon/) <a href="https://github.com/ambv/black"><img alt="Code style: black" src="https://img.shields.io/badge/code%20style-black-000000.svg"></a>


A daemon to automatically run the Uncompromising Code Formatter [`black`](https://github.com/ambv/black) by watching a directory or file for changes. [Try black online now](https://black.now.sh/).

What is black?
> Black is the uncompromising Python code formatter. By using it, you agree to cede control over minutiae of hand-formatting. In return, Black gives you speed, determinism, and freedom from pycodestyle nagging about formatting. You will save time and mental energy for more important matters.

## Installation

```
pip install blackdaemon
```

## Use
```
blackdaemon <directory or file>
```

## API
```
>> python blackdaemon.py --help
usage: blackdaemon.py [-h] [--recursive | --non-recursive] [--no-run-on-start]
                      [-v] [-q]
                      [path]

positional arguments:
  path               path of file or directory to watch for changes

optional arguments:
  -h, --help         show this help message and exit
  --recursive        recursively watch director for changes (default)
  --non-recursive
  --no-run-on-start  run black only when files change, not on startup.
  -v, --version      print version of blackdaemon and black, then exit
  -q, --quiet        don't emit non-error messages to stderr. Errors are still
                     emitted, silence those with 2>/dev/null
```

## Homepage
[https://github.com/cs01/blackdaemon](https://github.com/cs01/blackdaemon)
