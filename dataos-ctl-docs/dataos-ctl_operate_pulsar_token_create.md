## dataos-ctl operate pulsar token create

Create a token string.

### Synopsis

USED FOR:
    This command is used for create a token string.

REQUIRED PERMISSION:
    This command does not need any permission.

OUTPUT:
    #Create a token successfully.
    eyJhbGciOiJIUzI1NiJ9.eyJzdWIiOiJoZWxsby10ZXN0In0.qxaczygeZaZDlK7jQHHXCaQRbwd2wxIHjCH3y_Lo2Q4

    #None of the signing keys is specified.
    [✖]  none of the signing keys is specified

    #Signing key is specified more than one.
    [✖]  the signing key is specified more than one



```
dataos-ctl operate pulsar token create [flags]
```

### Examples

```
    #Create a token using a secret key string.
    pulsarctl token create --secret-key-string (secret-key-string) --subject (subject)

    #Create a token using a secret key file.
    pulsarctl token create --secret-key-file (secret-key-file-path) --subject (subject)

    #Create a token using a private key file.
    pulsarctl token create --private-key-file (private-key-file-path) --subject (subject)

    #Create a token with expire time.
    pulsarctl token create --secret-key-string (secret-key-string) --subject (subject) --expire 1m

    #Create a token using a base64 encoded secret key.
    pulsarctl token create --secret-key-string (secret-key-string) --base64 --subject (subject)


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
      --base64                             The secret key is base64 encoded or not.
      --bookie-service-url string          The bookie web service url that pulsarctl connects to.
      --expire string                      The expire time for a token. e.g. 1s, 1m, 1h
  -h, --help                               help for create
  -o, --output string                      The output format (text,json,yaml) (default "text")
      --private-key-file string            The private key file that used to sign a toke.
      --secret-key-file string             The secret key file that used to sign a token.
      --secret-key-string string           The secret key string that used to sign a token.
  -a, --signature-algorithm string         The signature algorithm used to generate the secret key or the private key Valid options are: 'HS256', 'HS384', 'HS512', 'RS256', 'RS384', 'RS512', 'PS256', 'PS384', 'PS512', 'ES256', 'ES384', 'ES512'. (default "RS256")
      --subject string                     The 'subject' or 'principal' associate with this token.
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

* [dataos-ctl operate pulsar token](dataos-ctl_operate_pulsar_token.md)	 - Operations of token

