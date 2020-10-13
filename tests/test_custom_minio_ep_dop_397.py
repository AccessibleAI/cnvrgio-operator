import unittest
import os
from common import CommonBase
from kubernetes import client, config
import logging

config.load_kube_config()


class MinioCustomEPDop397Test(unittest.TestCase, CommonBase):

    @classmethod
    def setUpClass(cls):
        cls.deploy()
        helm_cmd = """
            helm template ../chart \
            --set appSecrets.cnvrgStorageEndpoint='http://custom-minio-ep' \
            --set cnvrgApp.enabled="false" \
            --set autoscaler.enabled="false" \
            --set cnvrgRouter.enabled="false" \
            --set es.enabled="false" \
            --set fluentd.enabled="false" \
            --set hostpath.enabled="false" \
            --set ingress.enabled="false" \
            --set istio.enabled="false" \
            --set kibana.enabled="false" \
            --set prometheus.enabled="false" \
            --set minio.enabled="false" \
            --set mpi.enabled="false" \
            --set nfs.enabled="false" \
            --set nvidiadp.enabled="false" \
            --set pg.enabled="false" \
            --set redis.enabled="false" \
            -s templates/cnvrg-app.yaml
        """
        cls.create_cnvrg_spec(cls.get_spec_from_chart(helm_cmd))
        cls.wait_for_cnvrg_spec_ready()

    @classmethod
    def tearDownClass(cls):
        cls.delete_cnvrg_spec()
        cls.undeploy()

    def test_mpi_operator_pod_deployed(self):
        cmd = "kubectl get secret env-secrets -ncnvrg -ojson | jq -r .data.CNVRG_STORAGE_ENDPOINT | base64 -d"
        res = self.exec_cmd(cmd)
        self.assertEqual("http://custom-minio-ep", res[1])
