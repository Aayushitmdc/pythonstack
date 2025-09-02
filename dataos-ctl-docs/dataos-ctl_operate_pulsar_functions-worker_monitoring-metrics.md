## dataos-ctl operate pulsar functions-worker monitoring-metrics

Dump metrics for Monitoring

### Synopsis

USED FOR:
    Dump metrics for Monitoring

REQUIRED PERMISSION:
    This command requires super-user permissions.

OUTPUT:
    #normal output
    [
      {
        "metrics": {
          "fun_default_pool_allocated": 402653184,
          "fun_default_pool_used": 4734976,
          "jvm_direct_memory_used": 2550137118,
          "jvm_gc_old_count": 0,
          "jvm_gc_old_pause": 0,
          "jvm_gc_young_count": 0,
          "jvm_gc_young_pause": 0,
          "jvm_heap_used": 305348512,
          "jvm_max_direct_memory": 4294967296,
          "jvm_max_memory": 2147483648,
          "jvm_thread_cnt": 446,
          "jvm_total_memory": 2147483648
        },
        "dimensions": {
          "metric": "jvm_metrics"
        }
      }
    ]



```
dataos-ctl operate pulsar functions-worker monitoring-metrics [flags]
```

### Examples

```
    #Dump metrics for Monitoring
    pulsarctl functions-worker monitoring-metrics


```

### Options

```
  -s, --admin-service-url string           The admin web service url that pulsarctl connects to. (default "http://localhost:8080")
      --auth-params string                 Authentication parameters are used to configure the authentication provider specified by "AuthPlugin".
                                            Tls example: "tlsCertFile:val1,tlsKeyFile:val2"
                                            Token example: "authParams=file:///path/to/token/file" or "authParams=token:tokenVal"
      --auth-plugin string                 AuthPlugin is used to specify the plugin to use for authentication,
                                            the supported values are "org.apache.pulsar.client.impl.auth.AuthenticationTls"
                                            and "org.apache.pulsar.client.impl.auth.AuthenticationToken"
      --bookie-service-url string          The bookie web service url that pulsarctl connects to.
  -h, --help                               help for monitoring-metrics
  -o, --output string                      The output format (text,json,yaml) (default "text")
      --tls-allow-insecure                 Allow TLS insecure connection
      --tls-cert-file string               File path for TLS cert used for authentication
      --tls-enable-hostname-verification   Enable TLS hostname verification
      --tls-key-file string                File path for TLS key used for authentication
      --tls-trust-cert-path string         Allow TLS trust cert file path
      --token string                       Using the token to authentication
      --token-file string                  Using the token file to authentication
```

### Options inherited from parent commands

```
  -v, --verbose int   set log level, use 0 to silence, 4 for debugging (default 4)
```

### SEE ALSO

* [dataos-ctl operate pulsar functions-worker](dataos-ctl_operate_pulsar_functions-worker.md)	 - Operations to collect function-worker statistics

