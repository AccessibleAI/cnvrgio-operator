import unittest
from common import CommonBase
import yaml, time
import logging


class ComputeProfilesLargeWithHelmChartTest(unittest.TestCase, CommonBase):
    SPEC = ""
    VALUES = ""
    PROFILE = "large"

    @classmethod
    def setUpClass(cls):
        logging.info("starting -> ComputeProfilesLargeWithHelmChartTest")
        cls._started_at = time.time()
        cmd = "helm template chart -s templates/cnvrg-app.yaml --set computeProfile=large"
        res = cls._exec_cmd(cmd)
        cls.SPEC = yaml.load(res[1], Loader=yaml.FullLoader)
        res = cls._exec_cmd("helm show values chart")
        cls.VALUES = yaml.load(res[1], Loader=yaml.FullLoader)

    @classmethod
    def tearDownClass(cls):
        cls.log_total_test_execution_time(cls._started_at, "ComputeProfilesLargeWithHelmChartTest")

    def test_large_profile_webapp_cpu(self):
        self.assertEqual(
            str(self.VALUES['computeProfiles'][self.PROFILE]['cnvrgApp']['cpu']),
            str(self.SPEC['spec']['cnvrgApp']['cpu']))

    def test_large_profile_webapp_memory(self):
        self.assertEqual(
            str(self.VALUES['computeProfiles'][self.PROFILE]['cnvrgApp']['memory']),
            str(self.SPEC['spec']['cnvrgApp']['memory']))

    def test_large_profile_sidekiq_cpu(self):
        self.assertEqual(
            str(self.VALUES['computeProfiles'][self.PROFILE]['cnvrgApp']['sidekiq']['cpu']),
            str(self.SPEC['spec']['cnvrgApp']['sidekiq']['cpu']))

    def test_large_profile_sidekiq_memory(self):
        self.assertEqual(
            str(self.VALUES['computeProfiles'][self.PROFILE]['cnvrgApp']['sidekiq']['memory']),
            str(self.SPEC['spec']['cnvrgApp']['sidekiq']['memory']))

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
            str(self.SPEC['spec']['logging'][component]['cpuRequest']))

    def test_large_profile_es_memory(self):
        component = "es"
        self.assertEqual(
            str(self.VALUES['computeProfiles'][self.PROFILE][component]['memory']),
            str(self.SPEC['spec']['logging'][component]['memoryRequest']))

    def test_large_profile_prometheus_cpu(self):
        component = "monitoring"
        self.assertEqual(
            str(self.VALUES['computeProfiles'][self.PROFILE]['prometheus']['cpu']),
            str(self.SPEC['spec'][component]['prometheus']['cpuRequest']))

    def test_large_profile_prometheus_memory(self):
        component = "monitoring"
        self.assertEqual(
            str(self.VALUES['computeProfiles'][self.PROFILE]['prometheus']['memory']),
            str(self.SPEC['spec'][component]['prometheus']['memoryRequest']))

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
        cls._started_at = time.time()
        cmd = f"helm template chart -s templates/cnvrg-app.yaml --set computeProfile={cls.PROFILE}"
        res = cls._exec_cmd(cmd)
        cls.SPEC = yaml.load(res[1], Loader=yaml.FullLoader)
        res = cls._exec_cmd("helm show values chart")
        cls.VALUES = yaml.load(res[1], Loader=yaml.FullLoader)

    @classmethod
    def tearDownClass(cls):
        cls.log_total_test_execution_time(cls._started_at, "ComputeProfilesMediumWithHelmChartTest")

    def test_medium_profile_webapp_cpu(self):
        self.assertEqual(
            str(self.VALUES['computeProfiles'][self.PROFILE]['cnvrgApp']['cpu']),
            str(self.SPEC['spec']['cnvrgApp']['cpu']))

    def test_medium_profile_webapp_memory(self):
        self.assertEqual(
            str(self.VALUES['computeProfiles'][self.PROFILE]['cnvrgApp']['memory']),
            str(self.SPEC['spec']['cnvrgApp']['memory']))

    def test_medium_profile_sidekiq_cpu(self):
        self.assertEqual(
            str(self.VALUES['computeProfiles'][self.PROFILE]['cnvrgApp']['sidekiq']['cpu']),
            str(self.SPEC['spec']['cnvrgApp']['sidekiq']['cpu']))

    def test_medium_profile_sidekiq_memory(self):
        self.assertEqual(
            str(self.VALUES['computeProfiles'][self.PROFILE]['cnvrgApp']['sidekiq']['memory']),
            str(self.SPEC['spec']['cnvrgApp']['sidekiq']['memory']))

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
            str(self.SPEC['spec']['logging'][component]['cpuRequest']))

    def test_medium_profile_es_memory(self):
        component = "es"
        self.assertEqual(
            str(self.VALUES['computeProfiles'][self.PROFILE][component]['memory']),
            str(self.SPEC['spec']['logging'][component]['memoryRequest']))

    def test_medium_profile_prometheus_cpu(self):
        component = "monitoring"
        self.assertEqual(
            str(self.VALUES['computeProfiles'][self.PROFILE]['prometheus']['cpu']),
            str(self.SPEC['spec'][component]['prometheus']['cpuRequest']))

    def test_medium_profile_prometheus_memory(self):
        component = "monitoring"
        self.assertEqual(
            str(self.VALUES['computeProfiles'][self.PROFILE]['prometheus']['memory']),
            str(self.SPEC['spec'][component]['prometheus']['memoryRequest']))

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
        cls._started_at = time.time()
        cmd = f"helm template chart -s templates/cnvrg-app.yaml --set computeProfile={cls.PROFILE}"
        res = cls._exec_cmd(cmd)
        cls.SPEC = yaml.load(res[1], Loader=yaml.FullLoader)
        res = cls._exec_cmd("helm show values chart")
        cls.VALUES = yaml.load(res[1], Loader=yaml.FullLoader)

    @classmethod
    def tearDownClass(cls):
        cls.log_total_test_execution_time(cls._started_at, "ComputeProfilesSmallWithHelmChartTest")

    def test_small_profile_webapp_cpu(self):
        self.assertEqual(
            str(self.VALUES['computeProfiles'][self.PROFILE]['cnvrgApp']['cpu']),
            str(self.SPEC['spec']['cnvrgApp']['cpu']))

    def test_small_profile_webapp_memory(self):
        self.assertEqual(
            str(self.VALUES['computeProfiles'][self.PROFILE]['cnvrgApp']['memory']),
            str(self.SPEC['spec']['cnvrgApp']['memory']))

    def test_small_profile_sidekiq_cpu(self):
        self.assertEqual(
            str(self.VALUES['computeProfiles'][self.PROFILE]['cnvrgApp']['sidekiq']['cpu']),
            str(self.SPEC['spec']['cnvrgApp']['sidekiq']['cpu']))

    def test_small_profile_sidekiq_memory(self):
        self.assertEqual(
            str(self.VALUES['computeProfiles'][self.PROFILE]['cnvrgApp']['sidekiq']['memory']),
            str(self.SPEC['spec']['cnvrgApp']['sidekiq']['memory']))

    def test_small_profile_pg_cpu(self):
        self.assertEqual(
            str(self.VALUES['computeProfiles'][self.PROFILE]['pg']['cpu']),
            str(self.SPEC['spec']['pg']['cpuRequest']))

    def test_small_profile_pg_memory(self):
        self.assertEqual(
            str(self.VALUES['computeProfiles'][self.PROFILE]['pg']['memory']),
            str(self.SPEC['spec']['pg']['memoryRequest']))

    def test_small_profile_minio_cpu(self):
        self.assertEqual(
            str(self.VALUES['computeProfiles'][self.PROFILE]['minio']['cpu']),
            str(self.SPEC['spec']['minio']['cpuRequest']))

    def test_small_profile_minio_memory(self):
        self.assertEqual(
            str(self.VALUES['computeProfiles'][self.PROFILE]['minio']['memory']),
            str(self.SPEC['spec']['minio']['memoryRequest']))

    def test_small_profile_es_cpu(self):
        component = "es"
        self.assertEqual(
            str(self.VALUES['computeProfiles'][self.PROFILE][component]['cpu']),
            str(self.SPEC['spec']['logging'][component]['cpuRequest']))

    def test_small_profile_es_memory(self):
        component = "es"
        self.assertEqual(
            str(self.VALUES['computeProfiles'][self.PROFILE][component]['memory']),
            str(self.SPEC['spec']['logging'][component]['memoryRequest']))

    def test_small_profile_prometheus_cpu(self):
        component = "monitoring"
        self.assertEqual(
            str(self.VALUES['computeProfiles'][self.PROFILE]['prometheus']['cpu']),
            str(self.SPEC['spec'][component]['prometheus']['cpuRequest']))

    def test_small_profile_prometheus_memory(self):
        component = "monitoring"
        self.assertEqual(
            str(self.VALUES['computeProfiles'][self.PROFILE]['prometheus']['memory']),
            str(self.SPEC['spec'][component]['prometheus']['memoryRequest']))

    def test_small_profile_redis_cpu(self):
        component = "redis"
        self.assertEqual(
            str(self.VALUES['computeProfiles'][self.PROFILE][component]['cpu']),
            str(self.SPEC['spec'][component]['requests']['cpu']))

    def test_small_profile_redis_memory(self):
        component = "redis"
        self.assertEqual(
            str(self.VALUES['computeProfiles'][self.PROFILE][component]['memory']),
            str(self.SPEC['spec'][component]['requests']['memory']))


class HelmChartRenderTest(unittest.TestCase, CommonBase):

    @classmethod
    def setUpClass(cls):
        logging.info("starting -> HelmChartRenderTest")
        cls._started_at = time.time()

    @classmethod
    def tearDownClass(cls):
        cls.log_total_test_execution_time(cls._started_at, "ComputeProfilesSmallWithHelmChartTest")

    def test_custom_node_exporter_port(self):
        cmd = "helm template chart -s templates/cnvrg-app.yaml --set monitoring.nodeExporter.port=19100 | yq r - spec.monitoring.nodeExporter.port"
        res = self.exec_cmd(cmd)
        self.assertEqual("19100", res[1])
