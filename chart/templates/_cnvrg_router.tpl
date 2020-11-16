{{- define "spec.cnvrgRouter" }}
cnvrgRouter:
  enabled: "{{ .Values.cnvrgRouter.enabled }}"
  image: "{{.Values.cnvrgRouter.image}}"
  svcName: "{{ .Values.cnvrgRouter.svcName }}"
  nodePort: "{{ .Values.cnvrgRouter.nodePort }}"
  port: "{{ .Values.cnvrgRouter.port}}"
{{- end }}