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
    image: "cnvrg/core:3.1.3"
    intercom: "false"
  cnvrgRouter:
    enabled: "true"
  pgBackup:
    enabled: "true"
  vpa:
    enabled: "true"
"""

CNVRG_SPEC_WITH_TOLERATION = """
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
    dedicatedNodes: "true"
  cnvrgApp:
    enabled: "true"
    image: "cnvrg/core:3.1.2"
    customAgentTag: "false"
    intercom: "false"
  cnvrgRouter:
    enabled: "true"
  redis:
    enabled: "true"
  pg:
    enabled: "true"
  es:
    enabled: "true"
  minio:
    enabled: "true"
  prometheus:
    enabled: "true"
  istio:
    enabled: "true"
  kibana:
    enabled: "true"
  fluentd:
    enabled: "true"
  nvidiadp:
    enabled: "false"
  mpi:
    enabled: "true"
  vpa:
    enabled: "true"
"""

CNVRG_SPEC_WITH_TOLERATION_ISTIO_ONLY = """
apiVersion: mlops.cnvrg.io/v1
kind: CnvrgApp
metadata:
  name: cnvrg-app
  namespace: cnvrg
spec:
  ingressType: "istio"
  clusterDomain: "__CLUSTER_DOMAIN__"
  tenancy:
    enabled: "true"
    dedicatedNodes: "true"
  istio:
    enabled: "true"
  mpi:
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
  kibana:
    enabled: "false"
  fluentd:
    enabled: "false"
  nvidiadp:
    enabled: "false"
"""

CNVRG_SPEC_WITH_TOLERATION_HOSTPATH = """
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
    dedicatedNodes: "true"
  minio:
    enabled: "true"
    storageSize: "1Gi"
  prometheus:
    enabled: "true"
    storageSize: "1Gi"
  es:
    enabled: "true"
    storageSize: "1Gi"
  pg:
    enabled: "true"
    storageSize: "1Gi"
  hostpath:
    enabled: "true"
    nodeName: "__NODE_NAME__"
  conf:
    enabled: "true"
  cnvrgApp:
    enabled: "true"
    image: "cnvrg/core:core-3.4.1-10-300"
    customAgentTag: "false"
    intercom: "false"
  mpi:
    enabled: "false"
  pgBackup:
    enabled: "true"
  kibana:
    enabled: "false"
  fluentd:
    enabled: "false"
  nvidiadp:
    enabled: "false"
  vpa:
    enabled: "true"
"""


class CnvrgTaintsNoTaintsSetTest(unittest.TestCase, CommonBase):

    @classmethod
    def setUpClass(cls):
        cls.deploy()
        cls.create_cnvrg_spec(CNVRG_SPEC.replace("__CLUSTER_DOMAIN__", cls.get_nip_nip_url()))
        cls.wait_for_cnvrg_spec_ready()

    @classmethod
    def tearDownClass(cls):
        cls.delete_cnvrg_spec()
        cls.undeploy()

    def test_pg(self):
        v1 = client.CoreV1Api()
        pod = v1.list_namespaced_pod("cnvrg", label_selector="app=postgres")
        self.assertEqual(1, len(pod.items))
        self.assertIsNotNone(pod.items[0].status.conditions[0].message)
        self.assertIn("nodes are available", pod.items[0].status.conditions[0].message)

    def test_app(self):
        v1 = client.CoreV1Api()
        pod = v1.list_namespaced_pod("cnvrg", label_selector="app=app")
        self.assertEqual(1, len(pod.items))
        self.assertIsNotNone(pod.items[0].status.conditions[0].message)
        self.assertIn("nodes are available", pod.items[0].status.conditions[0].message)

    def test_es(self):
        v1 = client.CoreV1Api()
        pod = v1.list_namespaced_pod("cnvrg", label_selector="app=elasticsearch")
        self.assertEqual(1, len(pod.items))
        self.assertIsNotNone(pod.items[0].status.conditions[0].message)
        self.assertIn("nodes are available", pod.items[0].status.conditions[0].message)

    def test_kibana(self):
        v1 = client.CoreV1Api()
        pod = v1.list_namespaced_pod("cnvrg", label_selector="app=kibana")
        self.assertEqual(1, len(pod.items))
        self.assertIsNotNone(pod.items[0].status.conditions[0].message)
        self.assertIn("nodes are available", pod.items[0].status.conditions[0].message)

    def test_prom_operator(self):
        v1 = client.CoreV1Api()
        pod = v1.list_namespaced_pod("cnvrg", label_selector="app.kubernetes.io/name=prometheus-operator")
        self.assertEqual(1, len(pod.items))
        self.assertIn("nodes are available", pod.items[0].status.conditions[0].message)

    def test_minio(self):
        v1 = client.CoreV1Api()
        pod = v1.list_namespaced_pod("cnvrg", label_selector="app=minio")
        self.assertEqual(1, len(pod.items))
        self.assertIsNotNone(pod.items[0].status.conditions[0].message)
        self.assertIn("nodes are available", pod.items[0].status.conditions[0].message)

    def test_mpi_operator(self):
        v1 = client.CoreV1Api()
        pod = v1.list_namespaced_pod("cnvrg", label_selector="app=mpi-operator")
        self.assertEqual(1, len(pod.items))
        self.assertIsNotNone(pod.items[0].status.conditions[0].message)
        self.assertIn("nodes are available", pod.items[0].status.conditions[0].message)

    def test_redis(self):
        v1 = client.CoreV1Api()
        pod = v1.list_namespaced_pod("cnvrg", label_selector="app=redis")
        self.assertEqual(1, len(pod.items))
        self.assertIsNotNone(pod.items[0].status.conditions[0].message)
        self.assertIn("nodes are available", pod.items[0].status.conditions[0].message)

    def test_grafana(self):
        v1 = client.CoreV1Api()
        pod = v1.list_namespaced_pod("cnvrg", label_selector="app=grafana")
        self.assertEqual(1, len(pod.items))
        self.assertIsNotNone(pod.items[0].status.conditions[0].message)
        self.assertIn("nodes are available", pod.items[0].status.conditions[0].message)

    def test_kube_state_metrics(self):
        v1 = client.CoreV1Api()
        pod = v1.list_namespaced_pod("cnvrg", label_selector="app.kubernetes.io/name=kube-state-metrics")
        self.assertEqual(1, len(pod.items))
        self.assertIsNotNone(pod.items[0].status.conditions[0].message)
        self.assertIn("nodes are available", pod.items[0].status.conditions[0].message)

    def test_cnvrg_routing(self):
        v1 = client.CoreV1Api()
        pod = v1.list_namespaced_pod("cnvrg", label_selector="app=routing-service")
        self.assertEqual(1, len(pod.items))
        self.assertIsNotNone(pod.items[0].status.conditions[0].message)
        self.assertIn("nodes are available", pod.items[0].status.conditions[0].message)

    def test_vpa_recommender(self):
        cmd = "kubectl wait --for=condition=ready pod -l app=vpa-recommender -ncnvrg --timeout=300s"
        res = self.exec_cmd(cmd)
        self.assertEqual(0, res[0])

    def test_vpa_admission_controller(self):
        cmd = "kubectl wait --for=condition=ready pod -l app=vpa-admission-controller -ncnvrg --timeout=300s"
        res = self.exec_cmd(cmd)
        self.assertEqual(0, res[0])

    def test_vpa_updater(self):
        cmd = "kubectl wait --for=condition=ready pod -l app=vpa-updater -ncnvrg --timeout=300s"
        res = self.exec_cmd(cmd)
        self.assertEqual(0, res[0])

class CnvrgTaintsAreSetDedicatedNodesFalseTest(unittest.TestCase, CommonBase):

    @classmethod
    def setUpClass(cls):
        cls.get_nip_nip_url()
        cls.deploy()
        cls._exec_cmd("kubectl label nodes cnvrg-taint=true --all --overwrite")
        cls._exec_cmd("kubectl create deployment --image=nginx -ncnvrg test-nginx")
        cls.create_cnvrg_spec(CNVRG_SPEC.replace("__CLUSTER_DOMAIN__", cls.get_nip_nip_url()))
        cls.wait_for_cnvrg_spec_ready()

    @classmethod
    def tearDownClass(cls):
        cls._exec_cmd("kubectl label node cnvrg-taint- --all")
        cls.delete_cnvrg_spec()
        cls.undeploy()

    def test_app(self):
        cmd = "kubectl wait --for=condition=ready pod -l app=app -ncnvrg --timeout=300s"
        res = self.exec_cmd(cmd)
        self.assertEqual(0, res[0])

    def test_pg(self):
        cmd = "kubectl wait --for=condition=ready pod -l app=postgres -ncnvrg --timeout=300s"
        res = self.exec_cmd(cmd)
        self.assertEqual(0, res[0])

    def test_es(self):
        cmd = "kubectl wait --for=condition=ready pod -l app=elasticsearch -ncnvrg --timeout=300s"
        res = self.exec_cmd(cmd)
        self.assertEqual(0, res[0])

    def test_kibana(self):
        cmd = "kubectl wait --for=condition=ready pod -l app=kibana -ncnvrg --timeout=300s"
        res = self.exec_cmd(cmd)
        self.assertEqual(0, res[0])

    def test_prom_operator(self):
        cmd = "kubectl wait --for=condition=ready pod -l app.kubernetes.io/name=prometheus-operator -ncnvrg --timeout=300s"
        res = self.exec_cmd(cmd)
        self.assertEqual(0, res[0])

    def test_minio(self):
        cmd = "kubectl wait --for=condition=ready pod -l app=minio -ncnvrg --timeout=300s"
        res = self.exec_cmd(cmd)
        self.assertEqual(0, res[0])

    def test_mpi_operator(self):
        cmd = "kubectl wait --for=condition=ready pod -l app=mpi-operator -ncnvrg --timeout=300s"
        res = self.exec_cmd(cmd)
        self.assertEqual(0, res[0])

    def test_redis(self):
        cmd = "kubectl wait --for=condition=ready pod -l app=redis -ncnvrg --timeout=300s"
        res = self.exec_cmd(cmd)
        self.assertEqual(0, res[0])

    def test_grafana(self):
        cmd = "kubectl wait --for=condition=ready pod -l app=grafana -ncnvrg --timeout=300s"
        res = self.exec_cmd(cmd)
        self.assertEqual(0, res[0])

    def test_kube_state_metrics(self):
        cmd = "kubectl wait --for=condition=ready pod -l app.kubernetes.io/name=kube-state-metrics -ncnvrg --timeout=300s"
        res = self.exec_cmd(cmd)
        self.assertEqual(0, res[0])

    def test_cnvrg_routing(self):
        cmd = "kubectl wait --for=condition=ready pod -l app=routing-service -ncnvrg --timeout=300s"
        res = self.exec_cmd(cmd)
        self.assertEqual(0, res[0])

    def test_custom_nginx_deploy(self):
        cmd = "kubectl wait --for=condition=ready pod -l app=test-nginx -ncnvrg --timeout=300s"
        res = self.exec_cmd(cmd)
        self.assertEqual(0, res[0])

    def test_vpa_recommender(self):
        cmd = "kubectl wait --for=condition=ready pod -l app=vpa-recommender -ncnvrg --timeout=300s"
        res = self.exec_cmd(cmd)
        self.assertEqual(0, res[0])

    def test_vpa_admission_controller(self):
        cmd = "kubectl wait --for=condition=ready pod -l app=vpa-admission-controller -ncnvrg --timeout=300s"
        res = self.exec_cmd(cmd)
        self.assertEqual(0, res[0])

    def test_vpa_updater(self):
        cmd = "kubectl wait --for=condition=ready pod -l app=vpa-updater -ncnvrg --timeout=300s"
        res = self.exec_cmd(cmd)
        self.assertEqual(0, res[0])


class CnvrgTaintsAreSetDedicatedNodesTrueTest(unittest.TestCase, CommonBase):

    @classmethod
    def setUpClass(cls):
        cls.get_nip_nip_url()
        cls.deploy()
        cls._exec_cmd("kubectl label nodes cnvrg-taint=true --all --overwrite")
        cls._exec_cmd("kubectl taint nodes cnvrg-taint=true:NoSchedule --all")
        cls._exec_cmd("kubectl create deployment --image=nginx -ncnvrg test-nginx")
        cls.create_cnvrg_spec(CNVRG_SPEC_WITH_TOLERATION.replace("__CLUSTER_DOMAIN__", cls.get_nip_nip_url()))
        cls.wait_for_cnvrg_spec_ready()

    @classmethod
    def tearDownClass(cls):
        cls._exec_cmd("kubectl label node cnvrg-taint- --all")
        cls._exec_cmd("kubectl taint nodes cnvrg-taint- --all")
        cls.delete_cnvrg_spec()
        cls.undeploy()

    def test_app(self):
        cmd = "kubectl wait --for=condition=ready pod -l app=app -ncnvrg --timeout=300s"
        res = self.exec_cmd(cmd)
        self.assertEqual(0, res[0])

    def test_pg(self):
        cmd = "kubectl wait --for=condition=ready pod -l app=postgres -ncnvrg --timeout=300s"
        res = self.exec_cmd(cmd)
        self.assertEqual(0, res[0])

    def test_es(self):
        cmd = "kubectl wait --for=condition=ready pod -l app=elasticsearch -ncnvrg --timeout=300s"
        res = self.exec_cmd(cmd)
        self.assertEqual(0, res[0])

    def test_kibana(self):
        cmd = "kubectl wait --for=condition=ready pod -l app=kibana -ncnvrg --timeout=300s"
        res = self.exec_cmd(cmd)
        self.assertEqual(0, res[0])

    def test_prom_operator(self):
        cmd = "kubectl wait --for=condition=ready pod -l app.kubernetes.io/name=prometheus-operator -ncnvrg --timeout=300s"
        res = self.exec_cmd(cmd)
        self.assertEqual(0, res[0])

    def test_minio(self):
        cmd = "kubectl wait --for=condition=ready pod -l app=minio -ncnvrg --timeout=300s"
        res = self.exec_cmd(cmd)
        self.assertEqual(0, res[0])

    def test_mpi_operator(self):
        cmd = "kubectl wait --for=condition=ready pod -l app=mpi-operator -ncnvrg --timeout=300s"
        res = self.exec_cmd(cmd)
        self.assertEqual(0, res[0])

    def test_redis(self):
        cmd = "kubectl wait --for=condition=ready pod -l app=redis -ncnvrg --timeout=300s"
        res = self.exec_cmd(cmd)
        self.assertEqual(0, res[0])

    def test_grafana(self):
        cmd = "kubectl wait --for=condition=ready pod -l app=grafana -ncnvrg --timeout=300s"
        res = self.exec_cmd(cmd)
        self.assertEqual(0, res[0])

    def test_kube_state_metrics(self):
        cmd = "kubectl wait --for=condition=ready pod -l app.kubernetes.io/name=kube-state-metrics -ncnvrg --timeout=300s"
        res = self.exec_cmd(cmd)
        self.assertEqual(0, res[0])

    def test_cnvrg_routing(self):
        cmd = "kubectl wait --for=condition=ready pod -l app=routing-service -ncnvrg --timeout=300s"
        res = self.exec_cmd(cmd)
        self.assertEqual(0, res[0])

    def test_custom_nginx_deploy(self):
        v1 = client.CoreV1Api()
        pod = v1.list_namespaced_pod("cnvrg", label_selector="app=test-nginx")
        self.assertEqual(1, len(pod.items))
        self.assertIsNotNone(pod.items[0].status.conditions[0].message)
        self.assertIn("nodes are available", pod.items[0].status.conditions[0].message)

    def test_vpa_recommender(self):
        v1 = client.CoreV1Api()
        pod = v1.list_namespaced_pod("cnvrg", label_selector="app=vpa-recommender")
        self.assertEqual(1, len(pod.items))
        self.assertIsNotNone(pod.items[0].status.conditions[0].message)
        self.assertIn("nodes are available", pod.items[0].status.conditions[0].message)

    def test_vpa_admission_controller(self):
        v1 = client.CoreV1Api()
        pod = v1.list_namespaced_pod("cnvrg", label_selector="app=vpa-admission-controller")
        self.assertEqual(1, len(pod.items))
        self.assertIsNotNone(pod.items[0].status.conditions[0].message)
        self.assertIn("nodes are available", pod.items[0].status.conditions[0].message)

    def test_vpa_updater(self):
        v1 = client.CoreV1Api()
        pod = v1.list_namespaced_pod("cnvrg", label_selector="app=vpa-updater")
        self.assertEqual(1, len(pod.items))
        self.assertIsNotNone(pod.items[0].status.conditions[0].message)
        self.assertIn("nodes are available", pod.items[0].status.conditions[0].message)

class CnvrgTaintsAreSetDedicatedNodesTrueIstioOnlyTest(unittest.TestCase, CommonBase):

    @classmethod
    def setUpClass(cls):
        cls.deploy()
        cls._exec_cmd("kubectl label nodes cnvrg-taint=true --all --overwrite")
        cls._exec_cmd("kubectl taint nodes cnvrg-taint=true:NoSchedule --all")
        cls._exec_cmd("kubectl create deployment --image=nginx -ncnvrg test-nginx")
        cls.create_cnvrg_spec(
            CNVRG_SPEC_WITH_TOLERATION_ISTIO_ONLY.replace("__CLUSTER_DOMAIN__", cls.get_nip_nip_url()))
        cls.wait_for_cnvrg_spec_ready()

    @classmethod
    def tearDownClass(cls):
        cls._exec_cmd("kubectl label node cnvrg-taint- --all")
        cls._exec_cmd("kubectl taint nodes cnvrg-taint- --all")
        cls.delete_cnvrg_spec()
        cls.undeploy()

    def test_istiod_deployment(self):
        cmd = "kubectl wait --for=condition=ready pod -l app=istiod -ncnvrg --timeout=300s"
        res = self.exec_cmd(cmd)
        self.assertEqual(0, res[0])

    def test_istio_ingress_deployment(self):
        cmd = "kubectl wait --for=condition=ready pod -l app=istio-ingressgateway -ncnvrg --timeout=300s"
        res = self.exec_cmd(cmd)
        self.assertEqual(0, res[0])


class CnvrgTaintsAreSetDedicatedNodesTrueHostpathTest(unittest.TestCase, CommonBase):

    @classmethod
    def setUpClass(cls):
        res = cls._exec_cmd("kubectl get nodes -ojson | jq -r .items[0].metadata.name")
        node_name = res[1]
        cls.deploy()
        cls._exec_cmd("kubectl label nodes cnvrg-taint=true --all --overwrite")
        cls._exec_cmd("kubectl taint nodes cnvrg-taint=true:NoSchedule --all")
        spec = CNVRG_SPEC_WITH_TOLERATION_HOSTPATH.replace("__CLUSTER_DOMAIN__", cls.get_nip_nip_url())
        spec = spec.replace("__NODE_NAME__", node_name)
        cls.create_cnvrg_spec(spec)
        cls.wait_for_cnvrg_spec_ready()

    @classmethod
    def tearDownClass(cls):
        cls._exec_cmd("kubectl label node cnvrg-taint- --all")
        cls._exec_cmd("kubectl taint nodes cnvrg-taint- --all")
        cls.delete_cnvrg_spec()
        cls.undeploy()

    def test_pg_deployment(self):
        cmd = "kubectl wait --for=condition=ready pod -l app=postgres -ncnvrg --timeout=300s"
        res = self.exec_cmd(cmd)
        self.assertEqual(0, res[0])

    def test_app(self):
        cmd = "kubectl wait --for=condition=ready pod -l app=app -ncnvrg --timeout=300s"
        res = self.exec_cmd(cmd)
        self.assertEqual(0, res[0])

    def test_es(self):
        cmd = "kubectl wait --for=condition=ready pod -l app=elasticsearch -ncnvrg --timeout=300s"
        res = self.exec_cmd(cmd)
        self.assertEqual(0, res[0])

    def test_grafana(self):
        cmd = "kubectl wait --for=condition=ready pod -l app=grafana -ncnvrg --timeout=300s"
        res = self.exec_cmd(cmd)
        self.assertEqual(0, res[0])

    def test_kube_state_metrics(self):
        cmd = "kubectl wait --for=condition=ready pod -l app.kubernetes.io/name=kube-state-metrics -ncnvrg --timeout=300s"
        res = self.exec_cmd(cmd)
        self.assertEqual(0, res[0])

    def test_hostpath_provisioner(self):
        cmd = "kubectl wait --for=condition=ready pod -l k8s-app=hostpath-provisioner -ncnvrg --timeout=300s"
        res = self.exec_cmd(cmd)
        self.assertEqual(0, res[0])

    def test_minio(self):
        cmd = "kubectl wait --for=condition=ready pod -l app=minio -ncnvrg --timeout=300s"
        res = self.exec_cmd(cmd)
        self.assertEqual(0, res[0])

    def test_prom_instance(self):
        cmd = "kubectl wait --for=condition=ready pod -l app=prometheus -ncnvrg --timeout=300s"
        res = self.exec_cmd(cmd)
        self.assertEqual(0, res[0])

    def test_prom_operator(self):
        cmd = "kubectl wait --for=condition=ready pod -l app.kubernetes.io/name=prometheus-operator -ncnvrg --timeout=300s"
        res = self.exec_cmd(cmd)
        self.assertEqual(0, res[0])

    def test_redis(self):
        cmd = "kubectl wait --for=condition=ready pod -l app=redis -ncnvrg --timeout=300s"
        res = self.exec_cmd(cmd)
        self.assertEqual(0, res[0])

    def test_sidekiq(self):
        cmd = "kubectl wait --for=condition=ready pod -l app=sidekiq -ncnvrg --timeout=300s"
        res = self.exec_cmd(cmd)
        self.assertEqual(0, res[0])

    def test_sidekiq_searchkick(self):
        cmd = "kubectl wait --for=condition=ready pod -l app=sidekiq-searchkick -ncnvrg --timeout=300s"
        res = self.exec_cmd(cmd)
        self.assertEqual(0, res[0])

    def test_vpa_recommender(self):
        cmd = "kubectl wait --for=condition=ready pod -l app=vpa-recommender -ncnvrg --timeout=300s"
        res = self.exec_cmd(cmd)
        self.assertEqual(0, res[0])

    def test_vpa_admission_controller(self):
        cmd = "kubectl wait --for=condition=ready pod -l app=vpa-admission-controller -ncnvrg --timeout=300s"
        res = self.exec_cmd(cmd)
        self.assertEqual(0, res[0])

    def test_vpa_updater(self):
        cmd = "kubectl wait --for=condition=ready pod -l app=vpa-updater -ncnvrg --timeout=300s"
        res = self.exec_cmd(cmd)
        self.assertEqual(0, res[0])