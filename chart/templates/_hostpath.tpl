{{- define "spec.hostpath"  }}
hostpath:
  enabled: "{{ .Values.hostpath.enabled }}"
  image: "{{.Values.hostpath.image}}"
  hostPath: "{{ .Values.hostpath.hostPath }}"
  storageClassName: "{{ .Values.hostpath.storageClassName }}"
  nodeName: "{{ .Values.hostpath.nodeName }}"
  cpuRequest: "{{ .Values.hostpath.cpuRequest }}"
  memoryRequest: "{{ .Values.hostpath.memoryRequest }}"
  cpuLimit: "{{ .Values.hostpath.cpuLimit }}"
  memoryLimit: "{{ .Values.hostpath.memoryLimit }}"
{{- end }}