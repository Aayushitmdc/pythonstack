## dataos-ctl develop observability monitor equation

Run a monitor equation

### Synopsis

Run a monitor equation to validate and get the results

```
dataos-ctl develop observability monitor equation [flags]
```

### Options

```
      --disable-interpolation                       Disable interpolation, do not interpolate $ENV|${ENV}
  -d, --displayType string                          The way to display the results table|list (default "table")
  -h, --help                                        help for equation
      --listenPort int                              Port the local client will listen on to tcp stream (default 32017)
      --localMonitorServiceBaseUrlTemplate string   Local monitor service base url template (default "https://localhost:%d/observability/api/v1")
  -f, --manifestFile string                         Manifest file location for the monitor resource
      --maxRows int                                 Max query expression rows to display (default 10)
      --monitorServiceAddress string                Monitor service address (default "monitor-api.observability.svc.cluster.local:32017")
```

### Options inherited from parent commands

```
      --tls-allow-insecure   Allow insecure TLS connections
```

### SEE ALSO

* [dataos-ctl develop observability monitor](dataos-ctl_develop_observability_monitor.md)	 - Develop observability monitor resources
* [dataos-ctl develop observability monitor equation query](dataos-ctl_develop_observability_monitor_equation_query.md)	 - Run a monitor equation query

