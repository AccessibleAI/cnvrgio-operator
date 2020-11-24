{{- define "spec.fluentd" }}
fluentd:
  enabled: "{{ .Values.fluentd.enabled }}"
  image: "{{.Values.fluentd.image}}"
  journalPath: "{{ .Values.fluentd.journalPath }}"
  containersPath: "{{ .Values.fluentd.containersPath }}"
  journald: "{{ .Values.fluentd.journald }}"
  cpuRequest: "{{ .Values.fluentd.cpuRequest }}"
  memoryRequest: "{{ .Values.fluentd.memoryRequest }}"
  memoryLimit: "{{ .Values.fluentd.memoryLimit }}"
{{- end }}