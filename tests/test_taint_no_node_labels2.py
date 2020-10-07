
import unittest
from common import CommonBase
from kubernetes import client, config

config.load_kube_config()


class CnvrgTaintsTest2(unittest.TestCase, CommonBase):

    def test_something(self):
        self.assertEqual(True, True)
