{{- define "spec.microk8s"  }}
clusterDomain: "{{ .Values.clusterDomain }}"
ingressType: "{{.Values.specProfiles.microk8s.ingress}}"
redis:
  limits:
    cpu: "{{ .Values.computeProfiles.micro.redis.cpu }}"
    memory: "{{ .Values.computeProfiles.micro.redis.memory }}"
  requests:
    cpu: "{{ .Values.computeProfiles.micro.redis.cpu }}"
    memory: "{{ .Values.computeProfiles.micro.redis.memory }}"
pg:
  enabled: "{{ .Values.pg.enabled }}"
  image: "{{ .Values.pg.image }}"
  port: "{{ .Values.pg.port }}"
  storageSize: "{{ .Values.storageProfiles.micro.pg }}"
  dbname: "{{ .Values.pg.dbname }}"
  pass: "{{ .Values.pg.pass }}"
  user: "{{ .Values.pg.user }}"
  runAsUser: "{{ .Values.pg.runAsUser }}"
  runAsGroup: "{{ .Values.pg.runAsGroup }}"
  fsGroup: "{{ .Values.pg.fsGroup }}"
  storageClass: "{{ .Values.pg.storageClass }}"
  cpuRequest: "{{.Values.computeProfiles.micro.pg.cpu}}"
  memoryRequest: "{{.Values.computeProfiles.micro.pg.memory}}"
  svcName: "{{ .Values.pg.svcName }}"
minio:
  enabled: "{{ .Values.minio.enabled }}"
  image: "{{ .Values.minio.image }}"
  port: "{{ .Values.minio.port }}"
  storageSize: "{{ .Values.storageProfiles.micro.minio }}"
  svcName: "{{ .Values.minio.svcName }}"
  nodePort: "{{ .Values.minio.nodePort }}"
  storageClass: "{{ .Values.minio.storageClass }}"
  memoryRequest: "{{ .Values.computeProfiles.micro.minio.memory }}"
  sharedStorage:
    enabled: "{{ .Values.minio.sharedStorage.enabled }}"
    storageClassName: "{{ .Values.minio.sharedStorage.storageClassName }}"
    nfsServer: "{{ .Values.minio.sharedStorage.nfsServer }}"
    path: "{{ .Values.minio.sharedStorage.path }}"
  replicas: "{{ .Values.minio.replicas }}"
cnvrgApp:
  replicas: 1
  sidekiqReplicas: 1
  edition: "core"
  image: "cnvrg/core:coreoc"
  customAgentTag: "coreoc"
  cpu: "{{ .Values.computeProfiles.micro.app.cpu }}"
  memory: "{{ .Values.computeProfiles.micro.app.memory }}"
  sidekiqCpu: "{{ .Values.computeProfiles.micro.sidekiq.cpu }}"
  sidekiqMemory: "{{ .Values.computeProfiles.micro.sidekiq.memory }}"

seeder:
  image: "{{ .Values.seeder.image }}"
  seedCmd: "{{ .Values.seeder.seedCmd }}"

hostpath:
  enabled: "true"
  hostPath: "{{ .Values.hostpath.hostPath }}"
  nodeName: "{{ .Values.hostpath.nodeName }}"

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
  cnvrgStorageBucket: "{{ .Values.appSecrets.cnvrgStorageBucket }}"
  cnvrgStorageAccessKey: "{{ .Values.appSecrets.cnvrgStorageAccessKey }}"
  cnvrgStorageSecretKey: "{{ .Values.appSecrets.cnvrgStorageSecretKey }}"
  minioSseMasterKey: "{{ .Values.appSecrets.minioSseMasterKey }}"
  cnvrgStorageAzureAccessKey: "{{ .Values.appSecrets.cnvrgStorageAzureAccessKey }}"
  cnvrgStorageAzureAccountName: "{{ .Values.appSecrets.cnvrgStorageAzureAccountName }}"
  cnvrgStorageAzureContainer: "{{ .Values.appSecrets.cnvrgStorageAzureContainer }}"
  cnvrgStorageRegion: "{{ .Values.appSecrets.cnvrgStorageRegion }}"
  cnvrgStorageProject: "{{ .Values.appSecrets.cnvrgStorageProject }}"


es:
  enabled: "false"

prometheus:
  enabled: "false"

istio:
  enabled: "false"

kibana:
  enabled: "false"

fluentd:
  enabled: "false"

nvidiadp:
  enabled: "true"

mpi:
  enabled: "false"

nfs:
  enabled: "false"

{{- end}}

{{- define "spec.default"  }}
debug: "{{ .Values.debug }}"
dumpDir: "{{ .Values.dumpDir }}"
dryRun: "{{ .Values.dryRun }}"
privilegedSa: "{{ .Values.privilegedSa }}"
clusterDomain: "{{ .Values.clusterDomain }}"
useHttps: "{{ .Values.useHttps }}"
orchestrator: "{{ .Values.orchestrator }}"
securityMode: "{{ .Values.securityMode }}"
ingressType: "{{ .Values.ingressType }}"
https:
  enabled: "{{ .Values.https.enabled }}"
  useWildcardCertificate: "{{ .Values.https.useWildcardCertificate }}"
  cert: "{{ .Values.https.cert }}"
  key: "{{ .Values.https.key }}"
conf:
  enabled: "{{ .Values.conf.enabled }}"
  gcpStorageSecret: "{{ .Values.conf.gcpStorageSecret }}"
  gcpKeyfileMountPath: "{{ .Values.conf.gcpKeyfileMountPath }}"
  gcpKeyfileName: "{{ .Values.conf.gcpKeyfileName }}"
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
  cnvrgStorageBucket: "{{ .Values.appSecrets.cnvrgStorageBucket }}"
  cnvrgStorageAccessKey: "{{ .Values.appSecrets.cnvrgStorageAccessKey }}"
  cnvrgStorageSecretKey: "{{ .Values.appSecrets.cnvrgStorageSecretKey }}"
  minioSseMasterKey: "{{ .Values.appSecrets.minioSseMasterKey }}"
  cnvrgStorageAzureAccessKey: "{{ .Values.appSecrets.cnvrgStorageAzureAccessKey }}"
  cnvrgStorageAzureAccountName: "{{ .Values.appSecrets.cnvrgStorageAzureAccountName }}"
  cnvrgStorageAzureContainer: "{{ .Values.appSecrets.cnvrgStorageAzureContainer }}"
  cnvrgStorageRegion: "{{ .Values.appSecrets.cnvrgStorageRegion }}"
  cnvrgStorageProject: "{{ .Values.appSecrets.cnvrgStorageProject }}"
redis:
  enabled: "{{ .Values.redis.enabled }}"
  image: "{{ .Values.redis.image }}"
  {{- if eq .Values.computeProfile "default" }}
  limits:
    cpu: "{{ .Values.redis.limits.cpu }}"
    memory: "{{ .Values.redis.limits.memory }}"
  requests:
    cpu: "{{ .Values.redis.requests.cpu }}"
    memory: "{{ .Values.redis.requests.memory }}"
  {{- end }}
  {{- if eq .Values.computeProfile "micro" }}
  limits:
    cpu: "{{ .Values.computeProfiles.micro.redis.cpu }}"
    memory: "{{ .Values.computeProfiles.micro.redis.memory }}"
  requests:
    cpu: "{{ .Values.computeProfiles.micro.redis.cpu }}"
    memory: "{{ .Values.computeProfiles.micro.redis.memory }}"
  {{- end }}
  svcName: "{{ .Values.redis.svcName }}"
  port: "{{ .Values.redis.port }}"

pg:
  enabled: "{{ .Values.pg.enabled }}"
  image: "{{ .Values.pg.image }}"
  port: "{{ .Values.pg.port }}"
  {{- if eq .Values.storageProfile "default"}}
  storageSize: "{{ .Values.pg.storageSize }}"
  {{- end }}
  {{- if eq .Values.storageProfile "micro"}}
  storageSize: "{{ .Values.storageProfiles.micro.pg }}"
  {{- end }}
  dbname: "{{ .Values.pg.dbname }}"
  pass: "{{ .Values.pg.pass }}"
  user: "{{ .Values.pg.user }}"
  runAsUser: "{{ .Values.pg.runAsUser }}"
  runAsGroup: "{{ .Values.pg.runAsGroup }}"
  fsGroup: "{{ .Values.pg.fsGroup }}"
  storageClass: "{{ .Values.pg.storageClass }}"
  {{- if eq .Values.computeProfile "default"}}
  cpuRequest: "{{ .Values.pg.cpuRequest }}"
  memoryRequest: "{{ .Values.pg.memoryRequest }}"
  {{- end }}
  {{- if eq .Values.computeProfile "micro"}}
  cpuRequest: "{{.Values.computeProfiles.micro.pg.cpu}}"
  memoryRequest: "{{.Values.computeProfiles.micro.pg.memory}}"
  {{- end }}
  svcName: "{{ .Values.pg.svcName }}"

es:
  enabled: "{{ .Values.es.enabled }}"
  image: "{{ .Values.es.image }}"
  maxMapImage: "{{.Values.es.maxMapImage}}"
  port: "{{ .Values.es.port }}"
  {{- if eq .Values.storageProfile "default"}}
  storageSize: "{{ .Values.es.storageSize }}"
  {{- end }}
  {{- if eq .Values.storageProfile "micro"}}
  storageSize: "{{ .Values.storageProfiles.micro.pg }}"
  {{- end }}
  svcName: "{{ .Values.es.svcName }}"
  runAsUser: "{{ .Values.es.runAsUser }}"
  runAsGroup: "{{ .Values.es.runAsGroup }}"
  fsGroup: "{{ .Values.es.fsGroup }}"
  patchEsNodes: "{{ .Values.es.patchEsNodes }}"
  nodePort: "{{ .Values.es.nodePort }}"
  storageClass: "{{ .Values.es.storageClass }}"

  {{- if eq .Values.computeProfile "default"}}
  cpuRequest: "{{ .Values.es.cpuRequest }}"
  memoryRequest: "{{ .Values.es.memoryRequest }}"
  cpuLimit: "{{ .Values.es.cpuLimit }}"
  memoryLimit: "{{ .Values.es.memoryLimit }}"
  {{- end }}
  {{- if eq .Values.computeProfile "micro"}}
  cpuRequest: "{{ .Values.computeProfiles.micro.es.cpuRequest }}"
  memoryRequest: "{{ .Values.computeProfiles.micro.es.memoryRequest }}"
  {{- end }}
  javaOpts: "{{ .Values.es.javaOpts }}"

minio:
  enabled: "{{ .Values.minio.enabled }}"
  image: "{{ .Values.minio.image }}"
  port: "{{ .Values.minio.port }}"
  {{- if  eq .Values.storageProfile "default"}}
  storageSize: "{{ .Values.minio.storageSize }}"
  {{- end }}
  {{- if  eq .Values.storageProfile "micro"}}
  storageSize: "{{ .Values.storageProfiles.micro.minio }}"
  {{- end }}
  svcName: "{{ .Values.minio.svcName }}"
  nodePort: "{{ .Values.minio.nodePort }}"
  storageClass: "{{ .Values.minio.storageClass }}"
  {{- if eq .Values.computeProfile "default"}}
  memoryRequest: "{{ .Values.minio.memoryRequest }}"
  {{- end }}
  {{- if eq .Values.computeProfile "micro"}}
  memoryRequest: "{{ .Values.computeProfiles.micro.minio.memory }}"
  {{- end }}
  sharedStorage:
    enabled: "{{ .Values.minio.sharedStorage.enabled }}"
    storageClassName: "{{ .Values.minio.sharedStorage.storageClassName }}"
    nfsServer: "{{ .Values.minio.sharedStorage.nfsServer }}"
    path: "{{ .Values.minio.sharedStorage.path }}"
  replicas: "{{ .Values.minio.replicas }}"

prometheus:
  enabled: "{{ .Values.prometheus.enabled }}"
  image: "{{ .Values.prometheus.image }}"
  operatorImage: "{{ .Values.prometheus.operatorImage }}"
  configReloaderImage: "{{ .Values.prometheus.configReloaderImage }}"
  prometheusConfigReloaderImage: "{{ .Values.prometheus.prometheusConfigReloaderImage }}"
  kubeRbacProxyImage: "{{ .Values.prometheus.kubeRbacProxyImage }}"
  kubeStateMetricsImage: "{{ .Values.prometheus.kubeStateMetricsImage }}"
  alertManagerImage: "{{ .Values.prometheus.alertManagerImage }}"
  adapterImage: "{{ .Values.prometheus.adapterImage }}"
  nvidiaExporterImage: "{{ .Values.prometheus.nvidiaExporterImage }}"
  nodeExporterImage: "{{ .Values.prometheus.nodeExporterImage }}"
  svcName: "{{ .Values.prometheus.svcName }}"
  port: "{{ .Values.prometheus.port }}"
  nodePort: "{{ .Values.prometheus.nodePort }}"
  {{- if eq .Values.storageProfile "default"}}
  storageSize: "{{ .Values.prometheus.storageSize }}"
  {{- end }}
  {{- if eq .Values.storageProfile "micro"}}
  storageSize: "{{ .Values.storageProfiles.micro.prometheus }}"
  {{- end }}
  storageClass: "{{ .Values.prometheus.storageClass }}"
  kubeletMetrics:
    schema: "{{ .Values.prometheus.kubeletMetrics.schema }}"
    port: "{{ .Values.prometheus.kubeletMetrics.port }}"

grafana:
  svcName: "{{ .Values.grafana.svcName }}"
  port: "{{ .Values.grafana.port }}"
  image: "{{ .Values.grafana.image }}"
  nodePort: "{{ .Values.grafana.nodePort }}"

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

kibana:
  enabled: "{{ .Values.kibana.enabled }}"
  svcName: "{{ .Values.kibana.svcName }}"
  image: "{{ .Values.kibana.image }}"
  nodePort: "{{ .Values.kibana.nodePort }}"
  {{- if eq .Values.computeProfile "default"}}
  cpuRequest: "{{ .Values.kibana.cpuRequest }}"
  memoryRequest: "{{ .Values.kibana.memoryRequest }}"
  cpuLimit: "{{ .Values.kibana.cpuLimit }}"
  memoryLimit: "{{ .Values.kibana.memoryLimit }}"
  {{- end }}
  {{- if eq .Values.computeProfile "micro"}}
  cpuRequest: "{{ .Values.computeProfiles.micro.kibana.cpu }}"
  memoryRequest: "{{ .Values.computeProfiles.micro.kibana.memory }}"
  cpuLimit: "{{ .Values.computeProfiles.micro.kibana.cpu }}"
  memoryLimit: "{{ .Values.computeProfiles.micro.kibana.memory }}"
  {{- end }}
  port: "{{ .Values.kibana.port }}"

fluentd:
  enabled: "{{ .Values.fluentd.enabled }}"
  image: "{{.Values.fluentd.image}}"
  journalPath: "{{ .Values.fluentd.journalPath }}"
  containersPath: "{{ .Values.fluentd.containersPath }}"
  journald: "{{ .Values.fluentd.journald }}"
  cpuRequest: "{{ .Values.fluentd.cpuRequest }}"
  memoryRequest: "{{ .Values.fluentd.memoryRequest }}"
  memoryLimit: "{{ .Values.fluentd.memoryLimit }}"

nvidiadp:
  enabled: "{{ .Values.nvidiadp.enabled }}"
  image: "{{ .Values.nvidiadp.image }}"
  nodeSelector:
    enabled: "{{ .Values.nvidiadp.nodeSelector.enabled }}"
    key: "{{ .Values.nvidiadp.nodeSelector.key }}"
    value: "{{ .Values.nvidiadp.nodeSelector.value }}"

mpi:
  enabled: "{{ .Values.mpi.enabled }}"

cnvrgApp:
  replicas: {{ .Values.cnvrgApp.replicas }}
  sidekiqReplicas: {{ .Values.cnvrgApp.sidekiqReplicas }}
  edition: "{{ .Values.cnvrgApp.edition }}"
  enabled: "{{ .Values.cnvrgApp.enabled }}"
  image: "{{ .Values.cnvrgApp.image }}"
  port: "{{ .Values.cnvrgApp.port }}"
  {{- if eq .Values.computeProfile "default"}}
  cpu: "{{ .Values.cnvrgApp.cpu }}"
  memory: "{{ .Values.cnvrgApp.memory }}"
  sidekiqCpu: "{{ .Values.cnvrgApp.sidekiqCpu }}"
  sidekiqMemory: "{{ .Values.cnvrgApp.sidekiqMemory }}"
  {{- end }}
  {{- if eq .Values.computeProfile "micro"}}
  cpu: "{{ .Values.computeProfiles.micro.app.cpu }}"
  memory: "{{ .Values.computeProfiles.micro.app.memory }}"
  sidekiqCpu: "{{ .Values.computeProfiles.micro.sidekiq.cpu }}"
  sidekiqMemory: "{{ .Values.computeProfiles.micro.sidekiq.memory }}"
  {{- end }}
  svcName: "{{ .Values.cnvrgApp.svcName }}"
  customAgentTag: "{{ .Values.cnvrgApp.customAgentTag }}"
  intercom: "{{ .Values.cnvrgApp.intercom }}"
  nodePort: "{{ .Values.cnvrgApp.nodePort }}"

seeder:
  image: "{{ .Values.seeder.image }}"
  seedCmd: "{{ .Values.seeder.seedCmd }}"

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

autoscaler:
  enabled: "{{ .Values.autoscaler.enabled }}"

ingress:
  enabled: "{{ .Values.ingress.enabled }}"

cnvrgRouter:
  enabled: "{{ .Values.cnvrgRouter.enabled }}"
  image: "{{.Values.cnvrgRouter.image}}"
  svcName: "{{ .Values.cnvrgRouter.svcName }}"
  nodePort: "{{ .Values.cnvrgRouter.nodePort }}"
  port: "{{ .Values.cnvrgRouter.port}}"
{{- end}}