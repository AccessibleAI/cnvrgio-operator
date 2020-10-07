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
  tenancy:
    enabled: "true"
  cnvrgApp:
    image: "cnvrg/core:3.1.3"
    intercom: "false"
  cnvrgRouter:
    enabled: "true"
  hostpath:
    enabled: "true"
  nfs:
    enabled: "true"
    server: "1.2.3.4"
    path: "/bla"
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

    def test_pg(self):
        v1 = client.CoreV1Api()
        pod = v1.list_namespaced_pod("cnvrg", label_selector="app=postgres")
        self.assertEqual(1, len(pod.items))
        self.assertIn("nodes are available", pod.items[0].status.conditions[0].message)

    def test_app(self):
        v1 = client.CoreV1Api()
        pod = v1.list_namespaced_pod("cnvrg", label_selector="app=app")
        self.assertEqual(1, len(pod.items))
        self.assertIn("nodes are available", pod.items[0].status.conditions[0].message)

    def test_es(self):
        v1 = client.CoreV1Api()
        pod = v1.list_namespaced_pod("cnvrg", label_selector="app=elasticsearch")
        self.assertEqual(1, len(pod.items))
        self.assertIn("nodes are available", pod.items[0].status.conditions[0].message)

    def test_kibana(self):
        v1 = client.CoreV1Api()
        pod = v1.list_namespaced_pod("cnvrg", label_selector="app=kibana")
        self.assertEqual(1, len(pod.items))
        self.assertIn("nodes are available", pod.items[0].status.conditions[0].message)

    def test_prom_operator(self):
        v1 = client.CoreV1Api()
        pod = v1.list_namespaced_pod("cnvrg", label_selector="app.kubernetes.io/name=prometheus-operator")
        self.assertEqual(1, len(pod.items))
        self.assertIn("nodes are available", pod.items[0].status.conditions[0].message)

    def test_prom_instance(self):
        v1 = client.CoreV1Api()
        pod = v1.list_namespaced_pod("cnvrg", label_selector="app=prometheus")
        self.assertEqual(1, len(pod.items))
        self.assertIn("nodes are available", pod.items[0].status.conditions[0].message)

    def test_minio(self):
        v1 = client.CoreV1Api()
        pod = v1.list_namespaced_pod("cnvrg", label_selector="app=minio")
        self.assertEqual(1, len(pod.items))
        self.assertIn("nodes are available", pod.items[0].status.conditions[0].message)

    def test_mpi_operator(self):
        v1 = client.CoreV1Api()
        pod = v1.list_namespaced_pod("cnvrg", label_selector="app=mpi-operator")
        self.assertEqual(1, len(pod.items))
        self.assertIn("nodes are available", pod.items[0].status.conditions[0].message)

    def test_redis(self):
        v1 = client.CoreV1Api()
        pod = v1.list_namespaced_pod("cnvrg", label_selector="app=redis")
        self.assertEqual(1, len(pod.items))
        self.assertIn("nodes are available", pod.items[0].status.conditions[0].message)

    def test_grafana(self):
        v1 = client.CoreV1Api()
        pod = v1.list_namespaced_pod("cnvrg", label_selector="app=grafana")
        self.assertEqual(1, len(pod.items))
        self.assertIn("nodes are available", pod.items[0].status.conditions[0].message)

    def test_cnvrg_routing(self):
        v1 = client.CoreV1Api()
        pod = v1.list_namespaced_pod("cnvrg", label_selector="app=routing-service")
        self.assertEqual(1, len(pod.items))
        self.assertIn("nodes are available", pod.items[0].status.conditions[0].message)

    def test_minio_exporter(self):
        v1 = client.CoreV1Api()
        pod = v1.list_namespaced_pod("cnvrg", label_selector="app=minio-exporter-token")
        self.assertEqual(1, len(pod.items))
        self.assertIn("nodes are available", pod.items[0].status.conditions[0].message)

    def test_nfs_client(self):
        v1 = client.CoreV1Api()
        pod = v1.list_namespaced_pod("cnvrg", label_selector="app=nfs-client-provisioner")
        self.assertEqual(1, len(pod.items))
        self.assertIn("nodes are available", pod.items[0].status.conditions[0].message)

    def test_istio_operator(self):
        v1 = client.CoreV1Api()
        pod = v1.list_namespaced_pod("cnvrg", label_selector="name=istio-operator")
        self.assertEqual(1, len(pod.items))
        self.assertIn("nodes are available", pod.items[0].status.conditions[0].message)
