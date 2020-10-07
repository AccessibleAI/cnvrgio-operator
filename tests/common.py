import logging
import os
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
    @staticmethod
    def deploy():
        logging.info("deploying env...")
        img = os.getenv('IMG', None)
        if img is None:
            raise Exception("IMG env not set, can't continue")
        cmd = f"IMG={img} make deploy"
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
        for i in range(0, 1800):
            spec = CommonBase.get_cnvrg_spec(name)
            for condition in spec['status']['conditions']:
                if 'ansibleResult' in condition:
                    if condition['message'] == "Awaiting next reconciliation":
                        logging.info("cnvrg spec successfully deployed!")
                        return True
            logging.info(f"cnvrg spec not ready yet, ttl: {1800 - i} sec")
            time.sleep(1)
        logging.error("Cnvrg spec not ready, and timeout reached (30m)")
        return False
