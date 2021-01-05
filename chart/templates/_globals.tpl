{{- define "spec.globals"  }}
debug: "{{ .Values.debug }}"
dumpDir: "{{ .Values.dumpDir }}"
dryRun: "{{ .Values.dryRun }}"
clusterDomain: "{{ .Values.clusterDomain }}"
orchestrator: "{{ .Values.orchestrator }}"
securityMode: "{{ .Values.securityMode }}"
{{- end }}
