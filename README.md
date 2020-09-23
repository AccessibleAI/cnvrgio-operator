# cnvrg.io operator
## Deploy cnvrg stack on EKS | AKS | GKE | OpenShift* | On-Premise clusters with K8S operator

### Quick start

#### Prerequisite
1. Install helm3
2. Add cnvrg helm repo
   ```bash
   helm repo add cnvrg https://helm.cnvrg.io
   helm repo update
   ```

#### Deploy with defaults (Istio, Minio)
```bash
helm install cnvrg cnvrg/cnvrgio --timeout 1500s  --wait \
    --set clusterDomain=base.domain
```

### Upgrade with helm upgrade
```
helm upgrade cnvrg cnvrg/cnvrgio --reuse-values \
  --set cnvrgApp.image=cnvrg/app:master-1374-encode
```

### Uninstall cnvrg
```
# Uninstall cnvrg.io control plan
helm uninstall cnvrg
```

### Install without Helm (raw k8s manifests)
```
kubectl create namespace cnvrg
helm template cnvrg cnvrg/cnvrgio --no-hooks --set clusterDomain=base.domain > cnvrg.yaml # ... add extra params if required
kubectl apply -f cnvrg.yaml
```

### Dump only the CnvrgApp Custom Resource
```
helm template cnvrg cnvrg/cnvrgio  -s templates/cnvrg-app.yaml
```


### Examples

#### Deploy on EKS | AKS | GKE with  (Istio, Cloud Object Storage)
```bash
# AWS - EKS
helm install cnvrg cnvrg/cnvrgio --timeout 1500s --wait \
        --set clusterDomain=base.domain \
        --set cnvrgApp.image=cnvrg/app:enterprise-3.1.2 \
        --set cnvrgApp.edition=enterprise \
        --set registry.user=cnvrg-license-username \
        --set registry.password=cnvrg-license-password \
        --set appSecrets.cnvrgStorageType=aws \
        --set appSecrets.cnvrgStorageBucket=s3bucket-name \
        --set appSecrets.cnvrgStorageAccessKey=ACCESSKEY \
        --set appSecrets.cnvrgStorageSecretKey=SECRETKEY \
        --set appSecrets.cnvrgStorageRegion=aws-region


# Azure - AKS
helm install cnvrg cnvrg/cnvrgio --timeout 1500s --wait \
        --set cnvrgApp.image=cnvrg/app:enterprise-3.1.2 \
        --set cnvrgApp.edition=enterprise \
        --set registry.user=cnvrg-license-username \
        --set registry.password=cnvrg-license-password \
        --set clusterDomain=base.domain \
        --set appSecrets.cnvrgStorageType=azure \
        --set appSecrets.cnvrgStorageAzureAccessKey=azure-storage-account-access-key \
        --set appSecrets.cnvrgStorageAzureAccountName=azure-storage-account-name \
        --set appSecrets.cnvrgStorageAzureContainer=azure-storage-container-name

# GCP - GKE
helm install cnvrg cnvrg/cnvrgio --timeout 1500s --wait \
        --set cnvrgApp.image=cnvrg/app:enterprise-3.1.2 \
        --set cnvrgApp.edition=enterprise \
        --set registry.user=cnvrg-license-username \
        --set registry.password=cnvrg-license-password \
        --set clusterDomain=base.domain \
        --set appSecrets.cnvrgStorageType=gcp \
        --set appSecrets.cnvrgStorageProject=gcp-storage-project
```

#### Deploy OnPrem  (Istio, Minio, HostPath, SMTP, micro storage profile)
```bash
helm install cnvrg cnvrg/cnvrgio --timeout 1500s --wait \
    --set clusterDomain=apps.1.2.3.4.nip.io \
    --set storageProfile=micro \
    --set hostpath.enabled="true" \
    --set hostpath.nodeName="k8s-node-name" \
    --set appConfigs.smtp.server="smtp-server" \
    --set appConfigs.smtp.port="smtp-port" \
    --set appConfigs.smtp.username="smtp-user" \
    --set appConfigs.smtp.password="smtp-pass" \
    --set appConfigs.smtp.domain="domain"
```

#### Deploy OnPrem  (NodePort, Minio, NFS)
```bash
helm install cnvrg cnvrg/cnvrgio --timeout 1500s --wait \
    --set clusterDomain=192.168.1.2 \
    --set ingressType="nodeport" \
    --set nfs.enabled="true" \
    --set nfs.server="NFS.SERVER.IP" \
    --set nfs.path="/shared/nfs/directory"
```

#### Deploy OnPrem  (NodePort, Minio, Hostpath)
```bash
helm install cnvrg cnvrg/cnvrgio --timeout 1500s --wait \
    --set clusterDomain=<node-ip> \
    --set ingressType="nodeport" \
    --set hostpath.enabled="true" \
    --set hostpath.nodeName="<k8s-node>"
```

#### Turn On/Off components
```
helm install cnvrg cnvrg/cnvrgio --timeout 1500s --wait \
    --set cnvrgApp.enabled="false" \
    --set autoscaler.enabled="false" \
    --set cnvrgRouter.enabled="false" \
    --set conf.enabled="false" \
    --set es.enabled="false" \
    --set fluentd.enabled="false" \
    --set hostpath.enabled="false" \
    --set ingress.enabled="false" \
    --set istio.enabled="false" \
    --set kibana.enabled="false" \
    --set prometheus.enabled="false" \
    --set minio.enabled="false" \
    --set mpi.enabled="false" \
    --set nfs.enabled="false" \
    --set nvidiadp.enabled="false" \
    --set pg.enabled="false" \
    --set redis.enabled="false"
```


### Chart options 
|**key**|**default value**|**description**
| ---|---|---|
|`createNs`| true | set to `false` if cnvrg namespaces already exists 
|`specProfile`| default | can be on of the following `default` `microk8s`
|`computeProfile`| default |can be on of the following `default` `micro`
|`storageProfile`| default | can be on of the following `default` `micro`
|`debug`|false|
|`dumpDir`|-|
|`dryRun`|false|
|`privilegedSa`|cnvrg-privileged|
|`clusterDomain`|-|
|`orchestrator`|k8s|
|`securityMode`|default|
|`ingressType`|istio|
|`https.enabled`|false|
|`https.useWildcardCertificate`|true|
|`https.cert`|-|
|`https.key`|-|
|`https.certSecret`|-|
|`conf.enabled`|true|
|`conf.gcpStorageSecret`|gcp-storage-secret|
|`conf.gcpKeyfileMountPath`|/tmp/gcp_keyfile|
|`conf.gcpKeyfileName`|key.json|
|`registry.name`|cnvrg-registry|
|`registry.url`|docker.io|
|`registry.user`|-|
|`registry.password`|-|
|`rbac.role`|cnvrg-role|
|`rbac.serviceAccountName`|cnvrg|
|`rbac.roleBindingName`|cnvrg-role-binding|
|`appConfigs.cnvrgStorageUseIamRole`|false|
|`appConfigs.featureFlags`|-|Dynamic feature flags passed to be passed to the app as environment variables, exmpale: `--set appConfigs.featureFlags=KEY1=VAL;KEY2=VAL2`
|`appConfigs.smtp.server`|-|
|`appConfigs.smtp.port`|-|
|`appConfigs.smtp.username`|-|
|`appConfigs.smtp.password`|-|
|`appConfigs.smtp.domain`|-|
|`appSecrets.sentryUrl`|https://4409141e4a204282bd1f5c021e587509:dc15f684faa9479a839cf913b98b4ee2@sentry.cnvrg.io/32|
|`appSecrets.secretKeyBase`|0d2b33c2cc19cfaa838d3c354354a18fcc92beaaa8e97889ef99341c8aaf963ad3afcf0f7c20454cabb5c573c3fc35b60221034e109f4fb651ed1415bf61e9d5|
|`appSecrets.stsIv`|DeJ/CGz/Hkb/IbRe4t1xLg==|
|`appSecrets.stsKey`|05646d3cbf8baa5be7150b4283eda07d|
|`appSecrets.passengerAppEnv`|app|
|`appSecrets.railsEnv`|app|
|`appSecrets.runJobsOnSelfCluster`|true|
|`appSecrets.defaultComputeConfig`|/opt/kube|
|`appSecrets.defaultComputeName`|default|
|`appSecrets.useStdout`|true|
|`appSecrets.extractTagsFromCmd`|false|
|`appSecrets.checkJobExpiration`|true|
|`appSecrets.cnvrgStorageType`|minio|
|`appSecrets.cnvrgStorageBucket`|cnvrg-storage|
|`appSecrets.cnvrgStorageAccessKey`|AKIAIOSFODNN7EXAMPLE|
|`appSecrets.cnvrgStorageSecretKey`|wJalrXUtnFEMI/K7MDENG/bPxRfiCYEXAMPLEKEY|
|`appSecrets.minioSseMasterKey`|my-minio-key:a310aadcefdb634b748ae31225f175e3f64591f955dfc66ccc20e128a6817ff9|
|`appSecrets.cnvrgStorageAzureAccessKey`|-|
|`appSecrets.cnvrgStorageAzureAccountName`|-|
|`appSecrets.cnvrgStorageAzureContainer`|-|
|`appSecrets.cnvrgStorageRegion`|eastus|
|`appSecrets.cnvrgStorageProject`|-|
|`redis.enabled`|true|
|`redis.image`|redis:3.0.5|
|`redis.svcName`|redis|
|`redis.port`|6379|
|`redis.limits.cpu`|1|
|`redis.limits.memory`|2Gi|
|`redis.requests.cpu`|500m|
|`redis.requests.memory`|1Gi|
|`pg.enabled`|true|
|`pg.image`|centos/postgresql-12-centos7|
|`pg.port`|5432|
|`pg.storageSize`|80Gi|
|`pg.svcName`|postgres|
|`pg.dbname`|cnvrg_production|
|`pg.pass`|pg_pass|
|`pg.user`|cnvrg|
|`pg.runAsUser`|26|
|`pg.runAsGroup`|26|
|`pg.fsGroup`|26|
|`pg.storageClass`|use-default|
|`pg.cpuRequest`|1|
|`pg.memoryRequest`|2Gi|
|`pg.hugePages.enabled`|false|
|`pg.hugePages.size`|-|
|`pgBackup.storageSize`|30Gi|
|`pgBackup.enabled`|false|
|`pgBackup.name`|pg-backup|
|`pgBackup.path`|/opt/cnvrg-backups|
|`pgBackup.scriptPath`|/opt/script|
|`pgBackup.storageClass`|use-default|
|`pgBackup.cronTime`|1 1 * * *|
|`es.enabled`|true|
|`es.image`|docker.io/cnvrg/cnvrg-es:v7.8.1|
|`es.maxMapImage`|docker.io/cnvrg/cnvrg-tools:v0.3|
|`es.port`|9200|
|`es.storageSize`|30Gi|
|`es.svcName`|elasticsearch|
|`es.runAsUser`|1000|
|`es.runAsGroup`|1000|
|`es.fsGroup`|1000|
|`es.patchEsNodes`|true|
|`es.nodePort`|32200|
|`es.storageClass`|use-default|
|`es.cpuRequest`|1|
|`es.memoryRequest`|1Gi|
|`es.cpuLimit`|2|
|`es.memoryLimit`|4Gi|
|`es.javaOpts`|-|
|`minio.enabled`|true|
|`minio.replicas`|1|
|`minio.image`|docker.io/cnvrg/cnvrg-minio:RELEASE.2019-04-09T01-22-30Z.3|
|`minio.port`|9000|
|`minio.storageSize`|100Gi|
|`minio.svcName`|minio|
|`minio.nodePort`|30090|
|`minio.storageClass`|use-default|
|`minio.memoryRequest`|4Gi|
|`minio.sharedStorage.enabled`|false|
|`minio.sharedStorage.storageClassName`|minio-shared-backend|
|`minio.sharedStorage.nfsServer`|-|
|`minio.sharedStorage.path`|-|
|`prometheus.enabled`|true|
|`prometheus.image`|quay.io/prometheus/prometheus:v2.17.2|
|`prometheus.operatorImage`|quay.io/coreos/prometheus-operator:v0.38.1|
|`prometheus.configReloaderImage`|jimmidyson/configmap-reload:v0.3.0|
|`prometheus.prometheusConfigReloaderImage`|quay.io/coreos/prometheus-config-reloader:v0.38.1|
|`prometheus.kubeRbacProxyImage`|quay.io/coreos/kube-rbac-proxy:v0.4.1|
|`prometheus.kubeStateMetricsImage`|quay.io/coreos/kube-state-metrics:v1.9.5|
|`prometheus.alertManagerImage`|quay.io/prometheus/alertmanager:v0.20.0|
|`prometheus.adapterImage`|directxman12/k8s-prometheus-adapter:v0.7.0|
|`prometheus.nvidiaExporterImage`|nvidia/dcgm-exporter:1.7.2|
|`prometheus.nodeExporterImage`|quay.io/prometheus/node-exporter:v0.18.1|
|`prometheus.svcName`|prometheus|
|`prometheus.port`|9090|
|`prometheus.nodePort`|30909|
|`prometheus.storageSize`|40Gi|
|`prometheus.storageClass`|use-default|
|`prometheus.kubeletMetrics.schema`|https|
|`prometheus.kubeletMetrics.port`|https-metrics|
|`grafana.svcName`|grafana|
|`grafana.port`|3000|
|`grafana.image`|grafana/grafana:6.7.4|
|`grafana.nodePort`|30012|
|`istio.enabled`|true|
|`istio.operatorImage`|docker.io/istio/operator:1.6.0|
|`istio.hub`|docker.io/istio|
|`istio.tag`|1.6.0|
|`istio.proxyImage`|proxyv2|
|`istio.mixerImage`|mixer|
|`istio.pilotImage`|pilot|
|`istio.gwName`|cnvrg-gateway|
|`istio.externalIp`|-|
|`istio.ingressSvcAnnotations`|-|
|`kibana.enabled`|true|
|`kibana.svcName`|kibana|
|`kibana.port`|5601|
|`kibana.image`|docker.elastic.co/kibana/kibana-oss:7.8.1|
|`kibana.nodePort`|30601|
|`kibana.cpuRequest`|500m|
|`kibana.memoryRequest`|500Mi|
|`kibana.cpuLimit`|1|
|`kibana.memoryLimit`|2000Mi|
|`fluentd.enabled`|true|
|`fluentd.image`|fluent/fluentd-kubernetes-daemonset:v1.11.0-debian-elasticsearch6-1.0|
|`fluentd.journalPath`|/var/log/journal|
|`fluentd.containersPath`|/var/lib/docker/containers|
|`fluentd.journald`|false|
|`fluentd.cpuRequest`|100m|
|`fluentd.memoryRequest`|200Mi|
|`fluentd.memoryLimit`|200Mi|
|`nvidiadp.enabled`|true|
|`nvidiadp.image`|nvidia/k8s-device-plugin:v0.7.0-rc.1-ubi8|
|`nvidiadp.nodeSelector.enabled`|true|
|`nvidiadp.nodeSelector.key`|accelerator|
|`nvidiadp.nodeSelector.value`|nvidia|
|`mpi.enabled`|false|
|`cnvrgApp.replicas`|1|
|`cnvrgApp.edition`|core|
|`cnvrgApp.enabled`|true|
|`cnvrgApp.image`|-|
|`cnvrgApp.port`|80|
|`cnvrgApp.cpu`|1|
|`cnvrgApp.memory`|4Gi|
|`cnvrgApp.svcName`|app|
|`cnvrgApp.customAgentTag`|false|
|`cnvrgApp.intercom`|true|
|`cnvrgApp.nodePort`|30080|
|`cnvrgApp.sidekiqCpu`|1|
|`cnvrgApp.sidekiqMemory`|2Gi|
|`cnvrgApp.sidekiqReplicas`|2|
|`cnvrgApp.sidekiqSearchkickCpu`|1|
|`cnvrgApp.sidekiqSearchkickMemory`|2Gi|
|`cnvrgApp.sidekiqSearchkickReplicas`|1|
|`seeder.image`|docker.io/cnvrg/cnvrg-boot:v0.23|
|`seeder.seedCmd`|rails db:migrate && rails db:seed && rails libraries:update|
|`nfs.enabled`|false|
|`nfs.image`|quay.io/external_storage/nfs-client-provisioner:latest|
|`nfs.provisioner`|cnvrg.io/ifs|
|`nfs.storageClassName`|cnvrg-nfs-storage|
|`nfs.server`|-|
|`nfs.path`|-|
|`nfs.cpuRequest`|100m|
|`nfs.memoryRequest`|100Mi|
|`nfs.cpuLimit`|200m|
|`nfs.memoryLimit`|200Mi|
|`hostpath.enabled`|false|
|`hostpath.image`|quay.io/kubevirt/hostpath-provisioner|
|`hostpath.hostPath`|/cnvrg-storage|
|`hostpath.storageClassName`|cnvrg-hostpath-provisioner|
|`hostpath.nodeName`|-|
|`hostpath.cpuRequest`|100m|
|`hostpath.memoryRequest`|100Mi|
|`hostpath.cpuLimit`|200m|
|`hostpath.memoryLimit`|200Mi|
|`autoscaler.enabled`|false|
|`ingress.enabled`|true|either create ingress rules or not based on `ingressType`,if set to false,none of the ingress rules will be created
|`cnvrgRouter.enabled`|false|
|`cnvrgRouter.image`|nginx|
|`cnvrgRouter.svcName`|routing-service|
|`cnvrgRouter.nodePort`|30081|
|`cnvrgRouter.port`|80|
