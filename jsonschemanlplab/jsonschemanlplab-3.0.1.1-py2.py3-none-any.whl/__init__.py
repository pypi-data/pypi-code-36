"""
An implementation of JSON Schema for Python

The main functionality is provided by the validator classes for each of the
supported JSON Schema versions.

Most commonly, `validate` is the quickest way to simply validate a given
instance under a schema, and will create a validator for you.

"""

from jsonschemanlplab.exceptions import (
    ErrorTree, FormatError, RefResolutionError, SchemaError, ValidationError
)
from jsonschemanlplab._format import (
    FormatChecker,
    draft3_format_checker,
    draft4_format_checker,
    draft6_format_checker,
    draft7_format_checker,
)
from jsonschemanlplab._types import TypeChecker
from jsonschemanlplab.validators import (
    Draft3Validator,
    Draft4Validator,
    Draft6Validator,
    Draft7Validator,
    RefResolver,
    validate,
)

from pkg_resources import get_distribution
__version__ = get_distribution(__name__).version
