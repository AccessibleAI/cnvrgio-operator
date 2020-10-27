import unittest
import os
from common import CommonBase
from kubernetes import client, config
import logging

config.load_kube_config()

CNVRG_SPEC = """
apiVersion: mlops.cnvrg.io/v1
kind: CnvrgApp
metadata:
  name: cnvrg-app
  namespace: cnvrg
spec:
  clusterDomain: "__CLUSTER_DOMAIN__"
  cnvrgApp:
    image: "cnvrg/core:3.1.3"
    intercom: "false"
"""


class SanityAksIstioTest(unittest.TestCase, CommonBase):

    @classmethod
    def setUpClass(cls):
        cls.deploy()
        cls.create_cnvrg_spec(CNVRG_SPEC)
        cls.wait_for_cnvrg_spec_ready()

    @classmethod
    def tearDownClass(cls):
        if os.getenv("RUN_TEARDOWN", "true") == "true":
            cls.delete_cnvrg_spec()
            cls.undeploy()

    def test_mpi_operator_pod_deployed(self):
        v1 = client.CoreV1Api()
        pod = v1.list_namespaced_pod("cnvrg", label_selector="app=mpi-operator")
        self.assertEqual(1, len(pod.items))

    def test_mpi_operator_pod_ready(self):
        cmd = "kubectl wait --for=condition=ready pod -l app=mpi-operator -ncnvrg --timeout=120s"
        res = self.exec_cmd(cmd)
        self.assertEqual(0, res[0])
