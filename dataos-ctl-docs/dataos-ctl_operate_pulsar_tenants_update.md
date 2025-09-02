## dataos-ctl operate pulsar tenants update

update the configuration for a tenant

### Synopsis

USED FOR:
    This command is used for updating the configuration of a tenant.

REQUIRED PERMISSION:
    This command requires super-user permissions.

OUTPUT:
    #normal output
    Update tenant [%s] successfully

    #the tenant name is not specified or the tenant name is specified more than one
    [✖]  the tenant name is not specified or the tenant name is specified more than one

    #the specified tenant does not exist in
    [✖]  code: 404 reason: Tenant does not exist

    #the flag --admin-roles or --allowed-clusters are not specified
    [✖]  the admin roles or the allowed clusters is not specified



```
dataos-ctl operate pulsar tenants update [flags]
```

### Examples

```
    #clear the tenant configuration of a tenant
    pulsarctl tenant update (tenant-name)

    #update the admin roles for tenant (tenant-name)
    pulsarctl tenants update --admin-roles (admin-A)--admin-roles (admin-B) (tenant-name)

    #update the allowed cluster list for tenant (tenant-name)
    pulsarctl tenants update --allowed-clusters (cluster-A) --allowed-clusters (cluster-B) (tenant-name)


```

### Options

```
  -r, --admin-roles strings                Allowed admins to access the tenant
  -s, --admin-service-url string           The admin web service url that pulsarctl connects to. (default "http://localhost:8080")
  -c, --allowed-clusters strings           Allowed clusters
      --auth-params string                 Authentication parameters are used to configure the authentication provider specified by "AuthPlugin".
                                            Tls example: "tlsCertFile:val1,tlsKeyFile:val2"
                                            Token example: "authParams=file:///path/to/token/file" or "authParams=token:tokenVal"
      --auth-plugin string                 AuthPlugin is used to specify the plugin to use for authentication,
                                            the supported values are "org.apache.pulsar.client.impl.auth.AuthenticationTls"
                                            and "org.apache.pulsar.client.impl.auth.AuthenticationToken"
      --bookie-service-url string          The bookie web service url that pulsarctl connects to.
  -h, --help                               help for update
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

