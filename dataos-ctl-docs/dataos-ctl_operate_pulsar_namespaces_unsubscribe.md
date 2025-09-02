## dataos-ctl operate pulsar namespaces unsubscribe

Unsubscribe the specified subscription for all topic of a namespace

### Synopsis

USED FOR:
    This command is used for unsubscribing the specified subscription for all topics of a namespace.

REQUIRED PERMISSION:
    This command requires tenant admin permissions.

OUTPUT:
    #normal output
    Successfully unsubscribe the subscription (subscription-name) for all topics of the namespace (namespace-name)

    #the namespace name is not specified or the subscription name is not specified
    [✖]  need two arguments apply to the command

    #the specified namespace name does not exist
    [✖]  code: 404 reason: Namespace does not exist

    #the namespace name is not in the format of <tenant>/<namespace>
    [✖]  The complete name of namespace is invalid. complete name : <namespace-complete-name>

    #the tenant name and(or) namespace name is empty
    [✖]  Invalid tenant or namespace. [<tenant>/<namespace>]

    #the tenant name contains unsupported special chars. the alphanumeric (a-zA-Z0-9) and the special chars (-=:.%)  is allowed
    [✖]  Tenant name include unsupported special chars. tenant : [<namespace>]

    #the namespace name contains unsupported special chars. the  alphanumeric (a-zA-Z0-9) and the special chars (-=:.%) is allowed
    [✖]  Namespace name include unsupported special chars. namespace : [<namespace>]



```
dataos-ctl operate pulsar namespaces unsubscribe [flags]
```

### Examples

```
    #Unsubscribe the specified subscription <subscription-name> for all topic of the namespace (namespace-name)
    pulsarctl namespaces unsubscribe (namespace-name) (subscription-name)

    #Unsubscribe the specified subscription (subscription-name) for all topic of the namespace (namespace-name) with bundle range <bundle>
    pulsarctl namespaces unsubscribe --bundle (bundle) (namespace-name) (subscription-name)


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
  -b, --bundle string                      {start_boundary}_{end_boundary}
  -h, --help                               help for unsubscribe
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

