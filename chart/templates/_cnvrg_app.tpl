{{- define "spec.cnvrgApp" }}
cnvrgApp:
  replicas: {{ .Values.cnvrgApp.replicas }}
  edition: "{{ .Values.cnvrgApp.edition }}"
  enabled: "{{ .Values.cnvrgApp.enabled }}"
  fixpg:  "{{ .Values.cnvrgApp.fixpg }}"
  image: "{{ .Values.cnvrgApp.image }}"
  port: "{{ .Values.cnvrgApp.port }}"
  svcName: "{{ .Values.cnvrgApp.svcName }}"
  nodePort: "{{ .Values.cnvrgApp.nodePort }}"
  passengerMaxPoolSize: {{ .Values.cnvrgApp.passengerMaxPoolSize }}
  enableReadinessProbe: "{{.Values.cnvrgApp.enableReadinessProbe}}"
  initialDelaySeconds: "{{ .Values.cnvrgApp.initialDelaySeconds }}"
  readinessPeriodSeconds: "{{ .Values.cnvrgApp.readinessPeriodSeconds }}"
  readinessTimeoutSeconds: "{{ .Values.cnvrgApp.readinessTimeoutSeconds }}"
  failureThreshold: "{{ .Values.cnvrgApp.failureThreshold }}"
  resourcesRequestEnabled: "{{.Values.cnvrgApp.resourcesRequestEnabled}}"
  {{- if eq .Values.computeProfile "large"}}
  cpu: "{{ .Values.computeProfiles.large.cnvrgApp.webappCpu }}"
  memory: "{{ .Values.computeProfiles.large.cnvrgApp.webappMemory }}"
  sidekiqCpu: "{{ .Values.computeProfiles.large.cnvrgApp.sidekiqCpu}}"
  sidekiqMemory: "{{ .Values.computeProfiles.large.cnvrgApp.sidekiqMemory }}"
  sidekiqSearchkickCpu: "{{ .Values.computeProfiles.large.cnvrgApp.searchkiqCpu }}"
  sidekiqSearchkickMemory: "{{ .Values.computeProfiles.large.cnvrgApp.searchkiqMemory }}"
  sidekiqSearchkickReplicas: "{{ .Values.computeProfiles.large.cnvrgApp.searchkiqReplicas }}"
  sidekiqReplicas: "{{ .Values.computeProfiles.large.cnvrgApp.sidekiqReplicas }}"
  {{- end }}

  {{- if eq .Values.computeProfile "medium"}}
  cpu: "{{ .Values.computeProfiles.medium.cnvrgApp.webappCpu }}"
  memory: "{{ .Values.computeProfiles.medium.cnvrgApp.webappMemory }}"
  sidekiqCpu: "{{ .Values.computeProfiles.medium.cnvrgApp.sidekiqCpu}}"
  sidekiqMemory: "{{ .Values.computeProfiles.medium.cnvrgApp.sidekiqMemory }}"
  sidekiqSearchkickCpu: "{{ .Values.computeProfiles.medium.cnvrgApp.searchkiqCpu }}"
  sidekiqSearchkickMemory: "{{ .Values.computeProfiles.medium.cnvrgApp.searchkiqMemory }}"
  sidekiqSearchkickReplicas: "{{ .Values.computeProfiles.medium.cnvrgApp.searchkiqReplicas }}"
  sidekiqReplicas: "{{ .Values.computeProfiles.medium.cnvrgApp.sidekiqReplicas }}"
  {{- end }}

  {{- if eq .Values.computeProfile "small"}}
  cpu: "{{ .Values.computeProfiles.small.cnvrgApp.webappCpu }}"
  memory: "{{ .Values.computeProfiles.small.cnvrgApp.webappMemory }}"
  sidekiqCpu: "{{ .Values.computeProfiles.small.cnvrgApp.sidekiqCpu}}"
  sidekiqMemory: "{{ .Values.computeProfiles.small.cnvrgApp.sidekiqMemory }}"
  sidekiqSearchkickCpu: "{{ .Values.computeProfiles.small.cnvrgApp.searchkiqCpu }}"
  sidekiqSearchkickMemory: "{{ .Values.computeProfiles.small.cnvrgApp.searchkiqMemory }}"
  sidekiqSearchkickReplicas: "{{ .Values.computeProfiles.small.cnvrgApp.searchkiqReplicas }}"
  sidekiqReplicas: "{{ .Values.computeProfiles.small.cnvrgApp.sidekiqReplicas }}"
  {{- end }}
  sidekiqSystemCpu: "{{.Values.cnvrgApp.sidekiqSystemCpu}}"
  sidekiqSystemMemory: "{{.Values.cnvrgApp.sidekiqSystemMemory}}"
  sidekiqSystemReplicas: "{{.Values.cnvrgApp.sidekiqSystemReplicas}}"
  seeder:
    image: "{{ .Values.cnvrgApp.seeder.image }}"
    seedCmd: "{{ .Values.cnvrgApp.seeder.seedCmd }}"
  conf:
    gcpStorageSecret: "{{ .Values.cnvrgApp.conf.gcpStorageSecret }}"
    gcpKeyfileMountPath: "{{ .Values.cnvrgApp.conf.gcpKeyfileMountPath }}"
    gcpKeyfileName: "{{ .Values.cnvrgApp.conf.gcpKeyfileName }}"
    jobsStorageClass: "{{ .Values.cnvrgApp.conf.jobsStorageClass }}"
    cnvrgStorageUseIamRole: "{{ .Values.cnvrgApp.conf.cnvrgStorageUseIamRole }}"
    featureFlags: "{{ .Values.cnvrgApp.conf.featureFlags }}"
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
    cnvrgStorageBucket: "{{ .Values.cnvrgApp.conf.cnvrgStorageBucket }}"
    cnvrgStorageAccessKey: "{{ .Values.cnvrgApp.conf.cnvrgStorageAccessKey }}"
    cnvrgStorageSecretKey: "{{ .Values.cnvrgApp.conf.cnvrgStorageSecretKey }}"
    {{- if ne .Values.cnvrgApp.conf.cnvrgStorageEndpoint "default" }}
    cnvrgStorageEndpoint: {{ .Values.cnvrgApp.conf.cnvrgStorageEndpoint }}
    {{- end}}
    minioSseMasterKey: "{{ .Values.cnvrgApp.conf.minioSseMasterKey }}"
    cnvrgStorageAzureAccessKey: "{{ .Values.cnvrgApp.conf.cnvrgStorageAzureAccessKey }}"
    cnvrgStorageAzureAccountName: "{{ .Values.cnvrgApp.conf.cnvrgStorageAzureAccountName }}"
    cnvrgStorageAzureContainer: "{{ .Values.cnvrgApp.conf.cnvrgStorageAzureContainer }}"
    cnvrgStorageRegion: "{{ .Values.cnvrgApp.conf.cnvrgStorageRegion }}"
    cnvrgStorageProject: "{{ .Values.cnvrgApp.conf.cnvrgStorageProject }}"
    customAgentTag: "{{ .Values.cnvrgApp.conf.customAgentTag }}"
    intercom: "{{ .Values.cnvrgApp.conf.intercom }}"
    splitSidekiq: "{{ .Values.cnvrgApp.conf.splitSidekiq }}"
    registry:
      name: "{{ .Values.cnvrgApp.conf.registry.name}}"
      url: "{{ .Values.cnvrgApp.conf.registry.url}}"
      user: "{{ .Values.cnvrgApp.conf.registry.user}}"
      password: "{{ .Values.cnvrgApp.conf.registry.password}}"
    rbac:
      role: "{{ .Values.cnvrgApp.conf.rbac.role}}"
      serviceAccountName: "{{ .Values.cnvrgApp.conf.rbac.serviceAccountName}}"
      roleBindingName: "{{ .Values.cnvrgApp.conf.rbac.roleBindingName}}"
    smtp:
      server: "{{ .Values.cnvrgApp.conf.smtp.server}}"
      port: "{{ .Values.cnvrgApp.conf.smtp.port}}"
      username: "{{ .Values.cnvrgApp.conf.smtp.username}}"
      password: "{{ .Values.cnvrgApp.conf.smtp.password}}"
      domain: "{{ .Values.cnvrgApp.conf.smtp.domain}}"
  hyper:
    enabled: "{{ .Values.cnvrgApp.hyper.enabled }}"
    image: "{{ .Values.cnvrgApp.hyper.image }}"
    port: "{{ .Values.cnvrgApp.hyper.port }}"
    nodePort: "{{ .Values.cnvrgApp.hyper.nodePort }}"
    svcName: "{{ .Values.cnvrgApp.hyper.svcName }}"
    replicas: "{{ .Values.cnvrgApp.hyper.replicas }}"
    token: "{{.Values.cnvrgApp.hyper.token}}"
    enableReadinessProbe: "{{.Values.cnvrgApp.hyper.enableReadinessProbe}}"
    readinessPeriodSeconds: "{{.Values.cnvrgApp.hyper.readinessPeriodSeconds}}"
    readinessTimeoutSeconds: "{{.Values.cnvrgApp.hyper.readinessTimeoutSeconds}}"

    {{- if eq .Values.computeProfile "large"}}
    cpuRequest: "{{ .Values.computeProfiles.large.hyper.cpu }}"
    memoryRequest: "{{ .Values.computeProfiles.large.hyper.memory }}"
    {{- end }}

    {{- if eq .Values.computeProfile "medium"}}
    cpuRequest: "{{ .Values.computeProfiles.medium.hyper.cpu }}"
    memoryRequest: "{{ .Values.computeProfiles.medium.hyper.memory }}"
    {{- end }}

    {{- if eq .Values.computeProfile "small"}}
    cpuRequest: "{{ .Values.computeProfiles.small.hyper.cpu }}"
    memoryRequest: "{{ .Values.computeProfiles.small.hyper.memory }}"
    {{- end }}
  cnvrgRouter:
    enabled: "{{ .Values.cnvrgApp.cnvrgRouter.enabled }}"
    image: "{{.Values.cnvrgApp.cnvrgRouter.image}}"
    svcName: "{{ .Values.cnvrgApp.cnvrgRouter.svcName }}"
    nodePort: "{{ .Values.cnvrgApp.cnvrgRouter.nodePort }}"
    port: "{{ .Values.cnvrgApp.cnvrgRouter.port}}"

{{- end }}