import unittest
from common import CommonBase
import yaml


class ComputeProfilesLargeWithHelmChartTest(unittest.TestCase, CommonBase):
    SPEC = ""
    VALUES = ""
    PROFILE = "large"

    @classmethod
    def setUpClass(cls):
        cmd = "helm template chart -s templates/cnvrg-app.yaml --set computeProfile=large"
        res = cls._exec_cmd(cmd)
        cls.SPEC = yaml.load(res[1], Loader=yaml.FullLoader)
        res = cls._exec_cmd("helm show values chart")
        cls.VALUES = yaml.load(res[1], Loader=yaml.FullLoader)

    def test_large_profile_webapp_cpu(self):
        self.assertEqual(
            str(self.VALUES['computeProfiles'][self.PROFILE]['cnvrgApp']['webappCpu']),
            str(self.SPEC['spec']['cnvrgApp']['cpu']))

    def test_large_profile_webapp_memory(self):
        self.assertEqual(
            str(self.VALUES['computeProfiles'][self.PROFILE]['cnvrgApp']['webappMemory']),
            str(self.SPEC['spec']['cnvrgApp']['memory']))

    def test_large_profile_sidekiq_cpu(self):
        self.assertEqual(
            str(self.VALUES['computeProfiles'][self.PROFILE]['cnvrgApp']['sidekiqCpu']),
            str(self.SPEC['spec']['cnvrgApp']['sidekiqCpu']))

    def test_large_profile_sidekiq_memory(self):
        self.assertEqual(
            str(self.VALUES['computeProfiles'][self.PROFILE]['cnvrgApp']['sidekiqMemory']),
            str(self.SPEC['spec']['cnvrgApp']['sidekiqMemory']))

    def test_large_profile_pg_cpu(self):
        self.assertEqual(
            str(self.VALUES['computeProfiles'][self.PROFILE]['pg']['cpu']),
            str(self.SPEC['spec']['pg']['cpuRequest']))

    def test_large_profile_pg_memory(self):
        self.assertEqual(
            str(self.VALUES['computeProfiles'][self.PROFILE]['pg']['memory']),
            str(self.SPEC['spec']['pg']['memoryRequest']))

    def test_large_profile_minio_cpu(self):
        self.assertEqual(
            str(self.VALUES['computeProfiles'][self.PROFILE]['minio']['cpu']),
            str(self.SPEC['spec']['minio']['cpuRequest']))

    def test_large_profile_minio_memory(self):
        self.assertEqual(
            str(self.VALUES['computeProfiles'][self.PROFILE]['minio']['memory']),
            str(self.SPEC['spec']['minio']['memoryRequest']))

    def test_large_profile_es_cpu(self):
        component = "es"
        self.assertEqual(
            str(self.VALUES['computeProfiles'][self.PROFILE][component]['cpu']),
            str(self.SPEC['spec'][component]['cpuRequest']))

    def test_large_profile_es_memory(self):
        component = "es"
        self.assertEqual(
            str(self.VALUES['computeProfiles'][self.PROFILE][component]['memory']),
            str(self.SPEC['spec'][component]['memoryRequest']))

    def test_large_profile_prometheus_cpu(self):
        component = "prometheus"
        self.assertEqual(
            str(self.VALUES['computeProfiles'][self.PROFILE][component]['cpu']),
            str(self.SPEC['spec'][component]['cpuRequest']))

    def test_large_profile_prometheus_memory(self):
        component = "prometheus"
        self.assertEqual(
            str(self.VALUES['computeProfiles'][self.PROFILE][component]['memory']),
            str(self.SPEC['spec'][component]['memoryRequest']))

    def test_large_profile_redis_cpu(self):
        component = "redis"
        self.assertEqual(
            str(self.VALUES['computeProfiles'][self.PROFILE][component]['cpu']),
            str(self.SPEC['spec'][component]['requests']['cpu']))

    def test_large_profile_redis_memory(self):
        component = "redis"
        self.assertEqual(
            str(self.VALUES['computeProfiles'][self.PROFILE][component]['memory']),
            str(self.SPEC['spec'][component]['requests']['memory']))


class ComputeProfilesMediumWithHelmChartTest(unittest.TestCase, CommonBase):
    SPEC = ""
    VALUES = ""
    PROFILE = "medium"

    @classmethod
    def setUpClass(cls):
        cmd = f"helm template chart -s templates/cnvrg-app.yaml --set computeProfile={cls.PROFILE}"
        res = cls._exec_cmd(cmd)
        cls.SPEC = yaml.load(res[1], Loader=yaml.FullLoader)
        res = cls._exec_cmd("helm show values chart")
        cls.VALUES = yaml.load(res[1], Loader=yaml.FullLoader)

    def test_medium_profile_webapp_cpu(self):
        self.assertEqual(
            str(self.VALUES['computeProfiles'][self.PROFILE]['cnvrgApp']['webappCpu']),
            str(self.SPEC['spec']['cnvrgApp']['cpu']))

    def test_medium_profile_webapp_memory(self):
        self.assertEqual(
            str(self.VALUES['computeProfiles'][self.PROFILE]['cnvrgApp']['webappMemory']),
            str(self.SPEC['spec']['cnvrgApp']['memory']))

    def test_medium_profile_sidekiq_cpu(self):
        self.assertEqual(
            str(self.VALUES['computeProfiles'][self.PROFILE]['cnvrgApp']['sidekiqCpu']),
            str(self.SPEC['spec']['cnvrgApp']['sidekiqCpu']))

    def test_medium_profile_sidekiq_memory(self):
        self.assertEqual(
            str(self.VALUES['computeProfiles'][self.PROFILE]['cnvrgApp']['sidekiqMemory']),
            str(self.SPEC['spec']['cnvrgApp']['sidekiqMemory']))

    def test_medium_profile_pg_cpu(self):
        self.assertEqual(
            str(self.VALUES['computeProfiles'][self.PROFILE]['pg']['cpu']),
            str(self.SPEC['spec']['pg']['cpuRequest']))

    def test_medium_profile_pg_memory(self):
        self.assertEqual(
            str(self.VALUES['computeProfiles'][self.PROFILE]['pg']['memory']),
            str(self.SPEC['spec']['pg']['memoryRequest']))

    def test_medium_profile_minio_cpu(self):
        self.assertEqual(
            str(self.VALUES['computeProfiles'][self.PROFILE]['minio']['cpu']),
            str(self.SPEC['spec']['minio']['cpuRequest']))

    def test_medium_profile_minio_memory(self):
        self.assertEqual(
            str(self.VALUES['computeProfiles'][self.PROFILE]['minio']['memory']),
            str(self.SPEC['spec']['minio']['memoryRequest']))

    def test_medium_profile_es_cpu(self):
        component = "es"
        self.assertEqual(
            str(self.VALUES['computeProfiles'][self.PROFILE][component]['cpu']),
            str(self.SPEC['spec'][component]['cpuRequest']))

    def test_medium_profile_es_memory(self):
        component = "es"
        self.assertEqual(
            str(self.VALUES['computeProfiles'][self.PROFILE][component]['memory']),
            str(self.SPEC['spec'][component]['memoryRequest']))

    def test_medium_profile_prometheus_cpu(self):
        component = "prometheus"
        self.assertEqual(
            str(self.VALUES['computeProfiles'][self.PROFILE][component]['cpu']),
            str(self.SPEC['spec'][component]['cpuRequest']))

    def test_medium_profile_prometheus_memory(self):
        component = "prometheus"
        self.assertEqual(
            str(self.VALUES['computeProfiles'][self.PROFILE][component]['memory']),
            str(self.SPEC['spec'][component]['memoryRequest']))

    def test_medium_profile_redis_cpu(self):
        component = "redis"
        self.assertEqual(
            str(self.VALUES['computeProfiles'][self.PROFILE][component]['cpu']),
            str(self.SPEC['spec'][component]['requests']['cpu']))

    def test_medium_profile_redis_memory(self):
        component = "redis"
        self.assertEqual(
            str(self.VALUES['computeProfiles'][self.PROFILE][component]['memory']),
            str(self.SPEC['spec'][component]['requests']['memory']))


class ComputeProfilesSmallWithHelmChartTest(unittest.TestCase, CommonBase):
    SPEC = ""
    VALUES = ""
    PROFILE = "small"

    @classmethod
    def setUpClass(cls):
        cmd = f"helm template chart -s templates/cnvrg-app.yaml --set computeProfile={cls.PROFILE}"
        res = cls._exec_cmd(cmd)
        cls.SPEC = yaml.load(res[1], Loader=yaml.FullLoader)
        res = cls._exec_cmd("helm show values chart")
        cls.VALUES = yaml.load(res[1], Loader=yaml.FullLoader)

    def test_medium_profile_webapp_cpu(self):
        self.assertEqual(
            str(self.VALUES['computeProfiles'][self.PROFILE]['cnvrgApp']['webappCpu']),
            str(self.SPEC['spec']['cnvrgApp']['cpu']))

    def test_medium_profile_webapp_memory(self):
        self.assertEqual(
            str(self.VALUES['computeProfiles'][self.PROFILE]['cnvrgApp']['webappMemory']),
            str(self.SPEC['spec']['cnvrgApp']['memory']))

    def test_medium_profile_sidekiq_cpu(self):
        self.assertEqual(
            str(self.VALUES['computeProfiles'][self.PROFILE]['cnvrgApp']['sidekiqCpu']),
            str(self.SPEC['spec']['cnvrgApp']['sidekiqCpu']))

    def test_medium_profile_sidekiq_memory(self):
        self.assertEqual(
            str(self.VALUES['computeProfiles'][self.PROFILE]['cnvrgApp']['sidekiqMemory']),
            str(self.SPEC['spec']['cnvrgApp']['sidekiqMemory']))

    def test_medium_profile_pg_cpu(self):
        self.assertEqual(
            str(self.VALUES['computeProfiles'][self.PROFILE]['pg']['cpu']),
            str(self.SPEC['spec']['pg']['cpuRequest']))

    def test_medium_profile_pg_memory(self):
        self.assertEqual(
            str(self.VALUES['computeProfiles'][self.PROFILE]['pg']['memory']),
            str(self.SPEC['spec']['pg']['memoryRequest']))

    def test_medium_profile_minio_cpu(self):
        self.assertEqual(
            str(self.VALUES['computeProfiles'][self.PROFILE]['minio']['cpu']),
            str(self.SPEC['spec']['minio']['cpuRequest']))

    def test_medium_profile_minio_memory(self):
        self.assertEqual(
            str(self.VALUES['computeProfiles'][self.PROFILE]['minio']['memory']),
            str(self.SPEC['spec']['minio']['memoryRequest']))

    def test_medium_profile_es_cpu(self):
        component = "es"
        self.assertEqual(
            str(self.VALUES['computeProfiles'][self.PROFILE][component]['cpu']),
            str(self.SPEC['spec'][component]['cpuRequest']))

    def test_medium_profile_es_memory(self):
        component = "es"
        self.assertEqual(
            str(self.VALUES['computeProfiles'][self.PROFILE][component]['memory']),
            str(self.SPEC['spec'][component]['memoryRequest']))

    def test_medium_profile_prometheus_cpu(self):
        component = "prometheus"
        self.assertEqual(
            str(self.VALUES['computeProfiles'][self.PROFILE][component]['cpu']),
            str(self.SPEC['spec'][component]['cpuRequest']))

    def test_medium_profile_prometheus_memory(self):
        component = "prometheus"
        self.assertEqual(
            str(self.VALUES['computeProfiles'][self.PROFILE][component]['memory']),
            str(self.SPEC['spec'][component]['memoryRequest']))

    def test_medium_profile_redis_cpu(self):
        component = "redis"
        self.assertEqual(
            str(self.VALUES['computeProfiles'][self.PROFILE][component]['cpu']),
            str(self.SPEC['spec'][component]['requests']['cpu']))

    def test_medium_profile_redis_memory(self):
        component = "redis"
        self.assertEqual(
            str(self.VALUES['computeProfiles'][self.PROFILE][component]['memory']),
            str(self.SPEC['spec'][component]['requests']['memory']))
