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
  ingressType: "none"
  mpi:
    enabled: "false"
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
    enabled: "true"
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


class CnvrgEsSmallFixTest(unittest.TestCase, CommonBase):

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

    def test_es_pod_deployed(self):
        v1 = client.CoreV1Api()
        pod = v1.list_namespaced_pod("cnvrg", label_selector="app=elasticsearch")
        self.assertEqual(1, len(pod.items))

    def test_es_pod_ready(self):
        cmd = "kubectl wait --for=condition=ready pod -l app=elasticsearch -n cnvrg --timeout=120s"
        res = self.exec_cmd(cmd)
        self.assertEqual(0, res[0])