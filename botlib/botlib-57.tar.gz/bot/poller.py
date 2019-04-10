""" polling based handler. """

import os
import select

from obj.base import Dotted
from obj.handler import Handler
from obj.tasks import launch
from obj.utils import get_name

class ENOTIMPLEMENTED(Exception):
    pass

class Poller(Handler):

    def __init__(self):
        super().__init__()
        self._fds = []
        self._poll = select.epoll()
        self._stopped = False
        self.resume = Dotted()

    def events(self):
        self._poll.poll()
        yield self.get_event()

    def get_event(self):
        raise ENOTIMPLEMENTED

    def register_fd(self, fd):
        if "fileno" in dir(fd):
            fd = fd.fileno()
        self._poll.register(fd)
        self._fds.append(fd)
        self.resume.fd = fd
        os.set_inheritable(self.resume.fd, os.O_RDWR)

    def resume(self):
        if not self.resume.fd:
             raise ERESUME
        self._poll = select.epoll.fromfd(self.resume.fd)

    def loop(self):
        while not self._stopped:
            for event in self.events():
                if not event:
                    self._stopped = True
                    break
                self.put(event)
        self.stop()

    def register(self, bot):
        self.register_fd(bot)

    def start(self):
        self._stopped = False
        super().start()
        launch(self.work)

    def stop(self):
        for fd in self._fds:
            self.unregister_fd(fd)

    def unregister_fd(self, fd):
        if fd in self._fds:
            self._fds.remove(fd)
        try:
            self._poll.unregister(fd)
        except (PermissionError, FileNotFoundError):
            pass
