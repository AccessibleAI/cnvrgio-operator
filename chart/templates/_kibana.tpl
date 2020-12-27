{{- define "spec.kibana" }}
kibana:
  enabled: "{{ .Values.kibana.enabled }}"
  svcName: "{{ .Values.kibana.svcName }}"
  image: "{{ .Values.kibana.image }}"
  nodePort: "{{ .Values.kibana.nodePort }}"
  cpuRequest: "{{ .Values.kibana.cpuRequest }}"
  memoryRequest: "{{ .Values.kibana.memoryRequest }}"
  cpuLimit: "{{ .Values.kibana.cpuLimit }}"
  memoryLimit: "{{ .Values.kibana.memoryLimit }}"
  port: "{{ .Values.kibana.port }}"
{{- end }}