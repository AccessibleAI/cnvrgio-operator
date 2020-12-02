{{- define "spec.domainRegister" }}
domainRegister:
  enabled: "{{.Values.domainRegister.enabled}}"
  image: "{{.Values.domainRegister.image}}"
  hostedZoneId: "{{.Values.domainRegister.hostedZoneId}}"
  awsAccessKeyId: "{{.Values.domainRegister.awsAccessKeyId}}"
  awsSecretAccessKey: "{{.Values.domainRegister.awsSecretAccessKey}}"
{{- end }}
