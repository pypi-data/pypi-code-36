from __future__ import absolute_import
from __future__ import division
from __future__ import print_function
from __future__ import unicode_literals

import logging

import rasa_nlu_gao.version

logging.getLogger(__name__).addHandler(logging.NullHandler())

__version__ = rasa_nlu_gao.version.__version__
