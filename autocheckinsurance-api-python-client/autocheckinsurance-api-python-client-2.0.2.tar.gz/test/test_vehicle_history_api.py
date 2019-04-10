# coding: utf-8

"""
    ACI Services API

    API for methods pertaining to all ACI services  # noqa: E501

    OpenAPI spec version: 2.0.2
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import autocheckinsurance
from autocheckinsurance.api.vehicle_history_api import VehicleHistoryApi  # noqa: E501
from autocheckinsurance.rest import ApiException


class TestVehicleHistoryApi(unittest.TestCase):
    """VehicleHistoryApi unit test stubs"""

    def setUp(self):
        self.api = autocheckinsurance.api.vehicle_history_api.VehicleHistoryApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_history_full(self):
        """Test case for history_full

        Retrieve Historical Activity for Requested Vehicles  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()
