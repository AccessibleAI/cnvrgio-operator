{{- define "spec.ingress" }}
ingress:
  enabled: "{{ .Values.ingress.enabled }}"
  timeout: "{{ .Values.ingress.timeout }}"
  retriesAttempts: "{{ .Values.ingress.retriesAttempts }}"
  perTryTimeout: "{{ .Values.ingress.perTryTimeout }}"
{{- end }}