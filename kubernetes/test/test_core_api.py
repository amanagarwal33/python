# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)  # noqa: E501

<<<<<<< HEAD
    OpenAPI spec version: v1.15.6
    Generated by: https://openapi-generator.tech
=======
    OpenAPI spec version: v1.5.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
>>>>>>> release-1.0
"""


from __future__ import absolute_import

import unittest

import kubernetes.client
from kubernetes.client.api.core_api import CoreApi  # noqa: E501
from kubernetes.client.rest import ApiException


class TestCoreApi(unittest.TestCase):
    """CoreApi unit test stubs"""

    def setUp(self):
        self.api = kubernetes.client.api.core_api.CoreApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_get_api_versions(self):
        """Test case for get_api_versions

        """
        pass


if __name__ == '__main__':
    unittest.main()
