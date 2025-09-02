## dataos-ctl operate pulsar bookkeeper auto-recovery set-lost-bookie-recovery-delay

Set the lost bookie recovery delay.

### Synopsis

USED FOR:
    This command is used for setting the lost bookie recovery delay in second.

REQUIRED PERMISSION:
    This command does not need any permission.

OUTPUT:
    #Set the lost bookie recovery delay to the new delay successfully.
    Successfully set the lost bookie recovery delay to (delay)(second)

    #The specified delay time is not specified or the delay time is specified more than one.
    [✖]  the specified delay time is not specified or the delay time is specified more than one



```
dataos-ctl operate pulsar bookkeeper auto-recovery set-lost-bookie-recovery-delay [flags]
```

### Examples

```
    #Set the lost bookie recovery delay.
    pulsarctl bookkeeper auto-recovery set-lost-bookie-recovery-delay (delay)


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
  -h, --help                               help for set-lost-bookie-recovery-delay
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

