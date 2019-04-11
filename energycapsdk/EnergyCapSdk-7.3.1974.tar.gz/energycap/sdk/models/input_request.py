# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class InputRequest(Model):
    """InputRequest.

    :param name:  <span class='property-internal'>Required</span> <span
     class='property-internal'>Must be between 0 and 32 characters</span>
    :type name: str
    :param prompt:  <span class='property-internal'>Must be between 0 and 32
     characters</span>
    :type prompt: str
    :param help_tag:  <span class='property-internal'>Must be between 0 and 32
     characters</span>
    :type help_tag: str
    :param default_value:  <span class='property-internal'>Must be between 0
     and 255 characters</span>
    :type default_value: str
    :param calculation:
    :type calculation: int
    :param is_block:
    :type is_block: bool
    :param data_type:
    :type data_type: int
    :param observation_type_code:  <span class='property-internal'>Must be
     between 0 and 16 characters</span>
    :type observation_type_code: str
    :param unit_code:  <span class='property-internal'>Must be between 0 and
     16 characters</span>
    :type unit_code: str
    :param display_order:  <span class='property-internal'>Required</span>
    :type display_order: int
    """

    _validation = {
        'name': {'required': True, 'max_length': 32, 'min_length': 0},
        'prompt': {'max_length': 32, 'min_length': 0},
        'help_tag': {'max_length': 32, 'min_length': 0},
        'default_value': {'max_length': 255, 'min_length': 0},
        'observation_type_code': {'max_length': 16, 'min_length': 0},
        'unit_code': {'max_length': 16, 'min_length': 0},
        'display_order': {'required': True},
    }

    _attribute_map = {
        'name': {'key': 'name', 'type': 'str'},
        'prompt': {'key': 'prompt', 'type': 'str'},
        'help_tag': {'key': 'helpTag', 'type': 'str'},
        'default_value': {'key': 'defaultValue', 'type': 'str'},
        'calculation': {'key': 'calculation', 'type': 'int'},
        'is_block': {'key': 'isBlock', 'type': 'bool'},
        'data_type': {'key': 'dataType', 'type': 'int'},
        'observation_type_code': {'key': 'observationTypeCode', 'type': 'str'},
        'unit_code': {'key': 'unitCode', 'type': 'str'},
        'display_order': {'key': 'displayOrder', 'type': 'int'},
    }

    def __init__(self, name, display_order, prompt=None, help_tag=None, default_value=None, calculation=None, is_block=None, data_type=None, observation_type_code=None, unit_code=None):
        super(InputRequest, self).__init__()
        self.name = name
        self.prompt = prompt
        self.help_tag = help_tag
        self.default_value = default_value
        self.calculation = calculation
        self.is_block = is_block
        self.data_type = data_type
        self.observation_type_code = observation_type_code
        self.unit_code = unit_code
        self.display_order = display_order
