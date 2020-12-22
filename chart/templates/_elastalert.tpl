{{- define "spec.elastalert" }}
elastalert:
  enabled: "{{ .Values.elastalert.enabled }}"
  image: "{{ .Values.elastalert.image }}"
  port: "{{ .Values.elastalert.port }}"
  nodePort: "{{ .Values.elastalert.nodePort }}"
  containerPort: "{{ .Values.elastalert.containerPort }}"
  storageSize: "{{ .Values.elastalert.storageSize }}"
  svcName: "{{ .Values.elastalert.svcName }}"
  storageClass: "{{ .Values.elastalert.storageClass }}"
  cpuRequest: "{{ .Values.elastalert.cpuRequest }}"
  memoryRequest: "{{ .Values.elastalert.memoryRequest }}"
  cpuLimit: "{{ .Values.elastalert.cpuLimit }}"
  memoryLimit: "{{ .Values.elastalert.memoryLimit }}"
  runAsUser: "{{ .Values.elastalert.runAsUser }}"
  runAsGroup: "{{ .Values.elastalert.runAsGroup }}"
  fsGroup: "{{ .Values.elastalert.fsGroup }}"


  {{- if eq .Values.computeProfile "large"}}
  cpuRequest: "{{ .Values.computeProfiles.large.elastalert.cpu }}"
  memoryRequest: "{{ .Values.computeProfiles.large.elastalert.memory }}"
  storageSize: "{{ .Values.computeProfiles.large.storage }}"
  cpuLimit: "{{ .Values.computeProfiles.large.elastalert.cpu }}"
  memoryLimit: "{{ .Values.computeProfiles.large.elastalert.memory }}"
  {{- end }}

  {{- if eq .Values.computeProfile "medium"}}
  cpuRequest: "{{ .Values.computeProfiles.medium.elastalert.cpu }}"
  memoryRequest: "{{ .Values.computeProfiles.medium.elastalert.memory }}"
  storageSize: "{{ .Values.computeProfiles.medium.storage }}"
  cpuLimit: "{{ .Values.computeProfiles.medium.elastalert.cpu }}"
  memoryLimit: "{{ .Values.computeProfiles.medium.elastalert.memory }}"
  {{- end }}

  {{- if eq .Values.computeProfile "small"}}
  cpuRequest: "{{ .Values.computeProfiles.small.elastalert.cpu }}"
  memoryRequest: "{{ .Values.computeProfiles.small.elastalert.memory }}"
  storageSize: "{{ .Values.computeProfiles.small.storage }}"

  {{- end }}
{{- end }}