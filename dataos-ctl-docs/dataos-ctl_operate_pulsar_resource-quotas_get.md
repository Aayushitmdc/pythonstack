## dataos-ctl operate pulsar resource-quotas get

Get the resource quota for a specified namespace bundle, or default quota if no namespace/bundle is specified.

### Synopsis

USED FOR:
    Get the resource quota for a specified namespace bundle, or default quota if no namespace/bundle is specified.

REQUIRED PERMISSION:
    This command requires super-user permissions.

OUTPUT:
    #normal output
    {
      "msgRateIn" : 40.0,
      "msgRateOut" : 120.0,
      "bandwidthIn" : 100000.0,
      "bandwidthOut" : 300000.0,
      "memory" : 80.0,
      "dynamic" : true
    }



```
dataos-ctl operate pulsar resource-quotas get [flags]
```

### Examples

```
    #Get the resource quota use default namespace/bundle
    pulsarctl resource-quotas get

    #Get the resource quota for a specified namespace bundle
    pulsarctl resource-quotas get (namespace name) (bundle range)


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
  -h, --help                               help for get
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

