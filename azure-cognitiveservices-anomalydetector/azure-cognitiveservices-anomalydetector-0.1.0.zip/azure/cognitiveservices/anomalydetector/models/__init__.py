# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

# coding=utf-8
# --------------------------------------------------------------------------
# Copyright (c) Microsoft Corporation. All rights reserved.
# Licensed under the MIT License. See License.txt in the project root for
# license information.
#
# Code generated by Microsoft (R) AutoRest Code Generator.
# Changes may cause incorrect behavior and will be lost if the code is
# regenerated.
# --------------------------------------------------------------------------

try:
    from .api_error_py3 import APIError, APIErrorException
    from .point_py3 import Point
    from .request_py3 import Request
    from .entire_detect_response_py3 import EntireDetectResponse
    from .last_detect_response_py3 import LastDetectResponse
except (SyntaxError, ImportError):
    from .api_error import APIError, APIErrorException
    from .point import Point
    from .request import Request
    from .entire_detect_response import EntireDetectResponse
    from .last_detect_response import LastDetectResponse
from .anomaly_detector_client_enums import (
    Granularity,
)

__all__ = [
    'APIError', 'APIErrorException',
    'Point',
    'Request',
