# cnvrg control plan compute resources

### Following table lists required compute and storage resources for cnvrg control plan 


#### Large cluster
|**Workload**|**Replicas**|**CPU Request**|**Memory Request**|**Storage**|**CPU Limit**|**Memory Limit**
| ---|---|---|---|---|---|---|
|`webapp`| 1 | 4 | 8Gi | - | - | - 
|`sidekiq`| 2 | 4 | 8Gi | - | - | - 
|`searchkick`| 1 | 1 | 2Gi | - | - | - 
|`postgres`| 1 | 4 | 8Gi | 100Gi | - | - 
|`minio`| 1 | 2 | 4Gi | 1T | - | - 
|`elasticsearch`| 1 | 1 | 1Gi | 100Gi | 2 | 4Gi 
|`prometheus`| 1 | 1 | 1Gi | 100Gi | - | - 
|`redis`| 1 | 500m | 1Gi | - | 1 | 2Gi 
|`fluentd`| 1 * nodes count | 100m | 200Mi | - | - | 200Mi 
|`hostpath`| 1 | 100m | 200Mi | - | 200m | 200Mi 
|`istiod`| 1 | 500m | 2Gi | - | - | - 
|`istio-ingress`| 1 | 100m | 128Mi | - | 2 | 1Gi 
|`kibana`| 1 | 500m | 500Mi | - | 1 | 2Gi 
|`nfs-provisioner`| 1 | 100m | 100Mi | - | 200m | 200Mi 
|**TOTAL**| **15** | **~20** | **~40Gi** | 300Gi + 1T | - | - 


#### Medium cluster
|**Workload**|**Replicas**|**CPU Request**|**Memory Request**|**Storage**|**CPU Limit**|**Memory Limit**
| ---|---|---|---|---|---|---|
|`webapp`| 1 | 2 | 4Gi | - | - | - 
|`sidekiq`| 2 | 2 | 4Gi | - | - | - 
|`searchkick`| 1 | 1 | 1Gi | - | - | - 
|`postgres`| 1 | 2 | 4Gi | 100Gi | - | - 
|`minio`| 1 | 1 | 2Gi | 1T | - | - 
|`elasticsearch`| 1 | 1 | 1Gi | 100Gi | 2 | 4Gi 
|`prometheus`| 1 | 1 | 1Gi | 100Gi | - | - 
|`redis`| 1 | 500m | 1Gi | - | 1 | 2Gi 
|`fluentd`| 1 * nodes count | 100m | 200Mi | - | - | 200Mi 
|`hostpath`| 1 | 100m | 200Mi | - | 200m | 200Mi 
|`istiod`| 1 | 500m | 2Gi | - | - | - 
|`istio-ingress`| 1 | 100m | 128Mi | - | 2 | 1Gi 
|`kibana`| 1 | 500m | 500Mi | - | 1 | 2Gi 
|`nfs-provisioner`| 1 | 100m | 100Mi | - | 200m | 200Mi 
|**TOTAL**| **15** | **~12** | **~26Gi** | 300Gi + 1T | - | - 


#### Small cluster
Small cluster mainly intend for demos and single user usage. 
There is no any warranty that workloads will be executed, or even scheduled, since this profile doesn't specify any compute/storage resources.

|**Workload**|**Replicas**|**CPU Request**|**Memory Request**|**Storage**|**CPU Limit**|**Memory Limit**
| ---|---|---|---|---|---|---|
|`webapp`| 1 | - | - | - | - | - 
|`sidekiq`| 1 | - | - | - | - | - 
|`searchkick`| 1 | - | - | - | - | - 
|`postgres`| 1 | - | - | - | - | - 
|`minio`| 1 | - | - | - | - | - 
|`elasticsearch`| 1 | - | - | - | - | - 
|`prometheus`| 1 | - | - | - | - | - 
|`redis`| 1 | - | - | - | - | - 
|`fluentd`| 1 * nodes count | - | - | - | - | - 
|`hostpath`| 1 | - | - | - | - | - 
|`istiod`| 1 | - | - | - | - | - | - 
|`istio-ingress`| 1 | - | - | - | - | - 
|`kibana`| 1 | - | - | - | - | - | - 
|`nfs-provisioner`| 1 | - | - | - | - | - 
|**TOTAL**| **15** | **-** | **-** | - | - | - 
