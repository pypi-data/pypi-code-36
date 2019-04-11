# Copyright (C) 2015-2019 The Software Heritage developers
# See the AUTHORS file at the top-level directory of this distribution
# License: GNU General Public License version 3, or any later version
# See top-level LICENSE file for more information

from celery import current_app
import celery.app.task
from celery.utils.log import get_task_logger

from swh.core.statsd import Statsd


class SWHTask(celery.app.task.Task):
    """a schedulable task (abstract class)

    Current implementation is based on Celery. See
    http://docs.celeryproject.org/en/latest/reference/celery.app.task.html for
    how to use tasks once instantiated

    """

    _statsd = None
    _log = None

    @property
    def statsd(self):
        if self._statsd:
            return self._statsd
        worker_name = current_app.conf.get('worker_name')
        if worker_name:
            self._statsd = Statsd(constant_tags={
                'task': self.name,
                'worker': worker_name,
            })
            return self._statsd
        else:
            return Statsd(constant_tags={
                'task': self.name,
                'worker': 'unknown worker',
            })

    def __call__(self, *args, **kwargs):
        self.statsd.increment('swh_task_called_count')
        with self.statsd.timed('swh_task_duration_seconds'):
            return super().__call__(*args, **kwargs)

    def on_failure(self, exc, task_id, args, kwargs, einfo):
        self.statsd.increment('swh_task_failure_count')

    def on_success(self, retval, task_id, args, kwargs):
        self.statsd.increment('swh_task_success_count')
        # this is a swh specific event. Used to attach the retval to the
        # task_run
        self.send_event('task-result', result=retval)

    @property
    def log(self):
        if self._log is None:
            self._log = get_task_logger(self.name)
        return self._log

    def run(self, *args, **kwargs):
        self.log.debug('%s: args=%s, kwargs=%s', self.name, args, kwargs)
        ret = super().run(*args, **kwargs)
        self.log.debug('%s: OK => %s', self.name, ret)
        return ret
