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
from kubernetes.client.models.v1beta1_http_ingress_rule_value import V1beta1HTTPIngressRuleValue


class TestV1beta1HTTPIngressRuleValue(unittest.TestCase):
    """ V1beta1HTTPIngressRuleValue unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV1beta1HTTPIngressRuleValue(self):
        """
        Test V1beta1HTTPIngressRuleValue
        """
        model = kubernetes.client.models.v1beta1_http_ingress_rule_value.V1beta1HTTPIngressRuleValue()


if __name__ == '__main__':
    unittest.main()
