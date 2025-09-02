## dataos-ctl operate pulsar bookkeeper bookie last-log-marker

Get the last log marker of the journals on a bookie.

### Synopsis

USED FOR:
    This command is used for getting the last log marker of the journals on a bookie.

REQUIRED PERMISSION:
    This command does not need any permission.

OUTPUT:
    #Successfully get the last log marker of the journals on a bookie.
    {
        JournalId1 : position1,
        JournalId2 : position2,
        ...
    }



```
dataos-ctl operate pulsar bookkeeper bookie last-log-marker [flags]
```

### Examples

```
    #Get the last log marker of the journals on a bookie.
    pulsarctl bookkeeper bookie last-log-marker


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
  -h, --help                               help for last-log-marker
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

* [dataos-ctl operate pulsar bookkeeper bookie](dataos-ctl_operate_pulsar_bookkeeper_bookie.md)	 - Operations about one bookie

