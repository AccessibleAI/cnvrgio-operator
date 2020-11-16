{{- define "spec.nfs" }}
nfs:
  enabled: "{{ .Values.nfs.enabled }}"
  image: "{{.Values.nfs.image}}"
  provisioner: "{{ .Values.nfs.provisioner }}"
  storageClassName: "{{ .Values.nfs.storageClassName }}"
  server: "{{ .Values.nfs.server }}"
  path: "{{ .Values.nfs.path }}"
  cpuRequest: "{{ .Values.nfs.cpuRequest }}"
  memoryRequest: "{{ .Values.nfs.memoryRequest }}"
  cpuLimit: "{{ .Values.nfs.cpuLimit }}"
  memoryLimit: "{{ .Values.nfs.memoryLimit }}"
{{- end }}
