
import yaml
import json
y = """
storage:
  enabled: "true"
  ccpStorageClass: ""
  hostpath:
    enabled: "true"
    image: "quay.io/kubevirt/hostpath-provisioner"
    hostPath: "/cnvrg-storage"
    storageClassName: "cnvrg-hostpath-storage"
    nodeName: "node1"
    cpuRequest: 100m
    memoryRequest: 100Mi
    cpuLimit: 200m
    memoryLimit: 200Mi
    reclaimPolicy: "Retain"
    defaultSc: "true"
"""

print(json.dumps(yaml.safe_load(y)))