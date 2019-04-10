from __future__ import absolute_import

import io
import os

from pip._vendor import pytoml, six

from pip._internal.exceptions import InstallationError
from pip._internal.utils.typing import MYPY_CHECK_RUNNING

if MYPY_CHECK_RUNNING:
    from typing import Any, Tuple, Optional, List  # noqa: F401


def _is_list_of_str(obj):
    # type: (Any) -> bool
    return (
        isinstance(obj, list) and
        all(isinstance(item, six.string_types) for item in obj)
    )


def load_pyproject_toml(
    use_pep517,  # type: Optional[bool]
    pyproject_toml,  # type: str
    setup_py,  # type: str
    req_name  # type: str
):
    # type: (...) -> Optional[Tuple[List[str], str, List[str]]]
    """Load the pyproject.toml file.

    Parameters:
        use_pep517 - Has the user requested PEP 517 processing? None
                     means the user hasn't explicitly specified.
        pyproject_toml - Location of the project's pyproject.toml file
        setup_py - Location of the project's setup.py file
        req_name - The name of the requirement we're processing (for
                   error reporting)

    Returns:
        None if we should use the legacy code path, otherwise a tuple
        (
            requirements from pyproject.toml,
            name of PEP 517 backend,
            requirements we should check are installed after setting
                up the build environment
        )
    """
    has_pyproject = os.path.isfile(pyproject_toml)
    has_setup = os.path.isfile(setup_py)

    if has_pyproject:
        with io.open(pyproject_toml, encoding="utf-8") as f:
            pp_toml = pytoml.load(f)
        build_system = pp_toml.get("build-system")
    else:
        build_system = None

    # The following cases must use PEP 517
    # We check for use_pep517 being non-None and falsey because that means
    # the user explicitly requested --no-use-pep517.  The value 0 as
    # opposed to False can occur when the value is provided via an
    # environment variable or config file option (due to the quirk of
    # strtobool() returning an integer in pip's configuration code).
    if has_pyproject and not has_setup:
        if use_pep517 is not None and not use_pep517:
            raise InstallationError(
                "Disabling PEP 517 processing is invalid: "
                "project does not have a setup.py"
            )
        use_pep517 = True
    elif build_system and "build-backend" in build_system:
        if use_pep517 is not None and not use_pep517:
            raise InstallationError(
                "Disabling PEP 517 processing is invalid: "
                "project specifies a build backend of {} "
                "in pyproject.toml".format(
                    build_system["build-backend"]
                )
            )
        use_pep517 = True

    # If we haven't worked out whether to use PEP 517 yet,
    # and the user hasn't explicitly stated a preference,
    # we do so if the project has a pyproject.toml file.
    elif use_pep517 is None:
        use_pep517 = has_pyproject

    # At this point, we know whether we're going to use PEP 517.
    assert use_pep517 is not None

    # If we're using the legacy code path, there is nothing further
    # for us to do here.
    if not use_pep517:
        return None

    if build_system is None:
        # Either the user has a pyproject.toml with no build-system
        # section, or the user has no pyproject.toml, but has opted in
        # explicitly via --use-pep517.
        # In the absence of any explicit backend specification, we
        # assume the setuptools backend, and require wheel and a version
        # of setuptools that supports that backend.
        build_system = {
            "requires": ["setuptools>=40.2.0", "wheel"],
            "build-backend": "setuptools.build_meta",
        }

    # If we're using PEP 517, we have build system information (either
    # from pyproject.toml, or defaulted by the code above).
    # Note that at this point, we do not know if the user has actually
    # specified a backend, though.
    assert build_system is not None

    # Ensure that the build-system section in pyproject.toml conforms
    # to PEP 518.
    error_template = (
        "{package} has a pyproject.toml file that does not comply "
        "with PEP 518: {reason}"
    )

    # Specifying the build-system table but not the requires key is invalid
    if "requires" not in build_system:
        raise InstallationError(
            error_template.format(package=req_name, reason=(
                "it has a 'build-system' table but not "
                "'build-system.requires' which is mandatory in the table"
            ))
        )

    # Error out if requires is not a list of strings
    requires = build_system["requires"]
    if not _is_list_of_str(requires):
        raise InstallationError(error_template.format(
            package=req_name,
            reason="'build-system.requires' is not a list of strings.",
        ))

    backend = build_system.get("build-backend")
    check = []  # type: List[str]
    if backend is None:
        # If the user didn't specify a backend, we assume they want to use
        # the setuptools backend. But we can't be sure they have included
        # a version of setuptools which supplies the backend, or wheel
        # (which is neede by the backend) in their requirements. So we
        # make a note to check that those requirements are present once
        # we have set up the environment.
        # This is quite a lot of work to check for a very specific case. But
        # the problem is, that case is potentially quite common - projects that
        # adopted PEP 518 early for the ability to specify requirements to
        # execute setup.py, but never considered needing to mention the build
        # tools themselves. The original PEP 518 code had a similar check (but
        # implemented in a different way).
        backend = "setuptools.build_meta"
        check = ["setuptools>=40.2.0", "wheel"]

    return (requires, backend, check)
