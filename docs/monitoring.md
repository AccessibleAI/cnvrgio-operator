# CNVRG Monitoring stack

### Integration with external Prometheus
 
#### Required Prometheus exporters
* [kube-state-metrics](https://github.com/kubernetes/kube-state-metrics)
* [node-exporter](https://github.com/prometheus/node_exporter)
* [dcgm-exporter](https://github.com/NVIDIA/gpu-monitoring-tools)

#### Required Prometheus rules (use either kube-prometheus rules, or vanilla prometheus rules yaml file)
* [kube-prometheus-rules](https://github.com/prometheus-operator/kube-prometheus/blob/master/manifests/prometheus-rules.yaml)
* [kube-prometheus-rules.yaml](./kube-prometheus-rules.yaml)
 