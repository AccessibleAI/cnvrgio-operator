{{- define "spec.globals"  }}
debug: "{{ .Values.debug }}"
dumpDir: "{{ .Values.dumpDir }}"
dryRun: "{{ .Values.dryRun }}"
privilegedSa: "{{ .Values.privilegedSa }}"
clusterDomain: "{{ .Values.clusterDomain }}"
useHttps: "{{ .Values.useHttps }}"
orchestrator: "{{ .Values.orchestrator }}"
securityMode: "{{ .Values.securityMode }}"
networking.ingressType: "{{ .Values.networking.ingressType }}"
{{- end }}
