## dataos-ctl operate pulsar namespaces set-publish-rate

Set the default message publish rate of a namespace per second

### Synopsis

USED FOR:
    This command is used for setting the default maximum message publish rate of a namespace per second.

REQUIRED PERMISSION:
    This command requires super-user permissions.

OUTPUT:
    #normal output
    Success set the default message publish rate of the namespace (namespace-name) to (rate)

    #the namespace name is not in the format of <tenant>/<namespace>
    [✖]  The complete name of namespace is invalid. complete name : <namespace-complete-name>

    #the tenant name and(or) namespace name is empty
    [✖]  Invalid tenant or namespace. [<tenant>/<namespace>]

    #the tenant name contains unsupported special chars. the alphanumeric (a-zA-Z0-9) and the special chars (-=:.%)  is allowed
    [✖]  Tenant name include unsupported special chars. tenant : [<namespace>]

    #the namespace name contains unsupported special chars. the  alphanumeric (a-zA-Z0-9) and the special chars (-=:.%) is allowed
    [✖]  Namespace name include unsupported special chars. namespace : [<namespace>]



```
dataos-ctl operate pulsar namespaces set-publish-rate [flags]
```

### Examples

```
    #Set the default message publish rate per second by message of the namespace (namespace-name) to (rate)
    pulsarctl namespaces set-publish-rate --msg-rate (rate) (namespace)

    #Set the default message publish rate per second by byte of the namespace (namespace-name) to (rate)
    pulsarctl namespaces set-publish-rate --byte-rate (rate) (namespace)


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
  -b, --byte-rate int                      byte publish rate per second (default -1) (default -1)
  -h, --help                               help for set-publish-rate
  -m, --msg-rate int                       message publish rate per second (default -1) (default -1)
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

* [dataos-ctl operate pulsar namespaces](dataos-ctl_operate_pulsar_namespaces.md)	 - Operations about namespaces

