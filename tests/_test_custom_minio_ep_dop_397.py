import unittest
import time
from common import CommonBase
from kubernetes import config
import logging

config.load_kube_config()


class MinioCustomEPDop397Test(unittest.TestCase, CommonBase):

    @classmethod
    def setUpClass(cls):
        logging.info("starting -> MinioCustomEPDop397Test")
        cls._started_at = time.time()
        cls.deploy()
        helm_cmd = """
            helm template chart \
            --set otags="cnvrgApp" \
            --set cnvrgApp.conf.cnvrgStorageEndpoint='http://custom-minio-ep' \
            -s templates/cnvrg-app.yaml
        """
        cls.create_cnvrg_spec(cls.get_spec_from_chart(helm_cmd))
        cls.wait_for_cnvrg_spec_ready()

    @classmethod
    def tearDownClass(cls):
        cls.delete_cnvrg_spec()
        cls.undeploy()
        cls.log_total_test_execution_time(cls._started_at, "MinioCustomEPDop397Test")

    def test_custom_cnvrg_storage(self):
        cmd = "kubectl get secret env-secrets -ncnvrg -ojson | jq -r .data.CNVRG_STORAGE_ENDPOINT | base64 -d"
        res = self.exec_cmd(cmd)
        self.assertEqual("http://custom-minio-ep", res[1])
