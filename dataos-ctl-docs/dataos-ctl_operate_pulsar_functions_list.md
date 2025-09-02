## dataos-ctl operate pulsar functions list

List all Pulsar Functions running under a specific tenant and namespace

### Synopsis

USED FOR:
    List all Pulsar Functions running under a specific tenant and namespace.

REQUIRED PERMISSION:
    This command requires super-user permissions.

OUTPUT:
    #normal output
    +--------------------+
    |   Function Name    |
    +--------------------+
    | test_function_name |
    +--------------------+



```
dataos-ctl operate pulsar functions list [flags]
```

### Examples

```
    #List all Pulsar Functions running under a specific tenant and namespace
    pulsarctl functions list 
	--tenant public
	--namespace default


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
      --namespace string                   The namespace of a Pulsar Function
  -o, --output string                      The output format (text,json,yaml) (default "text")
      --tenant string                      The tenant of a Pulsar Function
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

* [dataos-ctl operate pulsar functions](dataos-ctl_operate_pulsar_functions.md)	 - Interface for managing Pulsar Functions (lightweight, Lambda-style compute processes that work with Pulsar)

