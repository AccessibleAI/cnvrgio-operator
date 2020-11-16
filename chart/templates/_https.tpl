{{- define "spec.https" }}
https:
  enabled: "{{ .Values.https.enabled }}"
  useWildcardCertificate: "{{ .Values.https.useWildcardCertificate }}"
  cert: "{{ .Values.https.cert }}"
  key: "{{ .Values.https.key }}"
  certSecret: "{{ .Values.https.certSecret }}"
{{- end }}
