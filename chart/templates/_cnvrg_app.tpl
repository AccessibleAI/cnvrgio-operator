{{- define "spec.cnvrgApp" }}
cnvrgApp:
  replicas: {{ .Values.cnvrgApp.replicas }}
  edition: "{{ .Values.cnvrgApp.edition }}"
  enabled: "{{ .Values.cnvrgApp.enabled }}"
  fixpg:  "{{ .Values.cnvrgApp.fixpg }}"
  image: "{{ .Values.cnvrgApp.image }}"
  port: "{{ .Values.cnvrgApp.port }}"
  svcName: "{{ .Values.cnvrgApp.svcName }}"
  customAgentTag: "{{ .Values.cnvrgApp.customAgentTag }}"
  intercom: "{{ .Values.cnvrgApp.intercom }}"
  nodePort: "{{ .Values.cnvrgApp.nodePort }}"
  passengerMaxPoolSize: {{ .Values.cnvrgApp.passengerMaxPoolSize }}
  enableReadinessProbe: "{{.Values.cnvrgApp.enableReadinessProbe}}"
  readinessPeriodSeconds: "{{.Values.cnvrgApp.readinessPeriodSeconds}}"
  readinessTimeoutSeconds: "{{.Values.cnvrgApp.readinessTimeoutSeconds}}"

  {{- if eq .Values.computeProfile "large"}}
  cpu: "{{ .Values.computeProfiles.large.cnvrgApp.webappCpu }}"
  memory: "{{ .Values.computeProfiles.large.cnvrgApp.webappMemory }}"
  sidekiqCpu: "{{ .Values.computeProfiles.large.cnvrgApp.sidekiqCpu}}"
  sidekiqMemory: "{{ .Values.computeProfiles.large.cnvrgApp.sidekiqMemory }}"
  sidekiqSearchkickCpu: "{{ .Values.computeProfiles.large.cnvrgApp.searchkiqCpu }}"
  sidekiqSearchkickMemory: "{{ .Values.computeProfiles.large.cnvrgApp.searchkiqMemory }}"
  sidekiqSearchkickReplicas: "{{ .Values.computeProfiles.large.cnvrgApp.sidekiqReplicas }}"
  sidekiqReplicas: "{{ .Values.computeProfiles.large.cnvrgApp.searchkiqReplicas }}"
  {{- end }}

  {{- if eq .Values.computeProfile "medium"}}
  cpu: "{{ .Values.computeProfiles.medium.cnvrgApp.webappCpu }}"
  memory: "{{ .Values.computeProfiles.medium.cnvrgApp.webappMemory }}"
  sidekiqCpu: "{{ .Values.computeProfiles.medium.cnvrgApp.sidekiqCpu}}"
  sidekiqMemory: "{{ .Values.computeProfiles.medium.cnvrgApp.sidekiqMemory }}"
  sidekiqSearchkickCpu: "{{ .Values.computeProfiles.medium.cnvrgApp.searchkiqCpu }}"
  sidekiqSearchkickMemory: "{{ .Values.computeProfiles.medium.cnvrgApp.searchkiqMemory }}"
  sidekiqSearchkickReplicas: "{{ .Values.computeProfiles.medium.cnvrgApp.sidekiqReplicas }}"
  sidekiqReplicas: "{{ .Values.computeProfiles.medium.cnvrgApp.searchkiqReplicas }}"
  {{- end }}

  {{- if eq .Values.computeProfile "small"}}
  cpu: "{{ .Values.computeProfiles.small.cnvrgApp.webappCpu }}"
  memory: "{{ .Values.computeProfiles.small.cnvrgApp.webappMemory }}"
  sidekiqCpu: "{{ .Values.computeProfiles.small.cnvrgApp.sidekiqCpu}}"
  sidekiqMemory: "{{ .Values.computeProfiles.small.cnvrgApp.sidekiqMemory }}"
  sidekiqSearchkickCpu: "{{ .Values.computeProfiles.small.cnvrgApp.searchkiqCpu }}"
  sidekiqSearchkickMemory: "{{ .Values.computeProfiles.small.cnvrgApp.searchkiqMemory }}"
  sidekiqSearchkickReplicas: "{{ .Values.computeProfiles.small.cnvrgApp.sidekiqReplicas }}"
  sidekiqReplicas: "{{ .Values.computeProfiles.small.cnvrgApp.searchkiqReplicas }}"
  {{- end }}
seeder:
  image: "{{ .Values.seeder.image }}"
  seedCmd: "{{ .Values.seeder.seedCmd }}"
{{- end }}