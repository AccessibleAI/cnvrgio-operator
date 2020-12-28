{{- define "spec.hyper" }}
hyper:
  enabled: "{{ .Values.hyper.enabled }}"
  image: "{{ .Values.hyper.image }}"
  port: "{{ .Values.hyper.port }}"
  nodePort: "{{ .Values.hyper.enabled }}"
  svcName: "{{ .Values.hyper.svcName }}"
  replicas: "{{ .Values.hyper.replicas }}"
  enableReadinessProbe: "{{.Values.hyper.enableReadinessProbe}}"
  readinessPeriodSeconds: "{{.Values.hyper.readinessPeriodSeconds}}"
  readinessTimeoutSeconds: "{{.Values.hyper.readinessTimeoutSeconds}}"

  {{- if eq .Values.computeProfile "large"}}
  cpuRequest: "{{ .Values.computeProfiles.large.hyper.cpu }}"
  memoryRequest: "{{ .Values.computeProfiles.large.hyper.memory }}"
  cpuLimit: "{{ .Values.computeProfiles.large.hyper.cpu }}"
  memoryLimit: "{{ .Values.computeProfiles.large.hyper.memory }}"
  {{- end }}

  {{- if eq .Values.computeProfile "medium"}}
  cpuRequest: "{{ .Values.computeProfiles.medium.hyper.cpu }}"
  memoryRequest: "{{ .Values.computeProfiles.medium.hyper.memory }}"
  cpuLimit: "{{ .Values.computeProfiles.medium.hyper.cpu }}"
  memoryLimit: "{{ .Values.computeProfiles.medium.hyper.memory }}"
  {{- end }}

  {{- if eq .Values.computeProfile "small"}}
  cpuRequest: "{{ .Values.computeProfiles.small.hyper.cpu }}"
  memoryRequest: "{{ .Values.computeProfiles.small.hyper.memory }}"

  {{- end }}
{{- end }}