import unittest
import os
from common import CommonBase
from kubernetes import client, config
import logging
import time

config.load_kube_config()
v1 = client.CoreV1Api()

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
  vpa:
    enabled: "true"
"""


class VpaAutoscalerTest(unittest.TestCase, CommonBase):

    @classmethod
    def setUpClass(cls):
        cls._started_at = time.time()
        cls.deploy()
        cls.create_cnvrg_spec(CNVRG_SPEC)
        if cls.wait_for_cnvrg_spec_ready() is False:
            assert False, 'CnvrgApp Spec was not ready in 30 min!'

    @classmethod
    def tearDownClass(cls):
        cls.delete_cnvrg_spec()
        cls.undeploy()
        cls.log_total_test_execution_time(cls._started_at, "VpaAutoscalerTest")

    def test_updater_ready(self):
        cmd = "kubectl -n cnvrg wait --for=condition=ready pod -l app=vpa-updater  --timeout=120s"
        res = self.exec_cmd(cmd)
        self.assertEqual(0, res[0])

    def test_recommender_ready(self):
        cmd = "kubectl -n cnvrg wait --for=condition=ready pod -l app=vpa-recommender  --timeout=120s"
        res = self.exec_cmd(cmd)
        self.assertEqual(0, res[0])

    def test_admission_ready(self):
        cmd = "kubectl -n cnvrg wait --for=condition=ready pod -l app=vpa-admission-controller --timeout=120s"
        res = self.exec_cmd(cmd)
        self.assertEqual(0, res[0])

    def test_vpa_deployments_ready(self):
        for i in range(60):
          cmd = "kubectl -n cnvrg get vpa |  grep -v NAME | wc -l"
          res = self.exec_cmd(cmd)
          time.sleep(2)
          if res[1] > '4':
            break
        self.assertTrue(res[1] > '4') 