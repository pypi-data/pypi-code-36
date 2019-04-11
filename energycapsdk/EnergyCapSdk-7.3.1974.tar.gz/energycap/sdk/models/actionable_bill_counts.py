# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class ActionableBillCounts(Model):
    """ActionableBillCounts.

    :param export_hold_count: Count of bills Held from Export
    :type export_hold_count: int
    :param ap_export_count: Count of bills Waiting for Export to AP
    :type ap_export_count: int
    :param gl_export_count: Count of bills Waiting for Export to AP
    :type gl_export_count: int
    :param approval_count: Count of bills which are Not Approved
    :type approval_count: int
    :param audit_problem_count: Count of bills with audit problems
    :type audit_problem_count: int
    """

    _attribute_map = {
        'export_hold_count': {'key': 'exportHoldCount', 'type': 'int'},
        'ap_export_count': {'key': 'apExportCount', 'type': 'int'},
        'gl_export_count': {'key': 'glExportCount', 'type': 'int'},
        'approval_count': {'key': 'approvalCount', 'type': 'int'},
        'audit_problem_count': {'key': 'auditProblemCount', 'type': 'int'},
    }

    def __init__(self, export_hold_count=None, ap_export_count=None, gl_export_count=None, approval_count=None, audit_problem_count=None):
        super(ActionableBillCounts, self).__init__()
        self.export_hold_count = export_hold_count
        self.ap_export_count = ap_export_count
        self.gl_export_count = gl_export_count
        self.approval_count = approval_count
        self.audit_problem_count = audit_problem_count
