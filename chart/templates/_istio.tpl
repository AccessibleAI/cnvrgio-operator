{{- define "spec.istio" }}
istio:
  enabled: "{{ .Values.istio.enabled }}"
  operatorImage: "{{ .Values.istio.operatorImage }}"
  hub: "{{.Values.istio.hub}}"
  tag: "{{.Values.istio.tag}}"
  proxyImage: "{{.Values.istio.proxyImage}}"
  mixerImage: "{{.Values.istio.mixerImage}}"
  pilotImage: "{{.Values.istio.pilotImage}}"
  gwName: "{{ .Values.istio.gwName }}"
  externalIp: "{{ .Values.istio.externalIp }}"
  ingressSvcAnnotations: "{{.Values.istio.ingressSvcAnnotations}}"
{{- end }}
