import unittest
import os
from common import CommonBase
from kubernetes import client, config
import logging

config.load_kube_config()

CNVRG_SPEC_ISTIO_ONLY = """
apiVersion: mlops.cnvrg.io/v1
kind: CnvrgApp
metadata:
  name: cnvrg-app
  namespace: cnvrg
spec:
  clusterDomain: "sample-domain"
  istio:
    enabled: "true"
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
  monitoring:
    enabled: "false"
  kibana:
    enabled: "false"
  fluentd:
    enabled: "false"
  nvidiadp:
    enabled: "false"
"""
CNVRG_SPEC_AKS_ISTIO_DEFAULT = """
apiVersion: mlops.cnvrg.io/v1
kind: CnvrgApp
metadata:
  name: cnvrg-app
  namespace: cnvrg
spec:
  clusterDomain: "__CLUSTER_DOMAIN__"
  cnvrgApp:
    enabled: "true"
    image: "cnvrg/core:3.1.3"
  pg:
    enabled: "true"
  conf:
    enabled: "true"
  redis:
    enabled: "true"
  es:
    enabled: "true"
  minio:
    enabled: "true"
"""


class SanityAksIstioTest(unittest.TestCase, CommonBase):

    @classmethod
    def setUpClass(cls):
        cls.deploy()
        cls.create_cnvrg_spec(CNVRG_SPEC_ISTIO_ONLY)
        cls.wait_for_cnvrg_spec_ready()
        patched_spec = CNVRG_SPEC_AKS_ISTIO_DEFAULT.replace("__CLUSTER_DOMAIN__", cls.get_nip_nip_url("istio"))
        cls.create_cnvrg_spec(patched_spec, True)
        cls.wait_for_cnvrg_spec_ready()

    @classmethod
    def tearDownClass(cls):
        cls.delete_cnvrg_spec()
        cls.undeploy()

    def test_app_ready_aks_istio(self):
        cmd = "kubectl wait --for=condition=ready pod -l app=app -ncnvrg --timeout=1500s"
        res = self.exec_cmd(cmd)
        self.assertEqual(0, res[0])
