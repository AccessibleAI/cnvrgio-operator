{{- define "spec.es" }}
es:
  enabled: "{{ .Values.es.enabled }}"
  image: "{{ .Values.es.image }}"
  maxMapImage: "{{.Values.es.maxMapImage}}"
  port: "{{ .Values.es.port }}"
  svcName: "{{ .Values.es.svcName }}"
  runAsUser: "{{ .Values.es.runAsUser }}"
  runAsGroup: "{{ .Values.es.runAsGroup }}"
  fsGroup: "{{ .Values.es.fsGroup }}"
  patchEsNodes: "{{ .Values.es.patchEsNodes }}"
  nodePort: "{{ .Values.es.nodePort }}"
  storageClass: "{{ .Values.es.storageClass }}"
  javaOpts: "{{ .Values.es.javaOpts }}"
  cpuLimit: "{{.Values.es.cpuLimit}}"
  memoryLimit: "{{.Values.es.memoryLimit}}"

  {{- if eq .Values.computeProfile "large"}}
  cpuRequest: "{{ .Values.computeProfiles.large.es.cpu }}"
  memoryRequest: "{{ .Values.computeProfiles.large.es.memory }}"
  storageSize: "{{ .Values.computeProfiles.large.storage }}"
  {{- end }}

  {{- if eq .Values.computeProfile "medium"}}
  cpuRequest: "{{ .Values.computeProfiles.medium.es.cpu }}"
  memoryRequest: "{{ .Values.computeProfiles.medium.es.memory }}"
  storageSize: "{{ .Values.computeProfiles.medium.storage }}"
  {{- end }}

  {{- if eq .Values.computeProfile "small"}}
  cpuRequest: "{{ .Values.computeProfiles.small.es.cpu }}"
  memoryRequest: "{{ .Values.computeProfiles.small.es.memory }}"
  storageSize: "{{ .Values.computeProfiles.small.storage }}"

  {{- end }}
{{- end }}