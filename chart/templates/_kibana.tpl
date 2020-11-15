{{- define "spec.kibana" }}
kibana:
  enabled: "{{ .Values.kibana.enabled }}"
  svcName: "{{ .Values.kibana.svcName }}"
  image: "{{ .Values.kibana.image }}"
  nodePort: "{{ .Values.kibana.nodePort }}"
  {{- if eq .Values.computeProfile "default"}}
  cpuRequest: "{{ .Values.kibana.cpuRequest }}"
  memoryRequest: "{{ .Values.kibana.memoryRequest }}"
  cpuLimit: "{{ .Values.kibana.cpuLimit }}"
  memoryLimit: "{{ .Values.kibana.memoryLimit }}"
  {{- end }}
  {{- if eq .Values.computeProfile "micro"}}
  cpuRequest: "{{ .Values.computeProfiles.micro.kibana.cpu }}"
  memoryRequest: "{{ .Values.computeProfiles.micro.kibana.memory }}"
  cpuLimit: "{{ .Values.computeProfiles.micro.kibana.cpu }}"
  memoryLimit: "{{ .Values.computeProfiles.micro.kibana.memory }}"
  {{- end }}
  port: "{{ .Values.kibana.port }}"
{{- end }}