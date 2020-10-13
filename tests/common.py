import logging
import os
import subprocess
import yaml
from kubernetes import client, config
from kubernetes.client.rest import ApiException
import time

log_format = "|%(asctime)s|%(levelname)-5s %(message)s"
logging.basicConfig(level=logging.INFO, format=log_format)

config.load_kube_config()
VERSION = "v1"
GROUP = "mlops.cnvrg.io"
PLURAL = "cnvrgapps"
NAMESPACE = "cnvrg"


class CommonBase(object):
    BRANCH_NAME = "*"

    @staticmethod
    def deploy():
        logging.info("deploying env...")
        tag = os.getenv('TAG', None)
        if tag is None:
            raise Exception("TAG env not set, can't continue")
        cmd = f"TAG={tag} make deploy"
        logging.info(f"executing: {cmd}")
        stream = os.popen(cmd)
        logging.info(stream.read())

    @staticmethod
    def undeploy():
        logging.info("undeploying env...")
        stream = os.popen('make undeploy')
        logging.info(stream.read())

    @staticmethod
    def create_cnvrg_spec(cnvrg_spec):
        body = yaml.load(cnvrg_spec, Loader=yaml.FullLoader)
        api_instance = client.CustomObjectsApi()
        try:
            api_response = api_instance.create_namespaced_custom_object(GROUP, VERSION, NAMESPACE, PLURAL, body)
            logging.info(api_response)
        except ApiException as e:
            if e.status == 409:
                logging.warning("The cnvrg spec already deployed, CR won't be created")
            else:
                logging.error("Exception when calling CustomObjectsApi->create_namespaced_custom_object: %s\n" % e)

    @staticmethod
    def get_cnvrg_spec(name="cnvrg-app"):
        api_instance = client.CustomObjectsApi()
        try:
            api_response = api_instance.get_namespaced_custom_object(GROUP, VERSION, NAMESPACE, PLURAL, name)
            logging.info(api_response)
            return api_response
        except ApiException as e:
            logging.error("Exception when calling CustomObjectsApi->create_namespaced_custom_object: %s\n" % e)

    @staticmethod
    def delete_cnvrg_spec(name="cnvrg-app"):
        api_instance = client.CustomObjectsApi()
        try:
            api_response = api_instance.delete_namespaced_custom_object(GROUP, VERSION, NAMESPACE, PLURAL, name)
            logging.info(api_response)
        except ApiException as e:
            logging.error("Exception when calling CustomObjectsApi->delete_namespaced_custom_object: %s\n" % e)

    @staticmethod
    def wait_for_cnvrg_spec_ready(name="cnvrg-app"):
        try:
            for i in range(0, 1800):
                spec = CommonBase.get_cnvrg_spec(name)
                if 'status' not in spec:
                    logging.info(f"cnvrg sepc don't have status object yet, ttl: {1800 - i} sec")
                    continue
                if 'conditions' not in spec['status']:
                    logging.info(f"cnvrg sepc don't have conditions object yet, ttl: {1800 - i} sec")
                    continue
                for condition in spec['status']['conditions']:
                    if 'ansibleResult' in condition:
                        if condition['message'] == "Awaiting next reconciliation":
                            logging.info("cnvrg spec successfully deployed!")
                            return True
                logging.info(f"cnvrg spec not ready yet, ttl: {1800 - i} sec")
                time.sleep(1)
            logging.error("Cnvrg spec not ready, and timeout reached (30m)")
        except Exception as ex:
            logging.error("Exception when calling wait_for_cnvrg_spec_ready: %s\n" % ex)
        return False

    @staticmethod
    def get_spec_from_chart(cmd):
        child = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        streamdata = child.communicate()[0]
        spec = str(streamdata, 'utf-8')
        return spec

    def exec_cmd(self, cmd):
        child = subprocess.Popen(cmd, shell=True, stdout=subprocess.PIPE, stderr=subprocess.PIPE)
        streamdata = child.communicate()[0]
        logging.info(str(streamdata, 'utf-8'))
        return child.returncode
