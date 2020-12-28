import unittest
import time
from common import CommonBase
from kubernetes import client, config
import logging

config.load_kube_config()


class TaintsOperatorDeploymentTest(unittest.TestCase, CommonBase):
    @classmethod
    def setUpClass(cls):
        logging.info("starting -> TaintsOperatorDeploymentTest")
        cls._started_at = time.time()
        cls._exec_cmd("kubectl create ns cnvrg")
        cls._exec_cmd("kubectl label nodes cnvrg=app --all --overwrite")
        cls._exec_cmd("kubectl taint nodes cnvrg=app:NoSchedule --all")

    @classmethod
    def tearDownClass(cls):
        cls._exec_cmd("kubectl label node cnvrg- --all")
        cls._exec_cmd("kubectl taint nodes cnvrg- --all")
        cls.undeploy()
        cls.log_total_test_execution_time(cls._started_at, "TaintsOperatorDeploymentTest")

    def test_app_ready_aks_istio(self):
        cmd = 'helm template chart --set tenancy.enabled="true" --include-crds --no-hooks | VERSION=$TAG envsubst | kubectl create -f -'
        self.exec_cmd(cmd)
        cmd = "kubectl wait --for=condition=ready pod -l control-plane=cnvrg-operator -ncnvrg --timeout=300s"
        res = self.exec_cmd(cmd)
        self.assertEqual(0, res[0])
