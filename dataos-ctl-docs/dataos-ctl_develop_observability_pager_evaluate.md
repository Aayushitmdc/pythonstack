## dataos-ctl develop observability pager evaluate

Evaluate an incident against a pager

### Synopsis

Evaluate an incident against a pager's conditions'

```
dataos-ctl develop observability pager evaluate [flags]
```

### Options

```
      --disable-interpolation                     Disable interpolation, do not interpolate $ENV|${ENV}
      --disablePagerTcpStream                     Disable tcp-stream pager
  -h, --help                                      help for evaluate
  -i, --incidentId string                         Incident id to use for develop activities
      --incidentJsonFile string                   Incident json file
      --listenPort int                            Port the local client will listen on to tcp stream (default 32017)
      --localPagerServiceBaseUrlTemplate string   Local pager service base url template (default "https://localhost:%d/observability/api/v1")
  -f, --manifestFile string                       Manifest file location for the pager resource
      --pagerServiceAddress string                Pager service address (default "pager-api.observability.svc.cluster.local:32017")
```

### Options inherited from parent commands

```
      --tls-allow-insecure   Allow insecure TLS connections
```

### SEE ALSO

* [dataos-ctl develop observability pager](dataos-ctl_develop_observability_pager.md)	 - Develop observability pager resources

