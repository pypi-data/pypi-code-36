# Copyright 2015 VMware, Inc.  All rights reserved.
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

from neutron.db import securitygroups_db
from neutron_lib.callbacks import registry
from neutron_lib import context as neutron_context
from neutron_lib.db import api as db_api
from oslo_log import log as logging

from vmware_nsx.db import db as nsx_db
from vmware_nsx.db import nsx_models
from vmware_nsx.extensions import providersecuritygroup as provider_sg
from vmware_nsx.extensions import securitygrouplogging as sg_logging
from vmware_nsx.plugins.nsx_v3 import utils as plugin_utils
from vmware_nsx.shell.admin.plugins.common import constants
from vmware_nsx.shell.admin.plugins.common import formatters
from vmware_nsx.shell.admin.plugins.common import utils as admin_utils
from vmware_nsx.shell.admin.plugins.nsxv3.resources import utils as v3_utils
from vmware_nsx.shell import resources as shell
from vmware_nsxlib.v3 import exceptions as nsx_lib_exc
from vmware_nsxlib.v3 import nsx_constants as consts
from vmware_nsxlib.v3 import security

LOG = logging.getLogger(__name__)


class NeutronSecurityGroupApi(securitygroups_db.SecurityGroupDbMixin):
    def __init__(self):
        super(NeutronSecurityGroupApi, self)
        self.context = neutron_context.get_admin_context()
        self.filters = v3_utils.get_plugin_filters(self.context)

    def get_security_groups(self):
        return super(NeutronSecurityGroupApi,
                     self).get_security_groups(self.context,
                                               filters=self.filters)

    def delete_security_group(self, sg_id):
        return super(NeutronSecurityGroupApi,
                     self).delete_security_group(self.context, sg_id)

    def get_nsgroup_id(self, sg_id):
        return nsx_db.get_nsx_security_group_id(
            self.context.session, sg_id)

    def get_port_security_groups(self, port_id):
        secgroups_bindings = self._get_port_security_group_bindings(
            self.context, {'port_id': [port_id]})
        return [b['security_group_id'] for b in secgroups_bindings]

    def get_ports_in_security_group(self, security_group_id):
        secgroups_bindings = self._get_port_security_group_bindings(
            self.context, {'security_group_id': [security_group_id]})
        return [b['port_id'] for b in secgroups_bindings]

    def delete_security_group_section_mapping(self, sg_id):
        with db_api.CONTEXT_WRITER.using(self.context):
            fw_mapping = self.context.session.query(
                nsx_models.NeutronNsxFirewallSectionMapping).filter_by(
                    neutron_id=sg_id).one_or_none()
            if fw_mapping:
                self.context.session.delete(fw_mapping)

    def delete_security_group_backend_mapping(self, sg_id):
        with db_api.CONTEXT_WRITER.using(self.context):
            sg_mapping = self.context.session.query(
                nsx_models.NeutronNsxSecurityGroupMapping).filter_by(
                    neutron_id=sg_id).one_or_none()
            if sg_mapping:
                self.context.session.delete(sg_mapping)

    def get_logical_port_id(self, port_id):
        mapping = self.context.session.query(
            nsx_models.NeutronNsxPortMapping).filter_by(
                neutron_id=port_id).one_or_none()
        if mapping:
            return mapping.nsx_id


neutron_sg = NeutronSecurityGroupApi()
neutron_db = v3_utils.NeutronDbClient()


def _log_info(resource, data, attrs=['display_name', 'id']):
    LOG.info(formatters.output_formatter(resource, data, attrs))


@admin_utils.list_handler(constants.SECURITY_GROUPS)
@admin_utils.output_header
def list_security_groups_mappings(resource, event, trigger, **kwargs):
    """List neutron security groups"""
    sg_mappings = plugin_utils.get_security_groups_mappings(neutron_sg.context)
    _log_info(constants.SECURITY_GROUPS,
              sg_mappings,
              attrs=['name', 'id', 'section-id', 'nsx-securitygroup-id'])
    return bool(sg_mappings)


@admin_utils.list_handler(constants.FIREWALL_SECTIONS)
@admin_utils.output_header
def nsx_list_dfw_sections(resource, event, trigger, **kwargs):
    """List NSX backend firewall sections"""
    nsxlib = v3_utils.get_connected_nsxlib()
    fw_sections = nsxlib.firewall_section.list()
    _log_info(constants.FIREWALL_SECTIONS, fw_sections)
    return bool(fw_sections)


@admin_utils.list_handler(constants.FIREWALL_NSX_GROUPS)
@admin_utils.output_header
def nsx_list_security_groups(resource, event, trigger, **kwargs):
    """List NSX backend security groups"""
    nsxlib = v3_utils.get_connected_nsxlib()
    nsx_secgroups = nsxlib.ns_group.list()
    _log_info(constants.FIREWALL_NSX_GROUPS, nsx_secgroups)
    return bool(nsx_secgroups)


def _find_missing_security_groups():
    nsxlib = v3_utils.get_connected_nsxlib()
    nsx_secgroups = nsxlib.ns_group.list()
    sg_mappings = plugin_utils.get_security_groups_mappings(neutron_sg.context)
    missing_secgroups = {}
    for sg_db in sg_mappings:
        for nsx_sg in nsx_secgroups:
            if nsx_sg['id'] == sg_db['nsx-securitygroup-id']:
                break
        else:
            missing_secgroups[sg_db['id']] = sg_db
    return missing_secgroups


@admin_utils.list_mismatches_handler(constants.FIREWALL_NSX_GROUPS)
@admin_utils.output_header
def list_missing_security_groups(resource, event, trigger, **kwargs):
    """List security groups with sections missing on the NSX backend"""
    sgs_with_missing_nsx_group = _find_missing_security_groups()
    missing_securitgroups_info = [
        {'securitygroup-name': sg['name'],
         'securitygroup-id': sg['id'],
         'nsx-securitygroup-id':
         sg['nsx-securitygroup-id']}
        for sg in sgs_with_missing_nsx_group.values()]
    _log_info(constants.FIREWALL_NSX_GROUPS, missing_securitgroups_info,
              attrs=['securitygroup-name', 'securitygroup-id',
                     'nsx-securitygroup-id'])
    return bool(missing_securitgroups_info)


def _find_missing_sections():
    nsxlib = v3_utils.get_connected_nsxlib()
    fw_sections = nsxlib.firewall_section.list()
    sg_mappings = plugin_utils.get_security_groups_mappings(neutron_sg.context)
    missing_sections = {}
    for sg_db in sg_mappings:
        for fw_section in fw_sections:
            if fw_section['id'] == sg_db['section-id']:
                break
        else:
            missing_sections[sg_db['id']] = sg_db
    return missing_sections


@admin_utils.list_mismatches_handler(constants.FIREWALL_SECTIONS)
@admin_utils.output_header
def list_missing_firewall_sections(resource, event, trigger, **kwargs):
    """List security groups with missing sections on the NSX backend"""
    sgs_with_missing_section = _find_missing_sections()
    missing_sections_info = [{'securitygroup-name': sg['name'],
                              'securitygroup-id': sg['id'],
                              'section-id': sg['section-id']}
                             for sg in sgs_with_missing_section.values()]
    _log_info(constants.FIREWALL_SECTIONS, missing_sections_info,
              attrs=['securitygroup-name', 'securitygroup-id', 'section-id'])
    return bool(missing_sections_info)


@admin_utils.fix_mismatches_handler(constants.SECURITY_GROUPS)
@admin_utils.output_header
def fix_security_groups(resource, event, trigger, **kwargs):
    """Fix mismatch security groups by recreating missing sections & NS groups
    on the NSX backend
    """
    context_ = neutron_context.get_admin_context()
    inconsistent_secgroups = _find_missing_sections()
    inconsistent_secgroups.update(_find_missing_security_groups())

    nsxlib = v3_utils.get_connected_nsxlib()
    with v3_utils.NsxV3PluginWrapper() as plugin:
        for sg_id, sg in inconsistent_secgroups.items():
            secgroup = plugin.get_security_group(context_, sg_id)

            try:
                # FIXME(roeyc): try..except clause should be removed once the
                # api will return 404 response code instead 400 for trying to
                # delete a non-existing firewall section.
                nsxlib.firewall_section.delete(sg['section-id'])
            except Exception:
                pass
            nsxlib.ns_group.delete(sg['nsx-securitygroup-id'])
            neutron_sg.delete_security_group_section_mapping(sg_id)
            neutron_sg.delete_security_group_backend_mapping(sg_id)
            nsgroup, fw_section = (
                plugin._create_security_group_backend_resources(secgroup))
            nsx_db.save_sg_mappings(
                context_, sg_id, nsgroup['id'], fw_section['id'])
            # If version > 1.1 then we use dynamic criteria tags, and the port
            # should already have them.
            if not nsxlib.feature_supported(consts.FEATURE_DYNAMIC_CRITERIA):
                members = []
                for port_id in neutron_sg.get_ports_in_security_group(sg_id):
                    lport_id = neutron_sg.get_logical_port_id(port_id)
                    members.append(lport_id)
                nsxlib.ns_group.add_members(
                    nsgroup['id'], consts.TARGET_TYPE_LOGICAL_PORT, members)

            for rule in secgroup['security_group_rules']:
                rule_mapping = (context_.session.query(
                    nsx_models.NeutronNsxRuleMapping).filter_by(
                        neutron_id=rule['id']).one())
                with context_.session.begin(subtransactions=True):
                    context_.session.delete(rule_mapping)
            action = (consts.FW_ACTION_DROP
                      if secgroup.get(provider_sg.PROVIDER)
                      else consts.FW_ACTION_ALLOW)
            rules = plugin._create_firewall_rules(
                context_, fw_section['id'], nsgroup['id'],
                secgroup.get(sg_logging.LOGGING, False), action,
                secgroup['security_group_rules'])
            plugin.save_security_group_rule_mappings(context_, rules['rules'])


def _update_ports_dynamic_criteria_tags():
    nsxlib = v3_utils.get_connected_nsxlib()
    for port in neutron_db.get_ports():
        secgroups = neutron_sg.get_port_security_groups(port['id'])
        # Nothing to do with ports that are not associated with any sec-group.
        if not secgroups:
            continue

        _, lport_id = neutron_db.get_lswitch_and_lport_id(port['id'])
        criteria_tags = nsxlib.ns_group.get_lport_tags(secgroups)
        nsxlib.logical_port.update(
            lport_id, False, tags_update=criteria_tags)


def _update_security_group_dynamic_criteria():
    nsxlib = v3_utils.get_connected_nsxlib()
    secgroups = neutron_sg.get_security_groups()
    for sg in secgroups:
        nsgroup_id = neutron_sg.get_nsgroup_id(sg['id'])
        membership_criteria = nsxlib.ns_group.get_port_tag_expression(
            security.PORT_SG_SCOPE, sg['id'])
        try:
            # We want to add the dynamic criteria and remove all direct members
            # they will be added by the manager using the new criteria.
            nsxlib.ns_group.update(nsgroup_id,
                                   membership_criteria=membership_criteria,
                                   members=[])
        except Exception as e:
            LOG.warning("Failed to update membership criteria for nsgroup "
                        "%(nsgroup_id)s, request to backend returned "
                        "with error: %(error)s",
                        {'nsgroup_id': nsgroup_id, 'error': str(e)})


@admin_utils.output_header
def migrate_nsgroups_to_dynamic_criteria(resource, event, trigger, **kwargs):
    """Update NSX security groups dynamic criteria for NSXv3 CrossHairs"""
    nsxlib = v3_utils.get_connected_nsxlib()
    if not nsxlib.feature_supported(consts.FEATURE_DYNAMIC_CRITERIA):
        LOG.error("Dynamic criteria grouping feature isn't supported by "
                  "this NSX version.")
        return
    # First, we add the criteria tags for all ports.
    _update_ports_dynamic_criteria_tags()
    # Update security-groups with dynamic criteria and remove direct members.
    _update_security_group_dynamic_criteria()


def list_orphaned_sections(resource, event, trigger, **kwargs):
    """List orphaned firewall sections"""
    nsxlib = v3_utils.get_connected_nsxlib()
    orphaned_sections = plugin_utils.get_orphaned_firewall_sections(
        neutron_sg.context, nsxlib)
    _log_info(constants.ORPHANED_FIREWALL_SECTIONS, orphaned_sections,
              attrs=['id', 'display_name'])


def clean_orphaned_sections(resource, event, trigger, **kwargs):
    """Delete orphaned firewall sections from the NSX backend"""
    nsxlib = v3_utils.get_connected_nsxlib()
    orphaned_sections = plugin_utils.get_orphaned_firewall_sections(
        neutron_sg.context, nsxlib)
    for sec in orphaned_sections:
        try:
            nsxlib.firewall_section.delete(sec['id'])
        except Exception as e:
            LOG.error("Failed to delete backend firewall section %(id)s : "
                      "%(e)s.", {'id': sec['id'], 'e': e})
        else:
            LOG.info("Backend firewall section %s was deleted.", sec['id'])


def update_security_groups_logging(resource, event, trigger, **kwargs):
    """Update allowed traffic logging for all neutron security group rules"""
    errmsg = ("Need to specify log-allowed-traffic property. Add --property "
              "log-allowed-traffic=true/false")
    if not kwargs.get('property'):
        LOG.error("%s", errmsg)
        return
    properties = admin_utils.parse_multi_keyval_opt(kwargs['property'])
    log_allowed_str = properties.get('log-allowed-traffic')
    if not log_allowed_str or log_allowed_str.lower() not in ['true', 'false']:
        LOG.error("%s", errmsg)
        return
    log_allowed = log_allowed_str.lower() == 'true'

    context = neutron_context.get_admin_context()
    nsxlib = v3_utils.get_connected_nsxlib()

    with v3_utils.NsxV3PluginWrapper() as plugin:
        secgroups = plugin.get_security_groups(context,
                                             fields=['id',
                                             sg_logging.LOGGING])
        LOG.info("Going to update logging of %s sections",
                 len(secgroups))
        for sg in [sg for sg in secgroups
                   if sg.get(sg_logging.LOGGING) is False]:
            nsgroup_id, section_id = nsx_db.get_sg_mappings(
                context.session, sg['id'])
            if section_id:
                try:
                    nsxlib.firewall_section.set_rule_logging(
                        section_id, logging=log_allowed)
                except nsx_lib_exc.ManagerError:
                    LOG.error("Failed to update firewall rule logging "
                              "for rule in section %s", section_id)


registry.subscribe(update_security_groups_logging,
                   constants.SECURITY_GROUPS,
                   shell.Operations.UPDATE_LOGGING.value)

registry.subscribe(migrate_nsgroups_to_dynamic_criteria,
                   constants.FIREWALL_NSX_GROUPS,
                   shell.Operations.MIGRATE_TO_DYNAMIC_CRITERIA.value)

registry.subscribe(fix_security_groups,
                   constants.FIREWALL_SECTIONS,
                   shell.Operations.NSX_UPDATE.value)

registry.subscribe(list_orphaned_sections,
                   constants.ORPHANED_FIREWALL_SECTIONS,
                   shell.Operations.NSX_LIST.value)

registry.subscribe(clean_orphaned_sections,
                   constants.ORPHANED_FIREWALL_SECTIONS,
                   shell.Operations.NSX_CLEAN.value)
