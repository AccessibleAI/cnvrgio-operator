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
  ingressType: "k8singress"
  clusterDomain: "__CLUSTER_DOMAIN__"
  tenancy:
    enabled: "true"
  cnvrgApp:
    image: "core:core-3.4.1-10-300"
    intercom: "false"
  cnvrgRouter:
    enabled: "true"
  pgBackup:
    enabled: "true"
"""


# class CnvrgTaintsNoTaintsSetTest(unittest.TestCase, CommonBase):
#
#     @classmethod
#     def setUpClass(cls):
#         cls.deploy()
#         cls._exec_cmd("kubectl label nodes cnvrg-taint=true --all --overwrite")
#         cls.create_cnvrg_spec(CNVRG_SPEC)
#         cls.wait_for_cnvrg_spec_ready()
#
#     @classmethod
#     def tearDownClass(cls):
#         return
#         cls._exec_cmd("kubectl label node cnvrg-taint- --all")
#         cls.delete_cnvrg_spec()
#         cls.undeploy()
#

#
#     def test_pg(self):
#         v1 = client.CoreV1Api()
#         pod = v1.list_namespaced_pod("cnvrg", label_selector="app=postgres")
#         self.assertEqual(1, len(pod.items))
#         self.assertIsNotNone(pod.items[0].status.conditions[0].message)
#         self.assertIn("nodes are available", pod.items[0].status.conditions[0].message)
#
#     def test_app(self):
#         v1 = client.CoreV1Api()
#         pod = v1.list_namespaced_pod("cnvrg", label_selector="app=app")
#         self.assertEqual(1, len(pod.items))
#         self.assertIsNotNone(pod.items[0].status.conditions[0].message)
#         self.assertIn("nodes are available", pod.items[0].status.conditions[0].message)
#
#     def test_es(self):
#         v1 = client.CoreV1Api()
#         pod = v1.list_namespaced_pod("cnvrg", label_selector="app=elasticsearch")
#         self.assertEqual(1, len(pod.items))
#         self.assertIsNotNone(pod.items[0].status.conditions[0].message)
#         self.assertIn("nodes are available", pod.items[0].status.conditions[0].message)
#
#     def test_kibana(self):
#         v1 = client.CoreV1Api()
#         pod = v1.list_namespaced_pod("cnvrg", label_selector="app=kibana")
#         self.assertEqual(1, len(pod.items))
#         self.assertIsNotNone(pod.items[0].status.conditions[0].message)
#         self.assertIn("nodes are available", pod.items[0].status.conditions[0].message)
#
#     def test_prom_operator(self):
#         v1 = client.CoreV1Api()
#         pod = v1.list_namespaced_pod("cnvrg", label_selector="app.kubernetes.io/name=prometheus-operator")
#         self.assertEqual(1, len(pod.items))
#         self.assertIn("nodes are available", pod.items[0].status.conditions[0].message)
#
#     def test_minio(self):
#         v1 = client.CoreV1Api()
#         pod = v1.list_namespaced_pod("cnvrg", label_selector="app=minio")
#         self.assertEqual(1, len(pod.items))
#         self.assertIsNotNone(pod.items[0].status.conditions[0].message)
#         self.assertIn("nodes are available", pod.items[0].status.conditions[0].message)
#
#     def test_mpi_operator(self):
#         v1 = client.CoreV1Api()
#         pod = v1.list_namespaced_pod("cnvrg", label_selector="app=mpi-operator")
#         self.assertEqual(1, len(pod.items))
#         self.assertIsNotNone(pod.items[0].status.conditions[0].message)
#         self.assertIn("nodes are available", pod.items[0].status.conditions[0].message)
#
#     def test_redis(self):
#         v1 = client.CoreV1Api()
#         pod = v1.list_namespaced_pod("cnvrg", label_selector="app=redis")
#         self.assertEqual(1, len(pod.items))
#         self.assertIsNotNone(pod.items[0].status.conditions[0].message)
#         self.assertIn("nodes are available", pod.items[0].status.conditions[0].message)
#
#     def test_grafana(self):
#         v1 = client.CoreV1Api()
#         pod = v1.list_namespaced_pod("cnvrg", label_selector="app=grafana")
#         self.assertEqual(1, len(pod.items))
#         self.assertIsNotNone(pod.items[0].status.conditions[0].message)
#         self.assertIn("nodes are available", pod.items[0].status.conditions[0].message)
#
#     def test_cnvrg_routing(self):
#         v1 = client.CoreV1Api()
#         pod = v1.list_namespaced_pod("cnvrg", label_selector="app=routing-service")
#         self.assertEqual(1, len(pod.items))
#         self.assertIsNotNone(pod.items[0].status.conditions[0].message)
#         self.assertIn("nodes are available", pod.items[0].status.conditions[0].message)
#


class CnvrgTaintsAreSetDedicatedNodesFalseTest(unittest.TestCase, CommonBase):

    @classmethod
    def setUpClass(cls):
        cls.get_nip_nip_url()
        cls.deploy()
        cls._exec_cmd("kubectl label nodes cnvrg-taint=true --all --overwrite")
        cls.create_cnvrg_spec(CNVRG_SPEC.replace("__CLUSTER_DOMAIN__", cls.get_nip_nip_url()))
        cls.wait_for_cnvrg_spec_ready()

    @classmethod
    def tearDownClass(cls):
        return
        cls._exec_cmd("kubectl label node cnvrg-taint- --all")
        cls.delete_cnvrg_spec()
        cls.undeploy()

    def test_pg(self):
        v1 = client.CoreV1Api()
        pod = v1.list_namespaced_pod("cnvrg", label_selector="app=postgres")
        self.assertEqual(1, len(pod.items))
        self.assertEqual("Running", pod.items[0].status.phase)

    def test_es(self):
        v1 = client.CoreV1Api()
        pod = v1.list_namespaced_pod("cnvrg", label_selector="app=elasticsearch")
        self.assertEqual(1, len(pod.items))
        self.assertEqual("Running", pod.items[0].status.phase)

    def test_kibana(self):
        v1 = client.CoreV1Api()
        pod = v1.list_namespaced_pod("cnvrg", label_selector="app=kibana")
        self.assertEqual(1, len(pod.items))
        self.assertEqual("Running", pod.items[0].status.phase)

    def test_prom_operator(self):
        v1 = client.CoreV1Api()
        pod = v1.list_namespaced_pod("cnvrg", label_selector="app.kubernetes.io/name=prometheus-operator")
        self.assertEqual(1, len(pod.items))
        self.assertEqual("Running", pod.items[0].status.phase)

    def test_minio(self):
        v1 = client.CoreV1Api()
        pod = v1.list_namespaced_pod("cnvrg", label_selector="app=minio")
        self.assertEqual(1, len(pod.items))
        self.assertEqual("Running", pod.items[0].status.phase)

    def test_mpi_operator(self):
        v1 = client.CoreV1Api()
        pod = v1.list_namespaced_pod("cnvrg", label_selector="app=mpi-operator")
        self.assertEqual(1, len(pod.items))
        self.assertEqual("Running", pod.items[0].status.phase)

    def test_redis(self):
        v1 = client.CoreV1Api()
        pod = v1.list_namespaced_pod("cnvrg", label_selector="app=redis")
        self.assertEqual(1, len(pod.items))
        self.assertEqual("Running", pod.items[0].status.phase)

    def test_grafana(self):
        v1 = client.CoreV1Api()
        pod = v1.list_namespaced_pod("cnvrg", label_selector="app=grafana")
        self.assertEqual(1, len(pod.items))
        self.assertEqual("Running", pod.items[0].status.phase)

    def test_cnvrg_routing(self):
        v1 = client.CoreV1Api()
        pod = v1.list_namespaced_pod("cnvrg", label_selector="app=routing-service")
        self.assertEqual(1, len(pod.items))
        self.assertEqual("Running", pod.items[0].status.phase)
