## dataos-ctl operate pulsar bookkeeper auto-recovery trigger-audit

Trigger audit by resetting the lost bookie recovery delay.

### Synopsis

USED FOR:
    This command is used for triggering audit by resetting the lost bookie recovery delay.

REQUIRED PERMISSION:
    This command does not need any permission.

OUTPUT:
    #Trigger audit by resetting the lost bookie recovery delay successfully.
    Successfully trigger audit by resetting the lost bookie recovery delay.



```
dataos-ctl operate pulsar bookkeeper auto-recovery trigger-audit [flags]
```

### Examples

```
    #Trigger audit by resetting the lost bookie recovery delay
    pulsarctl bookkeeper auto-recovery trigger-audit


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
  -h, --help                               help for trigger-audit
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

* [dataos-ctl operate pulsar bookkeeper auto-recovery](dataos-ctl_operate_pulsar_bookkeeper_auto-recovery.md)	 - Operations about auto recovering

