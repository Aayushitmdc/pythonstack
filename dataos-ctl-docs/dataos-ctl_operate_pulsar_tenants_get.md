## dataos-ctl operate pulsar tenants get

get the configuration of a tenant

### Synopsis

USED FOR:
    This command is used for getting the configuration of a tenant.

REQUIRED PERMISSION:
    This command requires super-user permissions.

OUTPUT:
    #normal output
    {
      "adminRoles": [],
      "allowedClusters": [
        "standalone"
      ]
    }

    #the tenant name is not specified or the tenant name is specified more than one
    [✖]  the tenant name is not specified or the tenant name is specified more than one

    #the specified tenant does not exist in the cluster
    [✖]  code: 404 reason: Tenant does not exist



```
dataos-ctl operate pulsar tenants get [flags]
```

### Examples

```
    #get the configuration of tenant (tenant-name)
    pulsarctl tenants get (tenant-name)


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

* [dataos-ctl operate pulsar tenants](dataos-ctl_operate_pulsar_tenants.md)	 - Operations about tenant(s)

