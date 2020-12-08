### Upgrades 

To upgrade from version <  1.40 run the following command
```bash
 helm upgrade cnvrg cnvrg/cnvrg --reuse-values \
 --set monitoring.enabled="true" \
 --set monitoring.prometheusOperator.enabled="true" \
 --set monitoring.prometheusOperator.images.operatorImage="quay.io/coreos/prometheus-operator:v0.40.0" \
 --set monitoring.prometheusOperator.images.configReloaderImage="jimmidyson/configmap-reload:v0.3.0" \
 --set monitoring.prometheusOperator.images.prometheusConfigReloaderImage="quay.io/coreos/prometheus-config-reloader:v0.40.0" \
 --set monitoring.prometheusOperator.images.kubeRbacProxyImage="quay.io/coreos/kube-rbac-proxy:v0.4.1" \
 --set monitoring.prometheus.enabled="true" \
 --set monitoring.prometheus.image="quay.io/prometheus/prometheus:v2.22.2" \
 --set monitoring.prometheus.cpuRequest="1" \
 --set monitoring.prometheus.memoryRequest="1Gi" \
 --set monitoring.prometheus.svcName="prometheus" \
 --set monitoring.prometheus.port="9090" \
 --set monitoring.prometheus.nodePort="30909" \
 --set monitoring.prometheus.storageSize="100Gi" \
 --set monitoring.prometheus.storageClass="use-default" \
 --set monitoring.nodeExporter.enabled="true" \
 --set monitoring.nodeExporter.port="9100" \
 --set monitoring.nodeExporter.image="quay.io/prometheus/node-exporter:v0.18.1" \
 --set monitoring.kubeStateMetrics.enabled="true" \
 --set monitoring.kubeStateMetrics.image="quay.io/coreos/kube-state-metrics:v1.9.5" \
 --set monitoring.grafana.enabled="true" \
 --set monitoring.grafana.image="grafana/grafana:7.1.0" \
 --set monitoring.grafana.svcName="grafana" \
 --set monitoring.grafana.port="3000" \
 --set monitoring.grafana.nodePort="30012" \
 --set monitoring.defaultServiceMonitors.enabled="true" \
 --set monitoring.sidekiqExporter.enabled="true" \
 --set monitoring.sidekiqExporter.image="docker.io/strech/sidekiq-prometheus-exporter:0.1.13" \
 --set monitoring.minioExporter.enabled="true" \
 --set monitoring.minioExporter.image="docker.io/cnvrg/cnvrg-boot:v0.24" \
 --set monitoring.dcgmExporter.enabled="true" \
 --set monitoring.dcgmExporter.image="nvidia/dcgm-exporter:1.7.2" \
 --set monitoring.dcgmExporter.port="9400" \
 --set monitoring.idleMetricsExporter.enabled="true" \
 --set monitoring.metricsServer.enabled="true" \
 --set monitoring.metricsServer.image="k8s.gcr.io/metrics-server/metrics-server:v0.3.7"
```

