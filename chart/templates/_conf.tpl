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
  cnvrgStorageUseIamRole: "{{ .Values.appConfigs.cnvrgStorageUseIamRole }}"
  featureFlags: "{{.Values.appConfigs.featureFlags}}"
  smtp:
    server: "{{ .Values.appConfigs.smtp.server }}"
    port: "{{ .Values.appConfigs.smtp.port }}"
    username: "{{ .Values.appConfigs.smtp.username }}"
    password: "{{ .Values.appConfigs.smtp.password }}"
    domain: "{{ .Values.appConfigs.smtp.domain }}"
appSecrets:
  sentryUrl: "{{ .Values.appSecrets.sentryUrl }}"
  secretKeyBase: "{{ .Values.appSecrets.secretKeyBase }}"
  stsIv: "{{ .Values.appSecrets.stsIv }}"
  stsKey: "{{ .Values.appSecrets.stsKey }}"
  passengerAppEnv: "{{ .Values.appSecrets.passengerAppEnv }}"
  railsEnv: "{{ .Values.appSecrets.railsEnv }}"
  runJobsOnSelfCluster: "{{ .Values.appSecrets.runJobsOnSelfCluster }}"
  defaultComputeConfig: "{{ .Values.appSecrets.defaultComputeConfig }}"
  defaultComputeName: "{{ .Values.appSecrets.defaultComputeName }}"
  useStdout: "{{ .Values.appSecrets.useStdout }}"
  extractTagsFromCmd: "{{ .Values.appSecrets.extractTagsFromCmd }}"
  checkJobExpiration: "{{ .Values.appSecrets.checkJobExpiration }}"
  cnvrgStorageType: "{{ .Values.appSecrets.cnvrgStorageType }}"
  {{- if ne .Values.appSecrets.cnvrgStorageEndpoint "default" }}
  cnvrgStorageEndpoint: {{ .Values.appSecrets.cnvrgStorageEndpoint }}
  {{- end}}
  cnvrgStorageBucket: "{{ .Values.appSecrets.cnvrgStorageBucket }}"
  cnvrgStorageAccessKey: "{{ .Values.appSecrets.cnvrgStorageAccessKey }}"
  cnvrgStorageSecretKey: "{{ .Values.appSecrets.cnvrgStorageSecretKey }}"
  minioSseMasterKey: "{{ .Values.appSecrets.minioSseMasterKey }}"
  cnvrgStorageAzureAccessKey: "{{ .Values.appSecrets.cnvrgStorageAzureAccessKey }}"
  cnvrgStorageAzureAccountName: "{{ .Values.appSecrets.cnvrgStorageAzureAccountName }}"
  cnvrgStorageAzureContainer: "{{ .Values.appSecrets.cnvrgStorageAzureContainer }}"
  cnvrgStorageRegion: "{{ .Values.appSecrets.cnvrgStorageRegion }}"
  cnvrgStorageProject: "{{ .Values.appSecrets.cnvrgStorageProject }}"
{{- end }}