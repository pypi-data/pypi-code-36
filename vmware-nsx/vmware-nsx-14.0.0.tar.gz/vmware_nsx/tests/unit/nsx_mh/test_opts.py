# Copyright 2013 VMware, Inc.
#
#    Licensed under the Apache License, Version 2.0 (the "License"); you may
#    not use this file except in compliance with the License. You may obtain
#    a copy of the License at
#
#         http://www.apache.org/licenses/LICENSE-2.0
#
#    Unless required by applicable law or agreed to in writing, software
#    distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
#    WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
#    License for the specific language governing permissions and limitations
#    under the License.
#

import mock
from neutron.tests import base
from oslo_config import cfg
from oslo_utils import uuidutils
import six

from vmware_nsx.api_client import client
from vmware_nsx.api_client import version
from vmware_nsx.common import config  # noqa
from vmware_nsx.common import exceptions
from vmware_nsx.common import sync
from vmware_nsx import nsx_cluster
from vmware_nsx.nsxlib.mh import lsn as lsnlib
from vmware_nsx import plugin as mh_plugin
from vmware_nsx.tests import unit as vmware

BASE_CONF_PATH = vmware.get_fake_conf('neutron.conf.test')
NSX_INI_PATH = vmware.get_fake_conf('nsx.ini.basic.test')
NSX_INI_FULL_PATH = vmware.get_fake_conf('nsx.ini.full.test')
NSX_INI_AGENTLESS_PATH = vmware.get_fake_conf('nsx.ini.agentless.test')
NSX_INI_COMBINED_PATH = vmware.get_fake_conf('nsx.ini.combined.test')
NVP_INI_DEPR_PATH = vmware.get_fake_conf('nvp.ini.full.test')


class NSXClusterTest(base.BaseTestCase):

    cluster_opts = {'default_tz_uuid': uuidutils.generate_uuid(),
                    'default_l2_gw_service_uuid': uuidutils.generate_uuid(),
                    'nsx_user': 'foo',
                    'nsx_password': 'bar',
                    'http_timeout': 25,
                    'retries': 7,
                    'redirects': 23,
                    'nsx_default_interface_name': 'baz',
                    'nsx_controllers': ['1.1.1.1:443']}

    def test_create_cluster(self):
        cluster = nsx_cluster.NSXCluster(**self.cluster_opts)
        for (k, v) in six.iteritems(self.cluster_opts):
            self.assertEqual(v, getattr(cluster, k))

    def test_create_cluster_default_port(self):
        opts = self.cluster_opts.copy()
        opts['nsx_controllers'] = ['1.1.1.1']
        cluster = nsx_cluster.NSXCluster(**opts)
        for (k, v) in six.iteritems(self.cluster_opts):
            self.assertEqual(v, getattr(cluster, k))

    def test_create_cluster_missing_required_attribute_raises(self):
        opts = self.cluster_opts.copy()
        opts.pop('default_tz_uuid')
        self.assertRaises(exceptions.InvalidClusterConfiguration,
                          nsx_cluster.NSXCluster, **opts)


class ConfigurationTest(base.BaseTestCase):

    def setUp(self):
        super(ConfigurationTest, self).setUp()
        # Avoid runs of the synchronizer looping call
        patch_sync = mock.patch.object(sync, '_start_loopingcall')
        patch_sync.start()

    def _assert_required_options(self, cluster):
        self.assertEqual(cluster.nsx_controllers, ['fake_1:443', 'fake_2:443'])
        self.assertEqual(cluster.default_tz_uuid, 'fake_tz_uuid')
        self.assertEqual(cluster.nsx_user, 'foo')
        self.assertEqual(cluster.nsx_password, 'bar')

    def _assert_extra_options(self, cluster):
        self.assertEqual(13, cluster.http_timeout)
        self.assertEqual(12, cluster.redirects)
        self.assertEqual(11, cluster.retries)
        self.assertEqual('whatever', cluster.default_l2_gw_service_uuid)
        self.assertEqual('whatever', cluster.default_l3_gw_service_uuid)
        self.assertEqual('whatever', cluster.nsx_default_interface_name)

    def _get_mh_plugin(self):
        with mock.patch("neutron_lib.rpc.Connection"):
            plugin = mh_plugin.NsxPlugin()
        return plugin

    def test_load_plugin_with_full_options(self):
        self.config_parse(args=['--config-file', BASE_CONF_PATH,
                                '--config-file', NSX_INI_FULL_PATH])
        cfg.CONF.set_override('core_plugin', vmware.PLUGIN_NAME)
        plugin = self._get_mh_plugin()
        cluster = plugin.cluster
        self._assert_required_options(cluster)
        self._assert_extra_options(cluster)

    def test_load_plugin_with_required_options_only(self):
        self.config_parse(args=['--config-file', BASE_CONF_PATH,
                                '--config-file', NSX_INI_PATH])
        cfg.CONF.set_override('core_plugin', vmware.PLUGIN_NAME)
        plugin = self._get_mh_plugin()
        self._assert_required_options(plugin.cluster)

    def test_defaults(self):
        self.assertEqual(5000, cfg.CONF.NSX.max_lp_per_bridged_ls)
        self.assertEqual(256, cfg.CONF.NSX.max_lp_per_overlay_ls)
        self.assertEqual(10, cfg.CONF.NSX.concurrent_connections)
        self.assertEqual('access_network', cfg.CONF.NSX.metadata_mode)
        self.assertEqual('stt', cfg.CONF.NSX.default_transport_type)
        self.assertEqual('service', cfg.CONF.NSX.replication_mode)

        self.assertIsNone(cfg.CONF.default_tz_uuid)
        self.assertEqual('admin', cfg.CONF.nsx_user)
        self.assertEqual('admin', cfg.CONF.nsx_password)
        self.assertEqual(75, cfg.CONF.http_timeout)
        self.assertEqual(2, cfg.CONF.retries)
        self.assertEqual(2, cfg.CONF.redirects)
        self.assertEqual([], cfg.CONF.nsx_controllers)
        self.assertIsNone(cfg.CONF.default_l3_gw_service_uuid)
        self.assertIsNone(cfg.CONF.default_l2_gw_service_uuid)
        self.assertEqual('breth0', cfg.CONF.nsx_default_interface_name)
        self.assertEqual(900, cfg.CONF.conn_idle_timeout)

    def test_load_api_extensions(self):
        self.config_parse(args=['--config-file', BASE_CONF_PATH,
                                '--config-file', NSX_INI_FULL_PATH])
        cfg.CONF.set_override('core_plugin', vmware.PLUGIN_NAME)
        # Load the configuration, and initialize the plugin
        self._get_mh_plugin()
        self.assertIn('extensions', cfg.CONF.api_extensions_path)

    def test_agentless_extensions(self):
        self.config_parse(args=['--config-file', BASE_CONF_PATH,
                                '--config-file', NSX_INI_AGENTLESS_PATH])
        cfg.CONF.set_override('core_plugin', vmware.PLUGIN_NAME)
        self.assertEqual(config.AgentModes.AGENTLESS,
                         cfg.CONF.NSX.agent_mode)
        # The version returned from NSX matter as it has be exactly 4.1
        with mock.patch.object(client.NsxApiClient,
                               'get_version',
                               return_value=version.Version("4.1")):
            with mock.patch.object(lsnlib,
                                   'service_cluster_exists',
                                   return_value=True):
                plugin = self._get_mh_plugin()
                self.assertNotIn('agent',
                                 plugin.supported_extension_aliases)
                self.assertNotIn('dhcp_agent_scheduler',
                                 plugin.supported_extension_aliases)
                self.assertNotIn('lsn',
                                 plugin.supported_extension_aliases)

    def test_agentless_extensions_version_fail(self):
        self.config_parse(args=['--config-file', BASE_CONF_PATH,
                                '--config-file', NSX_INI_AGENTLESS_PATH])
        cfg.CONF.set_override('core_plugin', vmware.PLUGIN_NAME)
        self.assertEqual(config.AgentModes.AGENTLESS,
                         cfg.CONF.NSX.agent_mode)
        with mock.patch.object(client.NsxApiClient,
                               'get_version',
                               return_value=version.Version("3.2")):
            try:
                self._get_mh_plugin()
            except exceptions.NsxPluginException:
                # This is the correct result
                pass
            else:
                self.fail('Expected NsxPluginException exception')

    def test_agentless_extensions_unmet_deps_fail(self):
        self.config_parse(args=['--config-file', BASE_CONF_PATH,
                                '--config-file', NSX_INI_AGENTLESS_PATH])
        cfg.CONF.set_override('core_plugin', vmware.PLUGIN_NAME)
        self.assertEqual(config.AgentModes.AGENTLESS,
                         cfg.CONF.NSX.agent_mode)
        with mock.patch.object(client.NsxApiClient,
                               'get_version',
                               return_value=version.Version("3.2")):
            with mock.patch.object(lsnlib,
                                   'service_cluster_exists',
                                   return_value=False):
                try:
                    self._get_mh_plugin()
                except exceptions.NsxPluginException:
                    # This is the correct result
                    pass
                else:
                    self.fail('Expected NsxPluginException exception')

    def test_agent_extensions(self):
        self.config_parse(args=['--config-file', BASE_CONF_PATH,
                                '--config-file', NSX_INI_FULL_PATH])
        cfg.CONF.set_override('core_plugin', vmware.PLUGIN_NAME)
        self.assertEqual(config.AgentModes.AGENT,
                         cfg.CONF.NSX.agent_mode)
        plugin = self._get_mh_plugin()
        self.assertIn('agent',
                      plugin.supported_extension_aliases)
        self.assertIn('dhcp_agent_scheduler',
                      plugin.supported_extension_aliases)

    def test_combined_extensions(self):
        self.config_parse(args=['--config-file', BASE_CONF_PATH,
                                '--config-file', NSX_INI_COMBINED_PATH])
        cfg.CONF.set_override('core_plugin', vmware.PLUGIN_NAME)
        self.assertEqual(config.AgentModes.COMBINED,
                         cfg.CONF.NSX.agent_mode)
        with mock.patch.object(client.NsxApiClient,
                               'get_version',
                               return_value=version.Version("4.1")):
            with mock.patch.object(lsnlib,
                                   'service_cluster_exists',
                                   return_value=True):
                plugin = self._get_mh_plugin()
                self.assertIn('agent',
                              plugin.supported_extension_aliases)
                self.assertIn('dhcp_agent_scheduler',
                              plugin.supported_extension_aliases)
                self.assertIn('lsn',
                              plugin.supported_extension_aliases)


class OldNVPConfigurationTest(base.BaseTestCase):

    def setUp(self):
        super(OldNVPConfigurationTest, self).setUp()
        # Avoid runs of the synchronizer looping call
        patch_sync = mock.patch.object(sync, '_start_loopingcall')
        patch_sync.start()

    def _assert_required_options(self, cluster):
        self.assertEqual(cluster.nsx_controllers, ['fake_1:443', 'fake_2:443'])
        self.assertEqual(cluster.nsx_user, 'foo')
        self.assertEqual(cluster.nsx_password, 'bar')
        self.assertEqual(cluster.default_tz_uuid, 'fake_tz_uuid')

    def test_load_plugin_with_deprecated_options(self):
        self.config_parse(args=['--config-file', BASE_CONF_PATH,
                                '--config-file', NVP_INI_DEPR_PATH])
        cfg.CONF.set_override('core_plugin', vmware.PLUGIN_NAME)
        with mock.patch("neutron_lib.rpc.Connection"):
            plugin = mh_plugin.NsxPlugin()
            cluster = plugin.cluster
            # Verify old nvp_* params have been fully parsed
            self._assert_required_options(cluster)
            self.assertEqual(3, cluster.http_timeout)
            self.assertEqual(2, cluster.retries)
            self.assertEqual(2, cluster.redirects)
