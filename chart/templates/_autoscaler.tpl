{{- define "spec.autoscaler" }}
autoscaler:
  enabled: "{{ .Values.autoscaler.enabled }}"
{{- end }}