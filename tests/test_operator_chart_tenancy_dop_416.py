import unittest
import os
from common import CommonBase
from kubernetes import client, config

config.load_kube_config()


class TaintsOperatorDeploymentTest(unittest.TestCase, CommonBase):
    @classmethod
    def setUpClass(cls):
        cls._exec_cmd("kubectl create ns cnvrg")
        cls._exec_cmd("kubectl label nodes cnvrg-taint=true --all --overwrite")
        cls._exec_cmd("kubectl taint nodes cnvrg-taint=true:NoSchedule --all")


    @classmethod
    def tearDownClass(cls):
        cls._exec_cmd("kubectl label node cnvrg-taint- --all")
        cls._exec_cmd("kubectl taint nodes cnvrg-taint- --all")
        cls.undeploy()

    def test_app_ready_aks_istio(self):
        cmd = 'helm template chart --set tenancy.enabled="true" --include-crds --no-hooks | VERSION=$TAG envsubst | kubectl create -f -'
        self.exec_cmd(cmd)
        cmd = "kubectl wait --for=condition=ready pod -l control-plane=cnvrg-operator -ncnvrg --timeout=300s"
        res = self.exec_cmd(cmd)
        self.assertEqual(0, res[0])
