import socket

class NetcatError(Exception):
    pass

class NetcatTimeout(NetcatError, socket.timeout):
    pass
