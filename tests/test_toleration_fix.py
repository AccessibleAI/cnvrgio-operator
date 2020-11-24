import unittest
from common import CommonBase
from kubernetes import client, config
import time

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
    enabled: "false"
  minio:
    enabled: "false"
  monitoring:
    enabled: "true"
  istio:
    enabled: "false"
  kibana:
    enabled: "false"
  fluentd:
    enabled: "true"
  nvidiadp:
    enabled: "true"
"""


class CnvrgTolerationFix(unittest.TestCase, CommonBase):

    @classmethod
    def setUpClass(cls):
        cls._started_at = time.time()
        cls._exec_cmd(
            "kubectl taint node {} kubernetes.azure.com/scalesetpriority=spot:NoSchedule --overwrite".format(nodes[-1]))
        cls._exec_cmd("kubectl taint node {} nvidia.com/gpu=present:NoSchedule --overwrite".format(nodes[-1]))
        cls._exec_cmd("kubectl label node {} accelerator=nvidia --overwrite".format(nodes[-1]))
        cls.deploy()
        cls.create_cnvrg_spec(CNVRG_SPEC)
        cls.wait_for_cnvrg_spec_ready()
        time.sleep(3)

    @classmethod
    def tearDownClass(cls):
        cls.delete_cnvrg_spec()
        cls.undeploy()
        cls._exec_cmd("kubectl taint node {} kubernetes.azure.com/scalesetpriority-".format(nodes[-1]))
        cls._exec_cmd("kubectl taint node {} nvidia.com/gpu-".format(nodes[-1]))
        cls._exec_cmd("kubectl label node {} accelerator-".format(nodes[-1]))
        cls.log_total_test_execution_time(cls._started_at, "CnvrgTolerationFix")

    def test_fluentd_ready(self):
        cmd = "kubectl -n cnvrg wait --for=condition=PodScheduled pod -l k8s-app=fluentd-logging --field-selector=spec.nodeName={}  --timeout=600s".format(
            nodes[-1])
        res = self.exec_cmd(cmd)
        self.assertEqual(0, res[0])

    def test_dcgm_ready(self):
        cmd = "kubectl -n cnvrg wait --for=condition=PodScheduled pod -l app.kubernetes.io/name=dcgm-exporter --field-selector=spec.nodeName={}  --timeout=600s".format(
            nodes[-1])
        res = self.exec_cmd(cmd)
        self.assertEqual(0, res[0])

    def test_node_exporter_ready(self):
        cmd = "kubectl -n cnvrg wait --for=condition=PodScheduled pod -l app.kubernetes.io/name=node-exporter --field-selector=spec.nodeName={}  --timeout=600s".format(
            nodes[-1])
        res = self.exec_cmd(cmd)
        self.assertEqual(0, res[0])

    def test_nvidia_plugin_ready(self):
        cmd = "kubectl -n cnvrg wait --for=condition=PodScheduled pod -l name=nvidia-device-plugin-ds --field-selector=spec.nodeName={}  --timeout=600s".format(
            nodes[-1])
        res = self.exec_cmd(cmd)
        self.assertEqual(0, res[0])
