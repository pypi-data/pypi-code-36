import getpass
import os
import platform
import socket
import sys


is_platform_windows = platform.system().lower() == 'windows'

if is_platform_windows:
    import lib_registry


def get_hostname():
    # type: () -> str
    """
    :returns: fqdn hostname lowercase

    >>> result = get_hostname()
    >>> assert len(result) > 1

    """

    if get_is_platform_windows_wine():  # for wine get hostname not via IP Adress - would give name of the host
        # noinspection PyBroadException
        try:
            _hostname = lib_registry.get_value(key_name=r'HKLM\System\CurrentControlSet\Control\ComputerName',
                                               value_name='ComputerName')
        except Exception:
            _hostname = os.getenv('COMPUTERNAME')  # max 15 Zeichen
    else:
        _hostname = socket.gethostbyaddr(socket.gethostname())[0]

    _hostname = _hostname.lower()
    return _hostname


def get_hostname_short():
    # type: () -> str
    """
    :returns: hostname lowercase

    >>> result = get_hostname_short()
    >>> assert len(result) > 1

    """

    _hostname = get_hostname()
    _hostname_short = _hostname.split('.', 1)[0]
    return _hostname_short


def get_system():
    # type: () -> str
    """
    :returns: darwin, linux, windows, windows_xp, windows_wine

    >>> result = get_system()
    >>> possible_results = ['darwin', 'linux', 'windows', 'windows_xp', 'windows_wine', 'windows_wine_xp']
    >>> assert result in possible_results
    """
    if not is_platform_windows:
        return platform.system().lower()
    else:
        _is_platform_windows_xp = get_is_platform_windows_xp()
        _is_platform_windows_wine = get_is_platform_windows_wine()
        if _is_platform_windows_xp and not _is_platform_windows_wine:
            return 'windows_xp'
        elif _is_platform_windows_xp and _is_platform_windows_wine:
            return 'windows_wine_xp'
        elif _is_platform_windows_wine and not _is_platform_windows_xp:
            return 'windows_wine'
        else:
            return 'windows'


def get_username():
    # type: () -> str
    """
    :returns: username lowercase

    >>> username = get_username()
    >>> assert len(username) > 1

    """
    _username = getpass.getuser().lower()
    return _username


def get_is_platform_windows():
    """
    >>> result = get_is_platform_windows()
    """

    if platform.system().lower() == 'windows':
        return True
    else:
        return False


def get_is_platform_windows_xp():
    # type: () -> bool

    if is_platform_windows:
        release = platform.release().lower()
        if release == 'xp':
            return True
        else:
            return False


def get_is_platform_windows_wine():
    # type: () -> bool
    """
    >>> result = get_is_platform_windows_wine()

    """

    if is_platform_windows:
        _is_platform_windows_wine = lib_registry.key_exist(r'HKEY_LOCAL_MACHINE\Software\Wine')
    else:
        _is_platform_windows_wine = False
    return _is_platform_windows_wine


def get_is_python_2():
    # type: () -> bool
    """
    >>> result = get_is_python_2()

    """

    if sys.version_info < (3, 0):
        return True
    else:
        return False


def get_path_userhome():
    """
    >>> result = get_path_userhome()
    >>> assert len(result) > 1

    """

    s_userhome = os.path.realpath(os.path.expanduser("~"))
    return s_userhome


is_platform_windows = get_is_platform_windows()
is_platform_linux = platform.system().lower() == 'linux'
is_platform_darwin = platform.system().lower() == 'darwin'
is_platform_posix = not is_platform_windows
is_platform_windows_xp = get_is_platform_windows_xp()
is_platform_windows_wine = get_is_platform_windows_wine()
system = get_system()  # 'darwin', 'linux', 'windows', 'windows_xp', 'windows_wine', 'windows_wine_xp'
username = get_username()
hostname = get_hostname()
hostname_short = get_hostname_short()
is_python2 = get_is_python_2()
is_python3 = not is_python2
path_userhome = get_path_userhome()
