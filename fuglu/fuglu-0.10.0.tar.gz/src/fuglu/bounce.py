# -*- coding: UTF-8 -*-
#   Copyright 2009-2019 Oli Schacher, Fumail Project
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
# http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.
#

import smtplib
import logging
import os
import email
import sys
from email.utils import formatdate, make_msgid
from email.header import Header
import socket

from fuglu.shared import apply_template
from fuglu.stringencode import force_bString


class Bounce(object):

    """Send Mail (Bounces)"""

    def __init__(self, config):
        self.logger = logging.getLogger('fuglu.bouncer')
        self.config = config

    def _add_required_headers(self, recipient, messagecontent):
        """add headers required for sending automated mail"""

        if sys.version_info > (3,):
            # Python 3 and larger
            # Use bytes so message_from_bytes will not screw around with
            # the encoding
            msgrep = email.message_from_bytes(force_bString(messagecontent))
        else:
            # Python 2.x
            msgrep = email.message_from_string(force_bString(messagecontent)) # byte-encode otherwise older python (<= 2.6)
                                                                              # will screw up the message because it assumes
                                                                              # a non-encode bytes string as input.
        msgrep.set_charset("utf-8") # define unicode because the messagecontent is unicode

        if not 'to' in msgrep:
            msgrep['To'] = Header("<%s>" % recipient).encode()

        if not 'From' in msgrep:
            msgrep['from'] = Header(
                "<MAILER-DAEMON@%s>" % socket.gethostname()).encode()

        if not 'auto-submitted' in msgrep:
            msgrep['auto-submitted'] = Header('auto-generated').encode()

        if not 'date' in msgrep:
            msgrep['Date'] = formatdate(localtime=True)

        if not 'Message-id' in msgrep:
            msgrep['Message-ID'] = make_msgid()

        return msgrep.as_string()

    def send_template_file(self, recipient, templatefile, suspect, values):
        """Send a E-Mail Bounce Message

        Args:
            recipient    (str):  Message recipient (bla@bla.com)
            templatefile (str): Template to use
            suspect      (fuglu.shared.Suspect) suspect that caused the bounce
            values            :Values to apply to the template. ensure all values are of type <str>

        If the suspect has the 'nobounce' tag set, the message will not be sent. The same happens
        if the global configuration 'disablebounces' is set.
        """

        if not os.path.exists(templatefile):
            self.logger.error(
                'Template file does not exist: %s' % templatefile)
            return

        with open(templatefile) as fp:
            filecontent = fp.read()

        self.send_template_string(recipient, filecontent, suspect, values)

    def send_template_string(self, recipient, templatecontent, suspect, values):
        """Send a E-Mail Bounce Message

        If the suspect has the 'nobounce' tag set, the message will not be sent. The same happens
        if the global configuration 'disablebounces' is set.

        Args:
            recipient       (unicode or str) : Message recipient (bla@bla.com)
            templatecontent (unicode or str) : Template to use
            suspect         (fuglu.shared.Suspect) : suspect that caused the bounce
            values       : Values to apply to the template
        """
        if suspect.get_tag('nobounce'):
            self.logger.info(
                'Not sending bounce to %s - bounces disabled by plugin' % recipient)
            return

        message = apply_template(templatecontent, suspect, values)
        try:
            message = self._add_required_headers(recipient, message)
        except Exception as e:
            self.logger.warning(
                "Bounce message template could not be verified: %s" % str(e))

        self.logger.debug('Sending bounce message to %s' % recipient)
        fromaddress = "<>"
        self._send(fromaddress, recipient, message)

    def _send(self, fromaddress, toaddress, message):
        """really send message"""
        if self.config.getboolean('main', 'disablebounces'):
            self.logger.warning(
                'Bounces are disabled in config - not sending message to %s' % toaddress)
            return
        smtpServer = smtplib.SMTP(self.config.get('main','bindaddress'), self.config.getint('main', 'outgoingport'))
        helo = self.config.get('main', 'outgoinghelo')
        if helo.strip() == '':
            import socket
            helo = socket.gethostname()
        smtpServer.helo(helo)
        smtpServer.sendmail(fromaddress, toaddress, message)
        smtpServer.quit()
