# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from blinker import Namespace

namespace = Namespace()

#: Trigerred when a dataset is published
on_dataset_published = namespace.signal('on-dataset-published')
