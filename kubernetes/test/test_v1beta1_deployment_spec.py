# coding: utf-8

"""
    Kubernetes

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)

    OpenAPI spec version: v1.5.3
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""


from __future__ import absolute_import

import os
import sys
import unittest

import kubernetes.client
from kubernetes.client.rest import ApiException
from kubernetes.client.models.v1beta1_deployment_spec import V1beta1DeploymentSpec


class TestV1beta1DeploymentSpec(unittest.TestCase):
    """ V1beta1DeploymentSpec unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV1beta1DeploymentSpec(self):
        """
        Test V1beta1DeploymentSpec
        """
        model = kubernetes.client.models.v1beta1_deployment_spec.V1beta1DeploymentSpec()


if __name__ == '__main__':
    unittest.main()
