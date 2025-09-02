## dataos-ctl operate pulsar ns-isolation-policy

Operations about namespace isolation policy

```
dataos-ctl operate pulsar ns-isolation-policy [flags]
```

### Options

```
  -h, --help   help for ns-isolation-policy
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
* [dataos-ctl operate pulsar ns-isolation-policy broker](dataos-ctl_operate_pulsar_ns-isolation-policy_broker.md)	 - Get broker with namespace-isolation policies attached to it
* [dataos-ctl operate pulsar ns-isolation-policy brokers](dataos-ctl_operate_pulsar_ns-isolation-policy_brokers.md)	 - List all brokers with namespace-isolation policies attached to it
* [dataos-ctl operate pulsar ns-isolation-policy delete](dataos-ctl_operate_pulsar_ns-isolation-policy_delete.md)	 - Delete namespace isolation policy of a cluster.
* [dataos-ctl operate pulsar ns-isolation-policy get](dataos-ctl_operate_pulsar_ns-isolation-policy_get.md)	 - Get namespace isolation policy of a cluster
* [dataos-ctl operate pulsar ns-isolation-policy list](dataos-ctl_operate_pulsar_ns-isolation-policy_list.md)	 - List all namespace isolation policies of a cluster.
* [dataos-ctl operate pulsar ns-isolation-policy set](dataos-ctl_operate_pulsar_ns-isolation-policy_set.md)	 - Create/Update a namespace isolation policy for a cluster

