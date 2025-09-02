## dataos-ctl operate pulsar token show

Show the algorithm and subject of a token.

### Synopsis

USED FOR:
    This command is used for showing the content of a token.

REQUIRED PERMISSION:
    This command does not need any permission.

OUTPUT:
    #Show the content of the given token.
    The algorithm and subject of the token are (signature algorithm), (subject).

    #There is no token to show.
    [✖]  both the token string and the token file are not specified

    #Too many tokens to show.
    [✖]  both the token string and token file are specified



```
dataos-ctl operate pulsar token show [flags]
```

### Examples

```
    #Read a token from the env TOKEN.
    pulsarctl token show

    #Read a token from a given string.
    pulsarctl token show --token-string (token)

    #Read a token from a given file.
    pulsarctl token show --token-file (token)


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
  -h, --help                               help for show
  -o, --output string                      The output format (text,json,yaml) (default "text")
      --tls-allow-insecure                 Allow TLS insecure connection
      --tls-cert-file string               File path for TLS cert used for authentication
      --tls-enable-hostname-verification   Enable TLS hostname verification
      --tls-key-file string                File path for TLS key used for authentication
      --tls-trust-cert-path string         Allow TLS trust cert file path
      --token string                       Using the token to authentication
      --token-file string                  The token file you would like to show the content.
      --token-string string                The token string you would like to show the content.
```

### Options inherited from parent commands

```
  -v, --verbose int   set log level, use 0 to silence, 4 for debugging (default 4)
```

### SEE ALSO

* [dataos-ctl operate pulsar token](dataos-ctl_operate_pulsar_token.md)	 - Operations of token

