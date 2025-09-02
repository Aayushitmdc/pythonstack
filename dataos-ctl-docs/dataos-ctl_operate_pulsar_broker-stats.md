## dataos-ctl operate pulsar broker-stats

Operations to collect broker statistics

```
dataos-ctl operate pulsar broker-stats [flags]
```

### Options

```
  -h, --help   help for broker-stats
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
* [dataos-ctl operate pulsar broker-stats allocator-stats](dataos-ctl_operate_pulsar_broker-stats_allocator-stats.md)	 - Dump the allocator stats
* [dataos-ctl operate pulsar broker-stats load-report](dataos-ctl_operate_pulsar_broker-stats_load-report.md)	 - Dump the broker load-report
* [dataos-ctl operate pulsar broker-stats mbeans](dataos-ctl_operate_pulsar_broker-stats_mbeans.md)	 - Dump the mbean stats
* [dataos-ctl operate pulsar broker-stats monitoring-metrics](dataos-ctl_operate_pulsar_broker-stats_monitoring-metrics.md)	 - Dumps the metrics for Monitoring
* [dataos-ctl operate pulsar broker-stats topics](dataos-ctl_operate_pulsar_broker-stats_topics.md)	 - Dump the topics stats

