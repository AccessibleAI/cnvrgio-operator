{{- define "spec.ingress" }}
ingress:
  enabled: "{{ .Values.ingress.enabled }}"
{{- end }}