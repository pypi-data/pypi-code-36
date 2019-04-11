# coding: utf-8

"""
    ACA Services API

    API for methods pertaining to all ACA services  # noqa: E501

    OpenAPI spec version: 1.0.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import unittest

import autocheckauctions
from autocheckauctions.api.default_api import DefaultApi  # noqa: E501
from autocheckauctions.rest import ApiException


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self):
        self.api = autocheckauctions.api.default_api.DefaultApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_vehicle_announcement_options(self):
        """Test case for vehicle_announcement_options

        """
        pass

    def test_vehicle_history_accident_options(self):
        """Test case for vehicle_history_accident_options

        """
        pass

    def test_vehicle_history_announcement_options(self):
        """Test case for vehicle_history_announcement_options

        """
        pass

    def test_vehicle_history_canadian_options(self):
        """Test case for vehicle_history_canadian_options

        """
        pass

    def test_vehicle_history_canadian_plus_options(self):
        """Test case for vehicle_history_canadian_plus_options

        """
        pass

    def test_vehicle_history_compromised_options(self):
        """Test case for vehicle_history_compromised_options

        """
        pass

    def test_vehicle_history_disaster_options(self):
        """Test case for vehicle_history_disaster_options

        """
        pass

    def test_vehicle_history_discrepancy_options(self):
        """Test case for vehicle_history_discrepancy_options

        """
        pass

    def test_vehicle_history_exception_options(self):
        """Test case for vehicle_history_exception_options

        """
        pass

    def test_vehicle_history_full_options(self):
        """Test case for vehicle_history_full_options

        """
        pass

    def test_vehicle_history_recall_options(self):
        """Test case for vehicle_history_recall_options

        """
        pass

    def test_vehicle_history_summary_options(self):
        """Test case for vehicle_history_summary_options

        """
        pass

    def test_vehicle_history_theft_options(self):
        """Test case for vehicle_history_theft_options

        """
        pass


if __name__ == '__main__':
    unittest.main()
