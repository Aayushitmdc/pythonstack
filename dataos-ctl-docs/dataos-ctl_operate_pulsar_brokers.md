## dataos-ctl operate pulsar brokers

Operations about broker(s)

```
dataos-ctl operate pulsar brokers [flags]
```

### Options

```
  -h, --help   help for brokers
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
* [dataos-ctl operate pulsar brokers delete-dynamic-config](dataos-ctl_operate_pulsar_brokers_delete-dynamic-config.md)	 - Delete dynamic-serviceConfiguration of broker
* [dataos-ctl operate pulsar brokers get-all-dynamic-config](dataos-ctl_operate_pulsar_brokers_get-all-dynamic-config.md)	 - Get all overridden dynamic-configuration values
* [dataos-ctl operate pulsar brokers get-internal-config](dataos-ctl_operate_pulsar_brokers_get-internal-config.md)	 - Get internal configuration information
* [dataos-ctl operate pulsar brokers get-runtime-config](dataos-ctl_operate_pulsar_brokers_get-runtime-config.md)	 - Get runtime configuration values
* [dataos-ctl operate pulsar brokers healthcheck](dataos-ctl_operate_pulsar_brokers_healthcheck.md)	 - Run a health check against the broker
* [dataos-ctl operate pulsar brokers list](dataos-ctl_operate_pulsar_brokers_list.md)	 - List active brokers of the cluster
* [dataos-ctl operate pulsar brokers list-dynamic-config](dataos-ctl_operate_pulsar_brokers_list-dynamic-config.md)	 - Get all overridden dynamic-configuration values
* [dataos-ctl operate pulsar brokers namespaces](dataos-ctl_operate_pulsar_brokers_namespaces.md)	 - List namespaces owned by the broker
* [dataos-ctl operate pulsar brokers update-dynamic-config](dataos-ctl_operate_pulsar_brokers_update-dynamic-config.md)	 - Update dynamic-serviceConfiguration of broker

