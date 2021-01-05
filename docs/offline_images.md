# cnvrg.io operator
## Deploy cnvrg stack with custom repo

### Quick start

#### List of images to download
```
docker.io/cnvrg/cnvrg-operator
docker.io/cnvrg/cnvrg-tools:v0.3
docker.io/redis:3.0.5
docker.io/centos/postgresql-12-centos7
docker.io/cnvrg/cnvrg-es:v7.8.1
docker.io/cnvrg/cnvrg-tools:v0.3
docker.io/minio/minio:RELEASE.2020-09-17T04-49-20Z
docker.io/quay.io/coreos/prometheus-operator:v0.40.0
docker.io/jimmidyson/configmap-reload:v0.3.0
docker.io/quay.io/coreos/prometheus-config-reloader:v0.40.0
docker.io/quay.io/coreos/kube-rbac-proxy:v0.4.1
docker.io/quay.io/prometheus/prometheus:v2.22.2
docker.io/quay.io/prometheus/node-exporter:v0.18.1
docker.io/quay.io/coreos/kube-state-metrics:v1.9.5
docker.io/grafana/grafana:7.1.0
docker.io/strech/sidekiq-prometheus-exporter:0.1.13
docker.io/cnvrg/cnvrg-boot:v0.24
docker.io/nvidia/dcgm-exporter:1.7.2
docker.io/k8s.gcr.io/metrics-server/metrics-server:v0.3.7
docker.io/istio/operator:1.7.3
docker.io/istio/proxyv2
docker.io/istio/mixer
docker.io/istio/pilot
docker.elastic.co/kibana/kibana-oss:7.8.1
docker.io/fluent/fluentd-kubernetes-daemonset:v1.11-debian-elasticsearch7-1
docker.io/nvidia/k8s-device-plugin:v0.7.0
docker.io/mpioperator/mpi-operator:v0.2.3
docker.io/mpioperator/kubectl-delivery:v0.2.3
docker.io/cnvrg/core:3.1.2
docker.io/cnvrg/cnvrg-boot:v0.23
docker.io/quay.io/external_storage/nfs-client-provisioner:latest
docker.io/quay.io/kubevirt/hostpath-provisioner
docker.io/nginx

```

### Helm command to install with custom repo
```
helm install cnvrg cnvrg/cnvrgio --timeout 1500s --wait \
--set operatorImage offline_repo/cnvrg/cnvrg-operator \
--set hookImage offline_repo/cnvrg/cnvrg-tools:v0.3 \
--set redis.image offline_repo/redis:3.0.5 \
--set pg.image offline_repo/centos/postgresql-12-centos7 \
--set logging.es.image offline_repo/cnvrg/cnvrg-es:v7.8.1 \
--set logging.es.maxMapImage offline_repo/cnvrg/cnvrg-tools:v0.3 \
--set minio.image offline_repo/minio/minio:RELEASE.2020-09-17T04-49-20Z \
--set monitoring.prometheusOperator.images.operatorImage offline_repo/coreos/prometheus-operator:v0.40.0 \
--set monitoring.prometheusOperator.images.configReloaderImage offline_repo/jimmidyson/configmap-reload:v0.3.0 \
--set monitoring.prometheusOperator.images.prometheusConfigReloaderImage offline_repo/coreos/prometheus-config-reloader:v0.40.0 \
--set monitoring.prometheusOperator.images.kubeRbacProxyImage offline_repo/coreos/kube-rbac-proxy:v0.4.1 \
--set monitoring.prometheus.image offline_repo/prometheus/prometheus:v2.22.2 \
--set monitoring.nodeExporter.image offline_repo/prometheus/node-exporter:v0.18.1 \
--set monitoring.kubeStateMetrics.image offline_repo/coreos/kube-state-metrics:v1.9.5 \
--set monitoring.grafana.image offline_repo/grafana/grafana:7.1.0 \
--set monitoring.sidekiqExporter.image offline_repo/strech/sidekiq-prometheus-exporter:0.1.13 \
--set monitoring.minioExporter.image offline_repo/cnvrg/cnvrg-boot:v0.24 \
--set monitoring.dcgmExporter.image offline_repo/nvidia/dcgm-exporter:1.7.2 \
--set monitoring.metricsServer.image offline_repo/metrics-server/metrics-server:v0.3.7 \
--set networking.istio.operatorImage offline_repo/istio/operator:1.7.3 \
--set networking.istio.proxyImage offline_repo/istio/proxyv2 \
--set networking.istio.mixerImage offline_repo/istio/mixer \
--set networking.istio.pilotImage offline_repo/istio/pilot \
--set logging.kibana.image offline_repo/kibana/kibana-oss:7.8.1 \
--set logging.fluentd.image offline_repo/fluent/fluentd-kubernetes-daemonset:v1.11-debian-elasticsearch7-1 \
--set nvidiadp.image offline_repo/nvidia/k8s-device-plugin:v0.7.0 \
--set mpi.image offline_repo/mpioperator/mpi-operator:v0.2.3 \
--set mpi.kubectlDeliveryImage offline_repo/mpioperator/kubectl-delivery:v0.2.3 \
--set cnvrgApp.image offline_repo/cnvrg/core:3.1.2 \
--set seeder.image offline_repo/cnvrg/cnvrg-boot:v0.23 \
--set storage.nfs.image offline_repo/external_storage/nfs-client-provisioner:latest \
--set storage.hostpath.image offline_repo/kubevirt/hostpath-provisioner \
--set cnvrgRouter.image offline_repo/nginx \

```