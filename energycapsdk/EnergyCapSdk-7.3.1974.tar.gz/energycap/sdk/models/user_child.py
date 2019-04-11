# coding=utf-8
# --------------------------------------------------------------------------
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

from msrest.serialization import Model


class UserChild(Model):
    """UserChild.

    :param user_id: The user identifier
    :type user_id: int
    :param user_code: The user code
    :type user_code: str
    :param full_name: The user's full name
    :type full_name: str
    """

    _attribute_map = {
        'user_id': {'key': 'userId', 'type': 'int'},
        'user_code': {'key': 'userCode', 'type': 'str'},
        'full_name': {'key': 'fullName', 'type': 'str'},
    }

    def __init__(self, user_id=None, user_code=None, full_name=None):
        super(UserChild, self).__init__()
        self.user_id = user_id
        self.user_code = user_code
        self.full_name = full_name
