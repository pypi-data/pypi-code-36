#  BSD 3-Clause License
#
#  Copyright (c) 2012, the Sentry Team, see AUTHORS for more details
#  Copyright (c) 2019, Elasticsearch BV
#  All rights reserved.
#
#  Redistribution and use in source and binary forms, with or without
#  modification, are permitted provided that the following conditions are met:
#
#  * Redistributions of source code must retain the above copyright notice, this
#    list of conditions and the following disclaimer.
#
#  * Redistributions in binary form must reproduce the above copyright notice,
#    this list of conditions and the following disclaimer in the documentation
#    and/or other materials provided with the distribution.
#
#  * Neither the name of the copyright holder nor the names of its
#    contributors may be used to endorse or promote products derived from
#    this software without specific prior written permission.
#
#  THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
#  AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
#  IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE ARE
#  DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT HOLDER OR CONTRIBUTORS BE LIABLE
#  FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR CONSEQUENTIAL
#  DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF SUBSTITUTE GOODS OR
#  SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS INTERRUPTION) HOWEVER
#  CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN CONTRACT, STRICT LIABILITY,
#  OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE) ARISING IN ANY WAY OUT OF THE USE


from __future__ import absolute_import

import sys
import traceback

import logbook

from elasticapm.base import Client
from elasticapm.utils import compat
from elasticapm.utils.encoding import to_unicode

LOOKBOOK_LEVELS = {
    logbook.DEBUG: "debug",
    logbook.INFO: "info",
    logbook.NOTICE: "info",
    logbook.WARNING: "warning",
    logbook.ERROR: "error",
    logbook.CRITICAL: "fatal",
}


class LogbookHandler(logbook.Handler):
    def __init__(self, *args, **kwargs):
        if len(args) == 1:
            arg = args[0]
            # if isinstance(arg, compat.string_types):
            # self.client = kwargs.pop('client_cls', Client)(dsn=arg)
            if isinstance(arg, Client):
                self.client = arg
            else:
                raise ValueError(
                    "The first argument to %s must be a Client instance, "
                    "got %r instead." % (self.__class__.__name__, arg)
                )
            args = []
        else:
            try:
                self.client = kwargs.pop("client")
            except KeyError:
                raise TypeError("Expected keyword argument for LoggingHandler: client")
        super(LogbookHandler, self).__init__(*args, **kwargs)

    def emit(self, record):
        self.format(record)

        # Avoid typical config issues by overriding loggers behavior
        if record.channel.startswith("elasticapm.errors"):
            sys.stderr.write(to_unicode(record.message + "\n"))
            return

        try:
            return self._emit(record)
        except Exception:
            sys.stderr.write("Top level ElasticAPM exception caught - failed creating log record.\n")
            sys.stderr.write(to_unicode(record.msg + "\n"))
            sys.stderr.write(to_unicode(traceback.format_exc() + "\n"))

            try:
                self.client.capture("Exception")
            except Exception:
                pass

    def _emit(self, record):
        # If there's no exception being processed,
        # exc_info may be a 3-tuple of None
        # http://docs.python.org/library/sys.html#sys.exc_info
        if record.exc_info is True or (record.exc_info and all(record.exc_info)):
            handler = self.client.get_handler("elasticapm.events.Exception")
            exception = handler.capture(self.client, exc_info=record.exc_info)
        else:
            exception = None

        return self.client.capture_message(
            param_message={"message": compat.text_type(record.msg), "params": record.args},
            exception=exception,
            level=LOOKBOOK_LEVELS[record.level],
            logger_name=record.channel,
            custom=record.extra,
            stack=record.kwargs.get("stack"),
        )
