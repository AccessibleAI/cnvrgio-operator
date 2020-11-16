{{- define "spec.promehteus" }}
prometheus:
  enabled: "{{ .Values.prometheus.enabled }}"
  image: "{{ .Values.prometheus.image }}"
  operatorImage: "{{ .Values.prometheus.operatorImage }}"
  configReloaderImage: "{{ .Values.prometheus.configReloaderImage }}"
  prometheusConfigReloaderImage: "{{ .Values.prometheus.prometheusConfigReloaderImage }}"
  kubeRbacProxyImage: "{{ .Values.prometheus.kubeRbacProxyImage }}"
  kubeStateMetricsImage: "{{ .Values.prometheus.kubeStateMetricsImage }}"
  alertManagerImage: "{{ .Values.prometheus.alertManagerImage }}"
  adapterImage: "{{ .Values.prometheus.adapterImage }}"
  nvidiaExporterImage: "{{ .Values.prometheus.nvidiaExporterImage }}"
  nodeExporterImage: "{{ .Values.prometheus.nodeExporterImage }}"
  sidekickExporterImage: "{{ .Values.prometheus.sidekickExporterImage }}"
  cnvrgBootImage: "{{ .Values.prometheus.cnvrgBootImage }}"
  svcName: "{{ .Values.prometheus.svcName }}"
  port: "{{ .Values.prometheus.port }}"
  nodePort: "{{ .Values.prometheus.nodePort }}"
  storageClass: "{{ .Values.prometheus.storageClass }}"
  kubeletMetrics:
    schema: "{{ .Values.prometheus.kubeletMetrics.schema }}"
    port: "{{ .Values.prometheus.kubeletMetrics.port }}"

  {{- if eq .Values.computeProfile "large"}}
  cpuRequest: "{{.Values.computeProfiles.large.prometheus.cpu}}"
  memoryRequest: "{{.Values.computeProfiles.large.prometheus.memory}}"
  storageSize: "{{.Values.computeProfiles.large.storage}}"
  {{- end }}

  {{- if eq .Values.computeProfile "medium"}}
  cpuRequest: "{{.Values.computeProfiles.medium.prometheus.cpu}}"
  memoryRequest: "{{.Values.computeProfiles.medium.prometheus.memory}}"
  storageSize: "{{.Values.computeProfiles.medium.storage}}"
  {{- end }}

  {{- if eq .Values.computeProfile "small"}}
  cpuRequest: "{{.Values.computeProfiles.small.prometheus.cpu}}"
  memoryRequest: "{{.Values.computeProfiles.small.prometheus.memory}}"
  storageSize: "{{.Values.computeProfiles.small.storage}}"
  {{- end }}
grafana:
  svcName: "{{ .Values.grafana.svcName }}"
  port: "{{ .Values.grafana.port }}"
  image: "{{ .Values.grafana.image }}"
  nodePort: "{{ .Values.grafana.nodePort }}"
{{- end }}