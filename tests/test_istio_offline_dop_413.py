import unittest
import time
from common import CommonBase
from kubernetes import config

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
    externalIp: "1.1.1.1;2.2.2.2;3.3.3.3"
    ingressSvcAnnotations: "service.beta.kubernetes.io/aws-load-balancer-backend-protocol: tcp; service.beta.kubernetes.io/aws-load-balancer-internal: true"
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


class IstioExternalIpsAndServiceAnnotationsTest(unittest.TestCase, CommonBase):

    @classmethod
    def setUpClass(cls):
        cls._started_at = time.time()
        cls.deploy()
        cls.create_cnvrg_spec(CNVRG_SPEC_ISTIO_ONLY)
        if cls.wait_for_cnvrg_spec_ready() is False:
            assert False, 'CnvrgApp Spec was not ready in 30 min!'

    @classmethod
    def tearDownClass(cls):
        cls.delete_cnvrg_spec()
        cls.undeploy()
        cls.log_total_test_execution_time(cls._started_at, "IstioExternalIpsAndServiceAnnotationsTest")

    def test_istio_ingress_service_annotations1(self):
        cmd = "kubectl wait --for=condition=ready pod -l app=istio-ingressgateway -ncnvrg --timeout=300s"
        res = self.exec_cmd(cmd)
        self.assertEqual(0, res[0])
        cmd = "kubectl get svc istio-ingressgateway -ncnvrg  -ojson | jq -r '.metadata.annotations.\"service.beta.kubernetes.io/aws-load-balancer-backend-protocol\"'"
        res = self.exec_cmd(cmd)
        self.assertEqual("tcp", res[1])

    def test_istio_ingress_service_annotations2(self):
        cmd = "kubectl wait --for=condition=ready pod -l app=istio-ingressgateway -ncnvrg --timeout=300s"
        res = self.exec_cmd(cmd)
        self.assertEqual(0, res[0])
        cmd = "kubectl get svc istio-ingressgateway -ncnvrg  -ojson | jq -r '.metadata.annotations.\"service.beta.kubernetes.io/aws-load-balancer-internal\"'"
        res = self.exec_cmd(cmd)
        self.assertEqual("true", res[1])

    def test_istio_ingress_service_external_ips(self):
        cmd = "kubectl wait --for=condition=ready pod -l app=istio-ingressgateway -ncnvrg --timeout=300s"
        res = self.exec_cmd(cmd)
        self.assertEqual(0, res[0])
        cmd = "kubectl get svc istio-ingressgateway -ncnvrg  -ojson | jq -rc .spec.externalIPs"
        res = self.exec_cmd(cmd)
        self.assertEqual('["1.1.1.1","2.2.2.2","3.3.3.3"]', res[1])
