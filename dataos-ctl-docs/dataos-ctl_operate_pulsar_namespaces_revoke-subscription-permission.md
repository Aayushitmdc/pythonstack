## dataos-ctl operate pulsar namespaces revoke-subscription-permission

Revoke a client role permissions of accessing a subscription of a namespace

### Synopsis

USED FOR:
    This command is used for revoking a client role permissions of accessing a subscription of a namespace.

REQUIRED PERMISSION:
    This command requires tenant admin permissions and broker has read-writer permissions on the zookeeper.

OUTPUT:
    #normal output
    Revoke the client role (role-name) permissions of accessing the subscription (subscription-name) of the namespace (namespace-name) successfully

    #the namespace name is not specified or the subscription name is not specified
    [✖]  need to specified namespace name and subscription name

    #the namespace name is not in the format of <tenant>/<namespace>
    [✖]  The complete name of namespace is invalid. complete name : <namespace-complete-name>

    #the tenant name and(or) namespace name is empty
    [✖]  Invalid tenant or namespace. [<tenant>/<namespace>]

    #the tenant name contains unsupported special chars. the alphanumeric (a-zA-Z0-9) and the special chars (-=:.%)  is allowed
    [✖]  Tenant name include unsupported special chars. tenant : [<namespace>]

    #the namespace name contains unsupported special chars. the  alphanumeric (a-zA-Z0-9) and the special chars (-=:.%) is allowed
    [✖]  Namespace name include unsupported special chars. namespace : [<namespace>]



```
dataos-ctl operate pulsar namespaces revoke-subscription-permission [flags]
```

### Examples

```
USED FOR:
    This command is used for revoking a client role permissions of accessing a subscription of a namespace.

REQUIRED PERMISSION:
    This command requires tenant admin permissions and broker has read-writer permissions on the zookeeper.

OUTPUT:
    #normal output
    Revoke the client role (role-name) permissions of accessing the subscription (subscription-name) of the namespace (namespace-name) successfully

    #the namespace name is not specified or the subscription name is not specified
    [✖]  need to specified namespace name and subscription name

    #the namespace name is not in the format of <tenant>/<namespace>
    [✖]  The complete name of namespace is invalid. complete name : <namespace-complete-name>

    #the tenant name and(or) namespace name is empty
    [✖]  Invalid tenant or namespace. [<tenant>/<namespace>]

    #the tenant name contains unsupported special chars. the alphanumeric (a-zA-Z0-9) and the special chars (-=:.%)  is allowed
    [✖]  Tenant name include unsupported special chars. tenant : [<namespace>]

    #the namespace name contains unsupported special chars. the  alphanumeric (a-zA-Z0-9) and the special chars (-=:.%) is allowed
    [✖]  Namespace name include unsupported special chars. namespace : [<namespace>]


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
  -h, --help                               help for revoke-subscription-permission
  -o, --output string                      The output format (text,json,yaml) (default "text")
      --role string                        Client role to which revoke permissions
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

