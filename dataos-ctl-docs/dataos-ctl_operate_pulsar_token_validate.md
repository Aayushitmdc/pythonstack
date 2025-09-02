## dataos-ctl operate pulsar token validate

Validate a token.

### Synopsis

USED FOR:
    This command is used for validating a token.

REQUIRED PERMISSION:
    This command does not need any permission.

OUTPUT:
    #The token is valid.
    The subject is (subject), and the expire time is (time).

    #Both the token string and the token file are not specified.
    [✖]  both the token string and the token file are not specified

    #Both the token string and the token file are specified.
    [✖]  both the token string and token file are specified

    #There is no key to validate the token.
    [✖]  none of the validate keys is specified

    #The key used to validate token is specified more than one.
    [✖]  the validate key is specified more than one



```
dataos-ctl operate pulsar token validate [flags]
```

### Examples

```
    #Validate a token string using the specified secret key string.
    pulsarctl token validate --token-string (token) --secret-key-string (secret-key-string)

    #Validate a token file using the specified secret key file.
    pulsarctl token validate --token-string (token) --secret-key-file (secret-key-file-path)

    #Validate a token string using the specified public key file.
    pulsarctl token validate --token-string (token) --public-key-file (public-key-file-path)

    #Validate a token string using the specified base64 encoded secret key string.
    pulsarctl token validate --token-string (token) --secret-key-string (secret-key-string) --base64

    #Validate a token file that signed with the specified secret key string and the specified signature algorithm.
    pulsarctl toke validate --token-string (token) --secret-key-file (secret-key-file-path) --signature-algorithm (algorithm)


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
  -h, --help                               help for validate
  -o, --output string                      The output format (text,json,yaml) (default "text")
      --public-key-file string             The public key file that used to validate a token.
      --secret-key-file string             The secret key file that used to validate a token.
      --secret-key-string string           The secret key string that used to validate a token.
  -a, --signature-algorithm string         The signature algorithm is used for generating the token. Valid options are: 'HS256', 'HS384', 'HS512', 'RS256', 'RS384', 'RS512', 'PS256', 'PS384', 'PS512', 'ES256', 'ES384', 'ES512'. (default "RS256")
      --tls-allow-insecure                 Allow TLS insecure connection
      --tls-cert-file string               File path for TLS cert used for authentication
      --tls-enable-hostname-verification   Enable TLS hostname verification
      --tls-key-file string                File path for TLS key used for authentication
      --tls-trust-cert-path string         Allow TLS trust cert file path
      --token string                       Using the token to authentication
      --token-file string                  The token file that will be validated.
      --token-string string                The token string that will be validated.
```

### Options inherited from parent commands

```
  -v, --verbose int   set log level, use 0 to silence, 4 for debugging (default 4)
```

### SEE ALSO

* [dataos-ctl operate pulsar token](dataos-ctl_operate_pulsar_token.md)	 - Operations of token

