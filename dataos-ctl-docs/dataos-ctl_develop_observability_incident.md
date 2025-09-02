## dataos-ctl develop observability incident

Get an incident

### Synopsis

Try and retrieve an incident by id

```
dataos-ctl develop observability incident [flags]
```

### Options

```
  -h, --help                                        help for incident
  -i, --incidentId string                           Incident id
      --listenPort int                              Port the local client will listen on to tcp stream (default 32017)
      --localMonitorServiceBaseUrlTemplate string   Local monitor service base url template (default "https://localhost:%d/observability/api/v1")
      --monitorServiceAddress string                Monitor service address (default "monitor-api.observability.svc.cluster.local:32017")
```

### Options inherited from parent commands

```
      --tls-allow-insecure   Allow insecure TLS connections
```

### SEE ALSO

* [dataos-ctl develop observability](dataos-ctl_develop_observability.md)	 - Develop observability resources

