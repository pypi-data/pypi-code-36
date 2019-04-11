""" Helper functions """

import os
import sys
if sys.version_info < (3, 3):
    from collections import Iterable
else:
    from collections.abc import Iterable

__author__ = "Vince Reuter"
__email__ = "vreuter@virginia.edu"

__all__ = ["expandpath", "is_callable_like", "is_collection_like"]


def expandpath(p):
    """
    Expand environment and user variables contained in filesystem path.

    :param str p: Path in which to perform the variable expansion
    :return str: The expansion of the input path
    """
    return os.path.expanduser(os.path.expandvars(p))


def is_callable_like(obj):
    """
    Determine whether an object is like a callable.

    :param object obj: Object to test for apparent callability.
    :return bool: Whether the given object appears to be a callable.

    """
    return isinstance(obj, property) or hasattr(obj, "__call__")


def is_collection_like(obj):
    """
    Determine whether given object appears to be a collection other than string.

    :param object obj: object to inspect as putative collection
    :return bool: whether given object appears to be a collection other than
        a string
    """
    return isinstance(obj, Iterable) and not isinstance(obj, str)
