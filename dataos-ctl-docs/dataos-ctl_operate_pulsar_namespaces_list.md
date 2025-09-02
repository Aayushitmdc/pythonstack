## dataos-ctl operate pulsar namespaces list

Get the list of namespaces of a tenant

### Synopsis

USED FOR:
    Get the list of namespaces of a tenant

REQUIRED PERMISSION:
    This command requires tenant admin permissions.

OUTPUT:
    #normal output
    +------------------+
    |  NAMESPACE NAME  |
    +------------------+
    | public/default   |
    | public/functions |
    +------------------+

    #you must specify a tenant name, please check if the tenant name is provided
    [✖]  the tenant name is not specified or the tenant name is specified more than one

    #the tenant does not exist
    [✖]  code: 404 reason: Tenant does not exist



```
dataos-ctl operate pulsar namespaces list [flags]
```

### Examples

```
    #Get the list of namespaces of a tenant
    pulsarctl namespaces list (tenant name)


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
  -h, --help                               help for list
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

