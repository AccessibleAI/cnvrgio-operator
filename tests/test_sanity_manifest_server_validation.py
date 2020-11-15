import unittest
from common import CommonBase
import yaml
from os import listdir
from os.path import isfile, join
import logging


class CnvrgAppReadinessTest(unittest.TestCase, CommonBase):
    MANIFESTS_PATH = "/tmp/t1"
    MANIFESTS = []

    @classmethod
    def setUpClass(cls):
        cls._exec_cmd(f"mkdir {cls.MANIFESTS_PATH}")
        params = f'{{"dump_dir":"{cls.MANIFESTS_PATH}","cnvrgApp":{{"image":"image"}},"debug":"true","dry_run":"true","ansible_operator_meta":{{"namespace":"cnvrg"}}'
        cmd = f"ansible-playbook playbooks/cnvrg.yml --extra-vars='{params}' --tags app"
        cls._exec_cmd(cmd)
        cls.MANIFESTS = [f for f in listdir(cls.MANIFESTS_PATH) if isfile(join(cls.MANIFESTS_PATH, f))]

    def test_app_create_dry_run(self):
        logging.info(self.MANIFESTS)
        pass
