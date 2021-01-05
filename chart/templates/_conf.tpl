{{- define "spec.conf" }}
conf:
  enabled: "{{ .Values.conf.enabled }}"
  gcpStorageSecret: "{{ .Values.conf.gcpStorageSecret }}"
  gcpKeyfileMountPath: "{{ .Values.conf.gcpKeyfileMountPath }}"
  gcpKeyfileName: "{{ .Values.conf.gcpKeyfileName }}"
  defaultJobsStorageClass: "{{ .Values.conf.defaultJobsStorageClass}}"
registry:
  name: "{{ .Values.registry.name }}"
  url: "{{ .Values.registry.url }}"
  user: "{{ .Values.registry.user }}"
  password: "{{ .Values.registry.password }}"
rbac:
  role: "{{ .Values.rbac.role }}"
  serviceAccountName: "{{ .Values.rbac.serviceAccountName }}"
  roleBindingName: "{{ .Values.rbac.roleBindingName }}"
appConfigs:
  cnvrgStorageUseIamRole: "{{ .Values.cnvrgApp.conf.cnvrgStorageUseIamRole }}"
  featureFlags: "{{.Values.cnvrgApp.conf.featureFlags}}"
  smtp:
    server: "{{ .Values.cnvrgApp.conf.smtp.server }}"
    port: "{{ .Values.cnvrgApp.conf.smtp.port }}"
    username: "{{ .Values.cnvrgApp.conf.smtp.username }}"
    password: "{{ .Values.cnvrgApp.conf.smtp.password }}"
    domain: "{{ .Values.cnvrgApp.conf.smtp.domain }}"
appSecrets:
  sentryUrl: "{{ .Values.cnvrgApp.conf.sentryUrl }}"
  secretKeyBase: "{{ .Values.cnvrgApp.conf.secretKeyBase }}"
  stsIv: "{{ .Values.cnvrgApp.conf.stsIv }}"
  stsKey: "{{ .Values.cnvrgApp.conf.stsKey }}"
  passengerAppEnv: "{{ .Values.cnvrgApp.conf.passengerAppEnv }}"
  railsEnv: "{{ .Values.cnvrgApp.conf.railsEnv }}"
  runJobsOnSelfCluster: "{{ .Values.cnvrgApp.conf.runJobsOnSelfCluster }}"
  defaultComputeConfig: "{{ .Values.cnvrgApp.conf.defaultComputeConfig }}"
  defaultComputeName: "{{ .Values.cnvrgApp.conf.defaultComputeName }}"
  useStdout: "{{ .Values.cnvrgApp.conf.useStdout }}"
  extractTagsFromCmd: "{{ .Values.cnvrgApp.conf.extractTagsFromCmd }}"
  checkJobExpiration: "{{ .Values.cnvrgApp.conf.checkJobExpiration }}"
  cnvrgStorageType: "{{ .Values.cnvrgApp.conf.cnvrgStorageType }}"
  {{- if ne .Values.cnvrgApp.conf.cnvrgStorageEndpoint "default" }}
  cnvrgStorageEndpoint: {{ .Values.cnvrgApp.conf.cnvrgStorageEndpoint }}
  {{- end}}
  cnvrgStorageBucket: "{{ .Values.cnvrgApp.conf.cnvrgStorageBucket }}"
  cnvrgStorageAccessKey: "{{ .Values.cnvrgApp.conf.cnvrgStorageAccessKey }}"
  cnvrgStorageSecretKey: "{{ .Values.cnvrgApp.conf.cnvrgStorageSecretKey }}"
  minioSseMasterKey: "{{ .Values.cnvrgApp.conf.minioSseMasterKey }}"
  cnvrgStorageAzureAccessKey: "{{ .Values.cnvrgApp.conf.cnvrgStorageAzureAccessKey }}"
  cnvrgStorageAzureAccountName: "{{ .Values.cnvrgApp.conf.cnvrgStorageAzureAccountName }}"
  cnvrgStorageAzureContainer: "{{ .Values.cnvrgApp.conf.cnvrgStorageAzureContainer }}"
  cnvrgStorageRegion: "{{ .Values.cnvrgApp.conf.cnvrgStorageRegion }}"
  cnvrgStorageProject: "{{ .Values.cnvrgApp.conf.cnvrgStorageProject }}"
{{- end }}