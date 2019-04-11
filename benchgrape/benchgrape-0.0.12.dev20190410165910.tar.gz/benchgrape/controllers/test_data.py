from cement import Controller, ex
from cement.utils import fs
import json
from benchgrape.core.db import TestDataMapper
from benchgrape.core.utils import map_benchmark_data


class TestData(Controller):
    class Meta:
        label = 'test-data'
        stacked_type = 'nested'
        stacked_on = 'base'

    @ex(help='Load Test Data from JSON-Config File generated by '
             'chatgrape\'s benchmark_setup command.',
        arguments=[
            (['config_file'], {
                'help': 'Config File exported by ChatGrape\'s '
                        'benchmark_setup command',
                'action': 'store'
            })
        ],
    )
    def load(self):
        fname = fs.abspath(self.app.pargs.config_file)
        self.app.log.info('loading config file from: %s' % fname)

        with open(fname, 'rb') as fhandle:
            config = json.loads(fhandle.read())

        organization, users, groups, private_conversations = map_benchmark_data(
            config
        )

        TestDataMapper(self.app.db, self.app.log).sync_db(
            organization, users, groups, private_conversations
        )

    @ex(help='Purge test data in the BenchGrape DB. '
             'This also reset the internal data structure.')
    def purge(self):
        TestDataMapper(self.app.db, self.app.log).drop_db()
