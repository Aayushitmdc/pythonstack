## dataos-ctl operate pulsar bookkeeper ledger delete

Delete a ledger

### Synopsis

USED FOR:
    This command is used for deleting a ledger.

REQUIRED PERMISSION:
    none

OUTPUT:
    #normal output
    Successfully delete the ledger (ledger-id)

    #the ledger id is not specified or the ledger id is specified more than one
    [✖]  the ledger id is not specified or the ledger id is specified more than one



```
dataos-ctl operate pulsar bookkeeper ledger delete [flags]
```

### Examples

```
    #Delete the specified ledger
    pulsarctl bookkeeper ledger delete (ledger-id)


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
  -h, --help                               help for delete
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

* [dataos-ctl operate pulsar bookkeeper ledger](dataos-ctl_operate_pulsar_bookkeeper_ledger.md)	 - Operations about ledger

