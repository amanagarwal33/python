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
from kubernetes.client.models.v1beta1_cpu_target_utilization import V1beta1CPUTargetUtilization


class TestV1beta1CPUTargetUtilization(unittest.TestCase):
    """ V1beta1CPUTargetUtilization unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV1beta1CPUTargetUtilization(self):
        """
        Test V1beta1CPUTargetUtilization
        """
        model = kubernetes.client.models.v1beta1_cpu_target_utilization.V1beta1CPUTargetUtilization()


if __name__ == '__main__':
    unittest.main()
