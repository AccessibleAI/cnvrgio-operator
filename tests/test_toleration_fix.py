import unittest
import os
from common import CommonBase
from kubernetes import client, config
import logging

config.load_kube_config()
v1 = client.CoreV1Api()

node_list = v1.list_node()
nodes = []
for obj in node_list.items:
  nodes.append(obj.metadata.name)


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

    def test_taint_node(self):
        cmd1 = "kubectl -n cnvrg taint node {} kubernetes.azure.com/scalesetpriority=spot:NoExecute".format(nodes[-1])
        cmd2 = "kubectl -n cnvrg taint node {} nvidia.com/gpu=present:NoExecute".format(nodes[-1])
        cmd3 = "kubectl -n cnvrg label node {} accelerator=nvidia".format(nodes[-1])
        res1 = self.exec_cmd(cmd1)
        res2 = self.exec_cmd(cmd2)
        res3 = self.exec_cmd(cmd3)
        res4 = res1[0] + res2[0] + res3[0]
        self.assertEqual(0, res4)

    def test_fluentd_ready(self):
        cmd = "kubectl -n cnvrg wait --for=condition=ready pod -l k8s-app=fluentd-logging --field-selector=spec.nodeName={}  --timeout=120s".format(nodes[-1])
        res = self.exec_cmd(cmd)
        self.assertEqual(0, res[0])

    def test_dcgm_ready(self):
        cmd = "kubectl -n cnvrg wait --for=condition=ready pod -l app.kubernetes.io/name=dcgm-exporter --field-selector=spec.nodeName={}  --timeout=120s".format(nodes[-1])
        res = self.exec_cmd(cmd)
        self.assertEqual(0, res[0])


    def test_node_exporter_ready(self):
        cmd = "kubectl -n cnvrg wait --for=condition=ready pod -l app.kubernetes.io/name=node-exporter --field-selector=spec.nodeName={}  --timeout=120s".format(nodes[-1])
        res = self.exec_cmd(cmd)
        self.assertEqual(0, res[0])


    def test_nvidia_plugin_ready(self):
        cmd = "kubectl -n cnvrg wait --for=condition=ready pod -l app=nvidia-device-plugin --field-selector=spec.nodeName={}  --timeout=120s".format(nodes[-1])
        res = self.exec_cmd(cmd)
        self.assertEqual(0, res[0])


    def test_untaint_node(self):
        cmd1 = "kubectl -n cnvrg taint node {} kubernetes.azure.com/scalesetpriority=spot:NoSchedule-".format(nodes[-1])
        cmd2 = "kubectl -n cnvrg taint node {} nvidia.com/gpu=present:NoSchedule-".format(nodes[-1])
        cmd3 = "kubectl -n cnvrg label node {} accelerator-".format(nodes[-1])
        res1 = self.exec_cmd(cmd1)
        res2 = self.exec_cmd(cmd2)
        res3 = self.exec_cmd(cmd3)
        res4 = res1[0] + res2[0] + res3[0]
        self.assertEqual(0, res4)