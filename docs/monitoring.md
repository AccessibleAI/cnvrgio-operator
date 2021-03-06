# CNVRG Monitoring stack

cnvrg can deploy end-to-end kubernetes native monitoring stack
The monitoring stack cnvrg deploys is based on [kube-prometheus](https://github.com/prometheus-operator/kube-prometheus)
and includes the following components.
* Prometheus Operator
* Prometheus
* Prometheus node-exporter
* kube-state-metrics
* Grafana

The monitoring stack can be fully as well as partially enabled or disabled.
The configurations below shows the configuration parameters for monitoring stack.

Configure monitoring stack with helm chart flags 
```bash
# completely enable or disable monitoring stack
--set monitoring.enabled=<"true"|"false">

# enable or disable prometheus operator 
--set monitoring.prometheusOperator.enabled=<"true"|"false">

# enable or disable prometheus instance 
--set monitoring.prometheus.enabled=<"true"|"false">

# enable or disable prometheus node exporter  
--set monitoring.nodeExporter.enabled=<"true"|"false">

# enable or disable kube state metrics  
--set monitoring.kubeStateMetrics.enabled=<"true"|"false">

# enable or disable Grafana 
--set monitoring.grafana.enabled=<"true"|"false">

# enable or disable default service monitors, (full list of default monitors is here: roles/monitoring/templates/default-service-monitors)
--set monitoring.defaultServiceMonitors.enabled=<"true"|"false">

# enable or disable sidekiq exporter
--set monitoring.sidekiqExporter.enabled=<"true"|"false">

# enable or disable minio exporter
--set monitoring.minioExporter.enabled=<"true"|"false">

# enable or disable dcgm exporter
--set monitoring.dcgmExporter.enabled=<"true"|"false">

# enable or disable idle metrics exporter
--set monitoring.idleMetricsExporter.enabled=<"true"|"false">
```

Configure monitoring stack with CnvrgApp CR 
```yaml
monitoring:
  enabled: "true|false"
  prometheusOperator:
    enabled: "true|false"
  prometheus:
    enabled: "true|false"
  nodeExporter:
    enabled: "true|false"
  kubeStateMetrics:
    enabled: "true|false"
  grafana:
    enabled: "true|false"
  defaultServiceMonitors:
    enabled: "true|false"
  sidekiqExporter:
    enabled: "true|false"
  minioExporter:
    enabled: "true|false"
  dcgmExporter:
    enabled: "true|false"
  idleMetricsExporter:
    enabled: "true|false"
```
### Integration with external Prometheus - Prometheus Federation (supported setup)

To scrap all metrics from cnvrg Prometheus instance add the following into yours Prometheus instance 
```yaml
  - job_name: cnvrg_app_cluster_federation_all_exporters
    honor_labels: true
    metrics_path: /federate
    params:
      match[]:
        - '{job=~".+"}'
    static_configs:
      - targets:
        - <cnvrg-prometheus-url>
```

To scrap cnvrg specific metrics from cnvrg Prometheus instance add the following into yours Prometheus instance
```yaml
  - job_name: cnvrg_app_cluster_federation_minimum_required_exporters
    honor_labels: true
    metrics_path: /federate
    params:
      match[]:
        - '{job=~"kube-state-metrics|node-exporter|dcgm-exporter|cnvrg-job|sidekiq-prometheus-exporter|minio"}'
    static_configs:
      - targets:
        - <cnvrg-prometheus-url>
```

External labels for identify cnvrg Prometheus federated metrics
```bash
cnvrg_cluster="<cnvrg-cluster-domain>"
``` 
For example, execute following query on upstream Prometheus instance 
where `cnvrg_cluster` equals source `"<cnvrg-cluster-domain>"`  
```bash
node_memory_MemFree_bytes{cnvrg_cluster="<cnvrg-cluster-domain>"}
```  

For debugging purpose, you may use the following commands 
to check if desired metrics available on cnvrg Prometheus instance  

```bash
curl -G --data-urlencode 'match[]={job=~".+"}' <cnvrg-prometheus-url>/federate
# or 
curl -sG --data-urlencode 'match[]={job=~"kube-state-metrics|node-exporter|dcgm-exporter|cnvrg-job|sidekiq-prometheus-exporter|minio"}' <cnvrg-prometheus-url>/federate
```
    
### Integration with external Prometheus without Prometheus Federation (not supported method - the application functionality may be partially broken in such a setup)
 
#### Prometheus exporters 
* [kube-state-metrics](https://github.com/kubernetes/kube-state-metrics)
* [node-exporter](https://github.com/prometheus/nodeExporter)
* [dcgm-exporter](https://github.com/NVIDIA/gpu-monitoring-tools)
* [sidekiq-exporter](../roles/monitoring/templates/sidekiq-exporter)

#### Prometheus Service Monitors
* [kube-state-metrics-service-monitor](../roles/monitoring/templates/kube-state-metrics/kube-state-metrics-serviceMonitor.yaml)
* [node-exporter-service-monitor](../roles/monitoring/templates/node-exporter/node-exporter-serviceMonitor.yaml)
* [dcgm-exporter-service-monitor](../roles/monitoring/templates/dcgm-exporter/service-monitor.yml)
* [idle-metrics-service-monitor](../roles/monitoring/templates/idle-metrics-exporter/service-monitor.yaml)
* [sidekiq-exporter](../roles/monitoring/templates/sidekiq-exporter/sidekiq-exporter-serviceMonitor.yaml)
* [minio-service-monitor](../roles/monitoring/templates/minio-exporter/prometheus-minio-serviceMonitor.yaml)


#### Required Prometheus rules (use either kube-prometheus rules, or vanilla prometheus rules yaml file)
* [kube-prometheus-rules](https://github.com/prometheus-operator/kube-prometheus/blob/master/manifests/prometheus-rules.yaml)  or [kube-prometheus-rules.yaml](./kube-prometheus-rules.yaml)
 