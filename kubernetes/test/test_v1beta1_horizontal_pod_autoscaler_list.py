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
from kubernetes.client.models.v1beta1_horizontal_pod_autoscaler_list import V1beta1HorizontalPodAutoscalerList


class TestV1beta1HorizontalPodAutoscalerList(unittest.TestCase):
    """ V1beta1HorizontalPodAutoscalerList unit test stubs """

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def testV1beta1HorizontalPodAutoscalerList(self):
        """
        Test V1beta1HorizontalPodAutoscalerList
        """
        model = kubernetes.client.models.v1beta1_horizontal_pod_autoscaler_list.V1beta1HorizontalPodAutoscalerList()


if __name__ == '__main__':
    unittest.main()
