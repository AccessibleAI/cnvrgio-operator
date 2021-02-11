# cnvrg.io operator
## Deploy cnvrg stack on EKS | AKS | GKE | OpenShift* | On-Premise clusters with K8S operator

### Quick start

#### Prerequisite
1. Install [helm3](https://helm.sh/docs/intro/install/#from-script)
2. Add cnvrg helm repo
   ```bash
   helm repo add cnvrg https://charts.cnvrg.io
   helm repo update
   helm search repo cnvrg -l
   ```

#### Deploy with defaults (Istio, Minio)
```bash
helm install cnvrg cnvrg/cnvrg -n cnvrg --create-namespace --timeout 1500s  --wait \
    --set clusterDomain=base.domain
```

### Upgrade with helm upgrade
```
helm upgrade cnvrg cnvrg/cnvrg -n cnvrg --reuse-values \
  --set cnvrgApp.image=cnvrg/app:master-1374-encode
```

### Uninstall cnvrg
```
# Uninstall cnvrg.io control plan
helm uninstall cnvrg -n cnvrg
```

### Install without Helm (raw k8s manifests)
```
kubectl create namespace cnvrg
helm template cnvrg cnvrg/cnvrg --no-hooks --set clusterDomain=base.domain > cnvrg.yaml # ... add extra params if required
kubectl apply -f cnvrg.yaml
```

### Dump only the CnvrgApp Custom Resource
```
helm template cnvrg cnvrg/cnvrg  -s templates/cnvrg-app.yaml
```


### Examples

#### Deploy on EKS | AKS | GKE with  (Istio, Cloud Object Storage)
```bash
# AWS - EKS
helm install cnvrg cnvrg/cnvrg -n cnvrg --create-namespace --timeout 1500s --wait \
        --set clusterDomain=base.domain \
        --set cnvrgApp.image=cnvrg/app:enterprise-3.1.2 \
        --set cnvrgApp.conf.registry.user=cnvrg-license-username \
        --set cnvrgApp.conf.registry.password=cnvrg-license-password \
        --set cnvrgApp.conf.cnvrgStorageType=aws \
        --set cnvrgApp.conf.cnvrgStorageBucket=s3bucket-name \
        --set cnvrgApp.conf.cnvrgStorageAccessKey=ACCESSKEY \
        --set cnvrgApp.conf.cnvrgStorageSecretKey=SECRETKEY \
        --set cnvrgApp.conf.cnvrgStorageRegion=aws-region


# Azure - AKS
helm install cnvrg cnvrg/cnvrg -n cnvrg --create-namespace --timeout 1500s --wait \
        --set clusterDomain=base.domain \
        --set cnvrgApp.image=cnvrg/app:enterprise-3.1.2 \
        --set cnvrgApp.conf.registry.user=cnvrg-license-username \
        --set cnvrgApp.conf.registry.password=cnvrg-license-password \
        --set cnvrgApp.conf.cnvrgStorageType=azure \
        --set cnvrgApp.conf.cnvrgStorageAzureAccessKey=azure-storage-account-access-key \
        --set cnvrgApp.conf.cnvrgStorageAzureAccountName=azure-storage-account-name \
        --set cnvrgApp.conf.cnvrgStorageAzureContainer=azure-storage-container-name

# GCP - GKE
helm install cnvrg cnvrg/cnvrg -n cnvrg --create-namespace --timeout 1500s --wait \
        --set clusterDomain=base.domain \
        --set cnvrgApp.image=cnvrg/app:enterprise-3.1.2 \
        --set cnvrgApp.conf.registry.user=cnvrg-license-username \
        --set cnvrgApp.conf.registry.password=cnvrg-license-password \
        --set cnvrgApp.conf.cnvrgStorageType=gcp \
        --set cnvrgApp.conf.cnvrgStorageProject=gcp-storage-project
```

#### Deploy OnPrem  (Istio, Minio, HostPath, SMTP, micro storage profile)
```bash
helm install cnvrg cnvrg/cnvrg -n cnvrg --create-namespace --timeout 1500s --wait \
    --set clusterDomain=apps.1.2.3.4.nip.io \
    --set storage.enabled="true" \
    --set storage.hostpath.enabled="true" \
    --set storage.hostpath.nodeName="k8s-node-name" \
    --set cnvrgApp.conf.smtp.server="smtp-server" \
    --set cnvrgApp.conf.smtp.port="smtp-port" \
    --set cnvrgApp.conf.smtp.username="smtp-user" \
    --set cnvrgApp.conf.smtp.password="smtp-pass" \
    --set cnvrgApp.conf.smtp.domain="domain"
```

#### Deploy OnPrem  (NodePort, Minio, NFS)
```bash
helm install cnvrg cnvrg/cnvrg -n cnvrg --create-namespace --timeout 1500s --wait \
    --set clusterDomain=192.168.1.2 \
    --set networking.ingressType="nodeport" \
    --set storage.enabled="true" \
    --set storage.nfs.enabled="true" \
    --set storage.nfs.defaultSc="true" \
    --set storage.nfs.server="storage.nfs.SERVER.IP" \
    --set storage.nfs.path="/shared/nfs/directory"
```

#### Deploy OnPrem  (NodePort, Minio, Hostpath)
```bash
helm install cnvrg cnvrg/cnvrg -n cnvrg --create-namespace --timeout 1500s --wait \
    --set clusterDomain=<node-ip> \
    --set networking.ingressType="nodeport" \
    --set storage.enabled="true" \
    --set storage.hostpath.enabled="true" \
    --set storage.hostpath.defaultSc="true" \
    --set storage.hostpath.nodeName="<k8s-node>"
```

#### Turn On/Off components
```
helm install cnvrg cnvrg/cnvrg -n cnvrg --create-namespace --timeout 1500s --wait \
    --set cnvrgApp.enabled="false" \
    --set logging.enabled="false" \
    --set storage.enabled="false" \
    --set networking.enabled="false" \
    --set minio.enabled="false" \
    --set mpi.enabled="false" \
    --set nvidiadp.enabled="false" \
    --set pg.enabled="false" \
    --set redis.enabled="false"
```


### Chart options - cnvrgApp 
|**key**|**default value**
| ---|---| 
|`cnvrgApp.replicas`|1
|`cnvrgApp.enabled`|true
|`cnvrgApp.image`|-
|`cnvrgApp.port`|80
|`cnvrgApp.cpu`|2
|`cnvrgApp.memory`|4Gi
|`cnvrgApp.svcName`|app
|`cnvrgApp.fixpg`|true
|`cnvrgApp.nodePort`|30080
|`cnvrgApp.passengerMaxPoolSize`|20
|`cnvrgApp.enableReadinessProbe`|true
|`cnvrgApp.initialDelaySeconds`|10
|`cnvrgApp.readinessPeriodSeconds`|25
|`cnvrgApp.readinessTimeoutSeconds`|20
|`cnvrgApp.failureThreshold`|4
|`cnvrgApp.resourcesRequestEnabled`|true
|`cnvrgApp.sidekiq.enabled`|true
|`cnvrgApp.sidekiq.split`|true
|`cnvrgApp.sidekiq.cpu`|1750m
|`cnvrgApp.sidekiq.memory`|3750Mi
|`cnvrgApp.sidekiq.replicas`|2
|`cnvrgApp.searchkiq.enabled`|true
|`cnvrgApp.searchkiq.cpu`|750m
|`cnvrgApp.searchkiq.memory`|750Mi
|`cnvrgApp.searchkiq.replicas`|1
|`cnvrgApp.systemkiq.enabled`|false
|`cnvrgApp.systemkiq.cpu`|500m
|`cnvrgApp.systemkiq.memory`|500Mi
|`cnvrgApp.systemkiq.replicas`|1
|`cnvrgApp.kiqPrestopHook.enabled`|true
|`cnvrgApp.kiqPrestopHook.killTimeout`|60
|`cnvrgApp.hyper.enabled`|true
|`cnvrgApp.hyper.image`|cnvrg/hyper-server:latest
|`cnvrgApp.hyper.port`|5050
|`cnvrgApp.hyper.replicas`|1
|`cnvrgApp.hyper.nodePort`|30050
|`cnvrgApp.hyper.svcName`|hyper
|`cnvrgApp.hyper.token`|token
|`cnvrgApp.hyper.cpuRequest`|100m
|`cnvrgApp.hyper.memoryRequest`|200Mi
|`cnvrgApp.hyper.cpuLimit`|2
|`cnvrgApp.hyper.memoryLimit`|4Gi
|`cnvrgApp.hyper.enableReadinessProbe`|true
|`cnvrgApp.hyper.readinessPeriodSeconds`|100
|`cnvrgApp.hyper.readinessTimeoutSeconds`|60
|`cnvrgApp.seeder.image`|docker.io/cnvrg/cnvrg-boot:v0.25
|`cnvrgApp.seeder.seedCmd`|rails db:migrate && rails db:seed && rails libraries:update
|`cnvrgApp.seeder.createBucketCmd`|mb.sh
|`cnvrgApp.conf.gcpStorageSecret`|gcp-storage-secret
|`cnvrgApp.conf.gcpKeyfileMountPath`|/tmp/gcp_keyfile
|`cnvrgApp.conf.gcpKeyfileName`|key.json
|`cnvrgApp.conf.jobsStorageClass`|-
|`cnvrgApp.conf.featureFlags`|-
|`cnvrgApp.conf.sentryUrl`|-
|`cnvrgApp.conf.secretKeyBase`|-
|`cnvrgApp.conf.stsIv`|-
|`cnvrgApp.conf.stsKey`|-
|`cnvrgApp.conf.passengerAppEnv`|app
|`cnvrgApp.conf.railsEnv`|app
|`cnvrgApp.conf.runJobsOnSelfCluster`|true
|`cnvrgApp.conf.defaultComputeConfig`|/opt/kube
|`cnvrgApp.conf.defaultComputeName`|default
|`cnvrgApp.conf.useStdout`|true
|`cnvrgApp.conf.extractTagsFromCmd`|false
|`cnvrgApp.conf.checkJobExpiration`|true
|`cnvrgApp.conf.cnvrgStorageType`|minio
|`cnvrgApp.conf.cnvrgStorageBucket`|cnvrg-storage
|`cnvrgApp.conf.cnvrgStorageAccessKey`|-
|`cnvrgApp.conf.cnvrgStorageSecretKey`|-
|`cnvrgApp.conf.minioSseMasterKey`|-
|`cnvrgApp.conf.cnvrgStorageAzureAccessKey`|-
|`cnvrgApp.conf.cnvrgStorageAzureAccountName`|-
|`cnvrgApp.conf.cnvrgStorageAzureContainer`|-
|`cnvrgApp.conf.cnvrgStorageRegion`|eastus
|`cnvrgApp.conf.cnvrgStorageProject`|-
|`cnvrgApp.conf.customAgentTag`|false
|`cnvrgApp.conf.intercom`|true
|`cnvrgApp.conf.cnvrgJobUid`|1000
|`cnvrgApp.conf.ldap.enabled`|false
|`cnvrgApp.conf.ldap.host`|-
|`cnvrgApp.conf.ldap.port`|-
|`cnvrgApp.conf.ldap.account`|userPrincipalName
|`cnvrgApp.conf.ldap.base`|-
|`cnvrgApp.conf.ldap.adminUser`|-
|`cnvrgApp.conf.ldap.adminPassword`|-
|`cnvrgApp.conf.ldap.ssl`|-
|`cnvrgApp.conf.registry.name`|cnvrg-registry
|`cnvrgApp.conf.registry.url`|docker.io
|`cnvrgApp.conf.registry.user`|-
|`cnvrgApp.conf.registry.password`|-
|`cnvrgApp.conf.rbac.role`|cnvrg-role
|`cnvrgApp.conf.rbac.serviceAccountName`|cnvrg
|`cnvrgApp.conf.rbac.roleBindingName`|cnvrg-role-binding
|`cnvrgApp.conf.smtp.server`|-
|`cnvrgApp.conf.smtp.port`|-
|`cnvrgApp.conf.smtp.username`|-
|`cnvrgApp.conf.smtp.password`|-
|`cnvrgApp.conf.smtp.domain`|-
|`cnvrgApp.cnvrgRouter.enabled`|false
|`cnvrgApp.cnvrgRouter.image`|nginx
|`cnvrgApp.cnvrgRouter.svcName`|routing-service
|`cnvrgApp.cnvrgRouter.nodePort`|30081
|`cnvrgApp.cnvrgRouter.port`|80

### Chart options - globals 
|**key**|**default value**
| ---|---| 
|`computeProfile`|medium
|`condition`|upgrade
|`cacheDsName`|app-image-cache
|`cnvrgAppName`|cnvrg-app
|`image`|-
|`cacheImage`|true
|`debug`|false
|`dumpDir`|-
|`dryRun`|false
|`clusterDomain`|-
|`otags`|all

### Chart options - logging 
|**key**|**default value**
| ---|---| 
|`logging.enabled`|true
|`logging.es.enabled`|true
|`logging.es.image`|docker.io/cnvrg/cnvrg-es:v7.8.1
|`logging.es.maxMapImage`|docker.io/cnvrg/cnvrg-tools:v0.3
|`logging.es.port`|9200
|`logging.es.storageSize`|30Gi
|`logging.es.svcName`|elasticsearch
|`logging.es.runAsUser`|1000
|`logging.es.fsGroup`|1000
|`logging.es.patchEsNodes`|false
|`logging.es.nodePort`|32200
|`logging.es.storageClass`|use-default
|`logging.es.cpuRequest`|1
|`logging.es.memoryRequest`|1Gi
|`logging.es.cpuLimit`|2
|`logging.es.memoryLimit`|4Gi
|`logging.es.javaOpts`|-
|`logging.elastalert.enabled`|true
|`logging.elastalert.image`|bitsensor/elastalert:3.0.0-beta.1
|`logging.elastalert.port`|80
|`logging.elastalert.nodePort`|32030
|`logging.elastalert.containerPort`|3030
|`logging.elastalert.storageSize`|30Gi
|`logging.elastalert.svcName`|elastalert
|`logging.elastalert.storageClass`|use-default
|`logging.elastalert.cpuRequest`|100m
|`logging.elastalert.memoryRequest`|200Mi
|`logging.elastalert.cpuLimit`|400m
|`logging.elastalert.memoryLimit`|800Mi
|`logging.elastalert.runAsUser`|1000
|`logging.elastalert.fsGroup`|1000
|`logging.fluentd.enabled`|true
|`logging.fluentd.image`|fluent/fluentd-kubernetes-daemonset:v1.11-debian-elasticsearch7-1
|`logging.fluentd.journalPath`|/var/log/journal
|`logging.fluentd.containersPath`|/var/lib/docker/containers
|`logging.fluentd.journald`|false
|`logging.fluentd.cpuRequest`|100m
|`logging.fluentd.memoryRequest`|200Mi
|`logging.fluentd.memoryLimit`|200Mi
|`logging.kibana.enabled`|true
|`logging.kibana.svcName`|kibana
|`logging.kibana.port`|5601
|`logging.kibana.image`|docker.elastic.co/kibana/kibana-oss:7.8.1
|`logging.kibana.nodePort`|30601
|`logging.kibana.cpuRequest`|100m
|`logging.kibana.memoryRequest`|100Mi
|`logging.kibana.cpuLimit`|1
|`logging.kibana.memoryLimit`|2000Mi

### Chart options - minio 
|**key**|**default value**
| ---|---| 
|`minio.enabled`|true
|`minio.replicas`|1
|`minio.image`|docker.io/minio/minio:RELEASE.2020-09-17T04-49-20Z
|`minio.port`|9000
|`minio.storageSize`|100Gi
|`minio.svcName`|minio
|`minio.nodePort`|30090
|`minio.storageClass`|use-default
|`minio.cpuRequest`|1
|`minio.memoryRequest`|2Gi
|`minio.sharedStorage.enabled`|false
|`minio.sharedStorage.consistentHash.key`|httpQueryParameterName
|`minio.sharedStorage.consistentHash.value`|uploadId

### Chart options - monitoring 
|**key**|**default value**
| ---|---| 
|`monitoring.enabled`|true
|`monitoring.prometheusOperator.enabled`|true
|`monitoring.prometheusOperator.images.operatorImage`|quay.io/coreos/prometheus-operator:v0.40.0
|`monitoring.prometheusOperator.images.configReloaderImage`|jimmidyson/configmap-reload:v0.3.0
|`monitoring.prometheusOperator.images.prometheusConfigReloaderImage`|quay.io/coreos/prometheus-config-reloader:v0.40.0
|`monitoring.prometheusOperator.images.kubeRbacProxyImage`|quay.io/coreos/kube-rbac-proxy:v0.4.1
|`monitoring.prometheus.enabled`|true
|`monitoring.prometheus.image`|quay.io/prometheus/prometheus:v2.22.2
|`monitoring.prometheus.cpuRequest`|1
|`monitoring.prometheus.memoryRequest`|1Gi
|`monitoring.prometheus.svcName`|prometheus
|`monitoring.prometheus.port`|9090
|`monitoring.prometheus.nodePort`|30909
|`monitoring.prometheus.storageSize`|100Gi
|`monitoring.prometheus.storageClass`|use-default
|`monitoring.nodeExporter.enabled`|true
|`monitoring.nodeExporter.port`|9100
|`monitoring.nodeExporter.image`|quay.io/prometheus/node-exporter:v0.18.1
|`monitoring.kubeStateMetrics.enabled`|true
|`monitoring.kubeStateMetrics.image`|quay.io/coreos/kube-state-metrics:v1.9.5
|`monitoring.grafana.enabled`|true
|`monitoring.grafana.image`|grafana/grafana:7.2.0
|`monitoring.grafana.svcName`|grafana
|`monitoring.grafana.port`|3000
|`monitoring.grafana.nodePort`|30012
|`monitoring.defaultServiceMonitors.enabled`|true
|`monitoring.sidekiqExporter.enabled`|true
|`monitoring.sidekiqExporter.image`|docker.io/strech/sidekiq-prometheus-exporter:0.1.13
|`monitoring.minioExporter.enabled`|true
|`monitoring.minioExporter.image`|docker.io/cnvrg/cnvrg-boot:v0.24
|`monitoring.dcgmExporter.enabled`|true
|`monitoring.dcgmExporter.image`|nvidia/dcgm-exporter:1.7.2
|`monitoring.dcgmExporter.port`|9400
|`monitoring.idleMetricsExporter.enabled`|true
|`monitoring.metricsServer.enabled`|true
|`monitoring.metricsServer.image`|k8s.gcr.io/metrics-server/metrics-server:v0.3.7

### Chart options - mpi 
|**key**|**default value**
| ---|---| 
|`mpi.enabled`|true
|`mpi.image`|mpioperator/mpi-operator:v0.2.3
|`mpi.kubectlDeliveryImage`|mpioperator/kubectl-delivery:v0.2.3
|`mpi.registry.name`|mpi-private-registry
|`mpi.registry.url`|docker.io
|`mpi.registry.user`|-
|`mpi.registry.password`|-

### Chart options - networking 
|**key**|**default value**
| ---|---| 
|`networking.enabled`|true
|`networking.ingressType`|istio
|`networking.https.enabled`|false
|`networking.https.cert`|-
|`networking.https.key`|-
|`networking.https.certSecret`|-
|`networking.istio.enabled`|true
|`networking.istio.operatorImage`|docker.io/istio/operator:1.8.1
|`networking.istio.hub`|docker.io/istio
|`networking.istio.tag`|1.8.1
|`networking.istio.proxyImage`|proxyv2
|`networking.istio.mixerImage`|mixer
|`networking.istio.pilotImage`|pilot
|`networking.istio.gwName`|cnvrg-gateway
|`networking.istio.externalIp`|-
|`networking.istio.ingressSvcAnnotations`|-
|`networking.istio.ingressSvcExtraPorts`|-
|`networking.istio.loadBalancerSourceRanges`|-
|`networking.ingress.enabled`|true
|`networking.ingress.timeout`|18000s
|`networking.ingress.retriesAttempts`|5
|`networking.ingress.perTryTimeout`|3600s

### Chart options - nvidiadp 
|**key**|**default value**
| ---|---| 
|`nvidiadp.enabled`|true
|`nvidiadp.image`|nvidia/k8s-device-plugin:v0.7.0
|`nvidiadp.nodeSelector.enabled`|true
|`nvidiadp.nodeSelector.key`|accelerator
|`nvidiadp.nodeSelector.value`|nvidia

### Chart options - pg 
|**key**|**default value**
| ---|---| 
|`pg.enabled`|true
|`pg.secretName`|cnvrg-pg-secret
|`pg.image`|centos/postgresql-12-centos7
|`pg.port`|5432
|`pg.storageSize`|80Gi
|`pg.svcName`|postgres
|`pg.dbname`|cnvrg_production
|`pg.pass`|-
|`pg.user`|cnvrg
|`pg.runAsUser`|26
|`pg.fsGroup`|26
|`pg.storageClass`|use-default
|`pg.cpuRequest`|2
|`pg.memoryRequest`|4Gi
|`pg.maxConnections`|500
|`pg.sharedBuffers`|64MB
|`pg.hugePages.enabled`|false
|`pg.hugePages.size`|2Mi
|`pg.hugePages.memory`|-

### Chart options - redis 
|**key**|**default value**
| ---|---| 
|`redis.enabled`|true
|`redis.image`|docker.io/cnvrg/cnvrg-redis:v3.0.5.c2
|`redis.svcName`|redis
|`redis.port`|6379
|`redis.appendonly`|yes
|`redis.storageSize`|10Gi
|`redis.storageClass`|use-default
|`redis.limits.cpu`|1
|`redis.limits.memory`|2Gi
|`redis.requests.cpu`|500m
|`redis.requests.memory`|1Gi

### Chart options - storage 
|**key**|**default value**
| ---|---| 
|`storage.enabled`|false
|`storage.ccpStorageClass`|-
|`storage.hostpath.enabled`|false
|`storage.hostpath.image`|quay.io/kubevirt/hostpath-provisioner
|`storage.hostpath.hostPath`|/cnvrg-storage
|`storage.hostpath.storageClassName`|cnvrg-hostpath-storage
|`storage.hostpath.nodeName`|-
|`storage.hostpath.cpuRequest`|100m
|`storage.hostpath.memoryRequest`|100Mi
|`storage.hostpath.cpuLimit`|200m
|`storage.hostpath.memoryLimit`|200Mi
|`storage.hostpath.reclaimPolicy`|Retain
|`storage.hostpath.defaultSc`|false
|`storage.nfs.enabled`|false
|`storage.nfs.image`|quay.io/external_storage/nfs-client-provisioner:latest
|`storage.nfs.provisioner`|cnvrg.io/ifs
|`storage.nfs.storageClassName`|cnvrg-nfs-storage
|`storage.nfs.server`|-
|`storage.nfs.path`|-
|`storage.nfs.cpuRequest`|100m
|`storage.nfs.memoryRequest`|100Mi
|`storage.nfs.cpuLimit`|200m
|`storage.nfs.memoryLimit`|200Mi
|`storage.nfs.reclaimPolicy`|Retain
|`storage.nfs.defaultSc`|false

### Chart options - tenancy 
|**key**|**default value**
| ---|---| 
|`tenancy.enabled`|false
|`tenancy.dedicatedNodes`|false
|`tenancy.cnvrg.key`|cnvrg-taint
|`tenancy.cnvrg.value`|true

### Chart options - vpa 
|**key**|**default value**
| ---|---| 
|`vpa.enabled`|false
|`vpa.images.admissionImage`|k8s.gcr.io/autoscaling/vpa-admission-controller:0.9.0
|`vpa.images.recommenderImage`|k8s.gcr.io/autoscaling/vpa-recommender:0.9.0
|`vpa.images.updaterImage`|k8s.gcr.io/autoscaling/vpa-updater:0.9.0
