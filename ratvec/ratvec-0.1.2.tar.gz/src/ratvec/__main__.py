# -*- coding: utf-8 -*-

"""Entrypoint module, in case you use `python -m ratvec`.

Why does this file exist, and why ``__main__``? For more info, read:

- https://www.python.org/dev/peps/pep-0338/
- https://docs.python.org/3/using/cmdline.html#cmdoption-m
"""

from ratvec.cli import main

if __name__ == '__main__':
    main()
