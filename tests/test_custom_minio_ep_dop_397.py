import unittest
import os
from common import CommonBase
from kubernetes import client, config
import logging

config.load_kube_config()


class CnvrgMpiOperatorDop395Test(unittest.TestCase, CommonBase):

    @classmethod
    def setUpClass(cls):
        cls.deploy()
        helm_cmd = "helm template ../chart/ -s templates/cnvrg-app.yaml"
        cls.create_cnvrg_spec(cls.get_spec_from_chart(helm_cmd))
        cls.wait_for_cnvrg_spec_ready()

    @classmethod
    def tearDownClass(cls):
        if os.getenv("RUN_TEARDOWN", "true") == "true":
            cls.delete_cnvrg_spec()
            cls.undeploy()

    def test_mpi_operator_pod_deployed(self):
        v1 = client.CoreV1Api()
        pod = v1.list_namespaced_pod("cnvrg", label_selector="app=mpi-operator")
        self.assertEqual(1, len(pod.items))

    def test_mpi_operator_pod_ready(self):
        cmd = "kubectl wait --for=condition=ready pod -l app=mpi-operator -ncnvrg --timeout=120s"
        ret_code = self.exec_cmd(cmd)
        self.assertEqual(0, ret_code)
