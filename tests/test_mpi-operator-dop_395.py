import unittest
import os
from common import CommonBase
from kubernetes import client, config

config.load_kube_config()

CNVRG_SPEC = """
apiVersion: mlops.cnvrg.io/v1
kind: CnvrgApp
metadata:
  name: cnvrg-app
  namespace: cnvrg
spec:
  mpi:
    enabled: "true"
  conf:
    enabled: "false"
  conf:
    enabled: "false"
  cnvrgApp:
    enabled: "false"
  pgBackup:
    enabled: "false"
  redis:
    enabled: "false"
  es:
    enabled: "false"
  minio:
    enabled: "false"
  prometheus:
    enabled: "false"
  istio:
    enabled: "false"
  kibana:
    enabled: "false"
  fluentd:
    enabled: "false"
  nvidiadp:
    enabled: "false"
"""


class CnvrgTaintsTest(unittest.TestCase, CommonBase):

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


    def test_mpi_operator(self):
        v1 = client.CoreV1Api()
        pod = v1.list_namespaced_pod("cnvrg", label_selector="app=mpi-operator")
        self.assertEqual(1, len(pod.items))
        self.assertIn("nodes are available", pod.items[0].status.conditions[0].message)