## dataos-ctl operate pulsar resource-quotas set

Set the resource quota for specified namespace bundle, or default quota if no namespace/bundle specified.

### Synopsis

USED FOR:
    Set the resource quota for specified namespace bundle, or default quota if no namespace/bundle specified.

REQUIRED PERMISSION:
    This command requires super-user permissions.

OUTPUT:
    #normal output
    Set (default) resource quota successful



```
dataos-ctl operate pulsar resource-quotas set [flags]
```

### Examples

```
    #Set the resource quota use default namespace/bundle
    pulsarctl resource-quotas set

    #Set the resource quota for specified namespace bundle
    pulsarctl resource-quotas set --namespace (namespace name) --bundle (bundle range)--msgRateIn (msg rate in value)--msgRateOut (msg rate out)--bandwidthIn (bandwidth in)--bandwidthOut (bandwidth out)--memory (memory)--dynamic


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
      --bandwidthIn int                    expected inbound bandwidth (bytes/second)
      --bandwidthOut int                   expected outbound bandwidth (bytes/second)
      --bookie-service-url string          The bookie web service url that pulsarctl connects to.
  -b, --bundle string                      {start-boundary}_{end-boundary}, must be specified together with '--namespace'
      --dynamic                            dynamic (allow to be dynamically re-calculated) or not
  -h, --help                               help for set
      --memory int                         expected memory usage (Mbytes)
      --msgRateIn int                      expected incoming messages per second
      --msgRateOut int                     expected outgoing messages per second
  -n, --namespace string                   cluster/namespace, must be specified together with '--bundle'
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

* [dataos-ctl operate pulsar resource-quotas](dataos-ctl_operate_pulsar_resource-quotas.md)	 - Operations about resource quotas

