## dataos-ctl operate pulsar

Pulsar management

### Synopsis

Pulsar management on the DataOS®

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
  -h, --help                               help for pulsar
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

* [dataos-ctl operate](dataos-ctl_operate.md)	 - Operate the DataOS®
* [dataos-ctl operate pulsar bookkeeper](dataos-ctl_operate_pulsar_bookkeeper.md)	 - Operations about bookKeeper
* [dataos-ctl operate pulsar broker-stats](dataos-ctl_operate_pulsar_broker-stats.md)	 - Operations to collect broker statistics
* [dataos-ctl operate pulsar brokers](dataos-ctl_operate_pulsar_brokers.md)	 - Operations about broker(s)
* [dataos-ctl operate pulsar clusters](dataos-ctl_operate_pulsar_clusters.md)	 - Operations about cluster(s)
* [dataos-ctl operate pulsar context](dataos-ctl_operate_pulsar_context.md)	 - Interface for setting Pulsar Context 
* [dataos-ctl operate pulsar functions](dataos-ctl_operate_pulsar_functions.md)	 - Interface for managing Pulsar Functions (lightweight, Lambda-style compute processes that work with Pulsar)
* [dataos-ctl operate pulsar functions-worker](dataos-ctl_operate_pulsar_functions-worker.md)	 - Operations to collect function-worker statistics
* [dataos-ctl operate pulsar namespaces](dataos-ctl_operate_pulsar_namespaces.md)	 - Operations about namespaces
* [dataos-ctl operate pulsar ns-isolation-policy](dataos-ctl_operate_pulsar_ns-isolation-policy.md)	 - Operations about namespace isolation policy
* [dataos-ctl operate pulsar resource-quotas](dataos-ctl_operate_pulsar_resource-quotas.md)	 - Operations about resource quotas
* [dataos-ctl operate pulsar schemas](dataos-ctl_operate_pulsar_schemas.md)	 - Operations related to Schemas associated with Pulsar topics
* [dataos-ctl operate pulsar sinks](dataos-ctl_operate_pulsar_sinks.md)	 - Interface for managing Pulsar IO sinks (egress data from Pulsar)
* [dataos-ctl operate pulsar sources](dataos-ctl_operate_pulsar_sources.md)	 - Interface for managing Pulsar IO Sources (ingress data into Pulsar)
* [dataos-ctl operate pulsar subscriptions](dataos-ctl_operate_pulsar_subscriptions.md)	 - Operations about subscription(s)
* [dataos-ctl operate pulsar tenants](dataos-ctl_operate_pulsar_tenants.md)	 - Operations about tenant(s)
* [dataos-ctl operate pulsar token](dataos-ctl_operate_pulsar_token.md)	 - Operations of token
* [dataos-ctl operate pulsar topics](dataos-ctl_operate_pulsar_topics.md)	 - Operations about topic(s)

