## dataos-ctl develop observability prometheus

Tcp-stream prometheus and start promlens

### Synopsis

Tcp-stream prometheus and start promlens

```
dataos-ctl develop observability prometheus [flags]
```

### Options

```
      --disablePromLensStart                           Disable starting promlens
      --disablePrometheusTcpStream                     Disable tcp-stream prometheus
  -h, --help                                           help for prometheus
      --localPromLensServiceBaseUrlTemplate string     Local promlens service base url template (default "http://localhost:%d")
      --localPrometheusServiceBaseUrlTemplate string   Local prometheus service base url template (default "http://localhost:%d")
      --promLensImage string                           Promlens image (default "prom/promlens")
      --promLensListenPort int                         Port the local client will listen on to run promlens (default 8080)
      --promListenPort int                             Port the local client will listen on for tcp-stream prometheus (default 9090)
      --prometheusServiceAddress string                Prometheus service address (default "thanos-query-frontend.sentinel.svc.cluster.local:9090")
```

### Options inherited from parent commands

```
      --tls-allow-insecure   Allow insecure TLS connections
```

### SEE ALSO

* [dataos-ctl develop observability](dataos-ctl_develop_observability.md)	 - Develop observability resources

