# coding: utf-8

"""
    Purity//FB REST Client

    Client for Purity//FB REST API (1.0), developed by [Pure Storage, Inc](http://www.purestorage.com/). Documentations can be found at [purity-fb.readthedocs.io](http://purity-fb.readthedocs.io/).

    OpenAPI spec version: 1.5
    Contact: info@purestorage.com
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from pprint import pformat
from six import iteritems
import re


class LinkAggregationGroup(object):
    """
    NOTE: This class is auto generated by the swagger code generator program.
    Do not edit the class manually.
    """


    """
    Attributes:
      swagger_types (dict): The key is attribute name
                            and the value is attribute type.
      attribute_map (dict): The key is attribute name
                            and the value is json key in definition.
    """
    swagger_types = {
        'name': 'str',
        'lag_speed': 'int',
        'mac_address': 'str',
        'ports': 'list[Reference]',
        'port_speed': 'int',
        'status': 'str'
    }

    attribute_map = {
        'name': 'name',
        'lag_speed': 'lag_speed',
        'mac_address': 'mac_address',
        'ports': 'ports',
        'port_speed': 'port_speed',
        'status': 'status'
    }

    def __init__(self, name=None, lag_speed=None, mac_address=None, ports=None, port_speed=None, status=None):
        """
        LinkAggregationGroup - a model defined in Swagger
        """

        self._name = None
        self._lag_speed = None
        self._mac_address = None
        self._ports = None
        self._port_speed = None
        self._status = None

        if name is not None:
          self.name = name
        if lag_speed is not None:
          self.lag_speed = lag_speed
        if mac_address is not None:
          self.mac_address = mac_address
        if ports is not None:
          self.ports = ports
        if port_speed is not None:
          self.port_speed = port_speed
        if status is not None:
          self.status = status

    @property
    def name(self):
        """
        Gets the name of this LinkAggregationGroup.
        name of the object (e.g., a file system or snapshot)

        :return: The name of this LinkAggregationGroup.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """
        Sets the name of this LinkAggregationGroup.
        name of the object (e.g., a file system or snapshot)

        :param name: The name of this LinkAggregationGroup.
        :type: str
        """

        self._name = name

    @property
    def lag_speed(self):
        """
        Gets the lag_speed of this LinkAggregationGroup.
        Combined speed of all ports in the LAG in bits-per-second.

        :return: The lag_speed of this LinkAggregationGroup.
        :rtype: int
        """
        return self._lag_speed

    @lag_speed.setter
    def lag_speed(self, lag_speed):
        """
        Sets the lag_speed of this LinkAggregationGroup.
        Combined speed of all ports in the LAG in bits-per-second.

        :param lag_speed: The lag_speed of this LinkAggregationGroup.
        :type: int
        """

        self._lag_speed = lag_speed

    @property
    def mac_address(self):
        """
        Gets the mac_address of this LinkAggregationGroup.
        Unique MAC address assigned to the LAG

        :return: The mac_address of this LinkAggregationGroup.
        :rtype: str
        """
        return self._mac_address

    @mac_address.setter
    def mac_address(self, mac_address):
        """
        Sets the mac_address of this LinkAggregationGroup.
        Unique MAC address assigned to the LAG

        :param mac_address: The mac_address of this LinkAggregationGroup.
        :type: str
        """
        if mac_address is not None and not re.search('^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$', mac_address):
            raise ValueError("Invalid value for `mac_address`, must be a follow pattern or equal to `/^([0-9A-Fa-f]{2}[:-]){5}([0-9A-Fa-f]{2})$/`")

        self._mac_address = mac_address

    @property
    def ports(self):
        """
        Gets the ports of this LinkAggregationGroup.
        Ports associated with the LAG

        :return: The ports of this LinkAggregationGroup.
        :rtype: list[Reference]
        """
        return self._ports

    @ports.setter
    def ports(self, ports):
        """
        Sets the ports of this LinkAggregationGroup.
        Ports associated with the LAG

        :param ports: The ports of this LinkAggregationGroup.
        :type: list[Reference]
        """

        self._ports = ports

    @property
    def port_speed(self):
        """
        Gets the port_speed of this LinkAggregationGroup.
        Configured speed of each port in the LAG in bits-per-second

        :return: The port_speed of this LinkAggregationGroup.
        :rtype: int
        """
        return self._port_speed

    @port_speed.setter
    def port_speed(self, port_speed):
        """
        Sets the port_speed of this LinkAggregationGroup.
        Configured speed of each port in the LAG in bits-per-second

        :param port_speed: The port_speed of this LinkAggregationGroup.
        :type: int
        """

        self._port_speed = port_speed

    @property
    def status(self):
        """
        Gets the status of this LinkAggregationGroup.
        Health status of the LAG. Possible values are critical, healthy, identifying, unclaimed, unhealthy, unrecognized and unused.

        :return: The status of this LinkAggregationGroup.
        :rtype: str
        """
        return self._status

    @status.setter
    def status(self, status):
        """
        Sets the status of this LinkAggregationGroup.
        Health status of the LAG. Possible values are critical, healthy, identifying, unclaimed, unhealthy, unrecognized and unused.

        :param status: The status of this LinkAggregationGroup.
        :type: str
        """

        self._status = status

    def to_dict(self):
        """
        Returns the model properties as a dict
        """
        result = {}

        for attr, _ in iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            else:
                result[attr] = value

        return result

    def to_str(self):
        """
        Returns the string representation of the model
        """
        return pformat(self.to_dict())

    def __repr__(self):
        """
        For `print` and `pprint`
        """
        return self.to_str()

    def __eq__(self, other):
        """
        Returns true if both objects are equal
        """
        if not isinstance(other, LinkAggregationGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        """
        Returns true if both objects are not equal
        """
        return not self == other
