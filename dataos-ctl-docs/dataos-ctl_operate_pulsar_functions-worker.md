## dataos-ctl operate pulsar functions-worker

Operations to collect function-worker statistics

```
dataos-ctl operate pulsar functions-worker [flags]
```

### Options

```
  -h, --help   help for functions-worker
```

### Options inherited from parent commands

```
  -s, --admin-service-url string           The admin web service url that pulsarctl connects to. (default "http://localhost:8080")
      --auth-params string                 Authentication parameters are used to configure the authentication provider specified by "AuthPlugin".
                                            Tls example: "tlsCertFile:val1,tlsKeyFile:val2"
                                            Token example: "authParams=file:///path/to/token/file" or "authParams=token:tokenVal"
      --auth-plugin string                 AuthPlugin is used to specify the plugin to use for authentication,
                                            the supported values are "org.apache.pulsar.client.impl.auth.AuthenticationTls"
                                            and "org.apache.pulsar.client.impl.auth.AuthenticationToken"
      --bookie-service-url string          The bookie web service url that pulsarctl connects to.
      --tls-allow-insecure                 Allow TLS insecure connection
      --tls-cert-file string               File path for TLS cert used for authentication
      --tls-enable-hostname-verification   Enable TLS hostname verification
      --tls-key-file string                File path for TLS key used for authentication
      --tls-trust-cert-path string         Allow TLS trust cert file path
      --token string                       Using the token to authentication
      --token-file string                  Using the token file to authentication
  -v, --verbose int                        set log level, use 0 to silence, 4 for debugging (default 4)
```

### SEE ALSO

* [dataos-ctl operate pulsar](dataos-ctl_operate_pulsar.md)	 - Pulsar management
* [dataos-ctl operate pulsar functions-worker function-stats](dataos-ctl_operate_pulsar_functions-worker_function-stats.md)	 - Dump all functions stats running on this broker
* [dataos-ctl operate pulsar functions-worker get-cluster](dataos-ctl_operate_pulsar_functions-worker_get-cluster.md)	 - Get all workers belonging to this cluster
* [dataos-ctl operate pulsar functions-worker get-cluster-leader](dataos-ctl_operate_pulsar_functions-worker_get-cluster-leader.md)	 - Get the leader of the worker cluster
* [dataos-ctl operate pulsar functions-worker get-function-assignments](dataos-ctl_operate_pulsar_functions-worker_get-function-assignments.md)	 - Get the assignments of the functions across the worker cluster
* [dataos-ctl operate pulsar functions-worker monitoring-metrics](dataos-ctl_operate_pulsar_functions-worker_monitoring-metrics.md)	 - Dump metrics for Monitoring

