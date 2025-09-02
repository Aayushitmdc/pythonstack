## dataos-ctl operate pulsar token create-key-pair

Create a private and public key pair.

### Synopsis

USED FOR:
    This command is used for creating a private and public key pair.

REQUIRED PERMISSION:
    This command does not need any permission.

OUTPUT:
    #Create a key pair successfully.
    The private key and public key are generated to (private-key-path) and (public-key-path) successfully.

    #Writing a private key to a file was failed.
    [✖]  failed to write private key to the file (private-key-path)

    #Writing a public key failed to a file was failed.
    [✖]  failed to write public key to the file (public-key-path)

    #The specified output key file path is empty.
    [✖]  the private key file path and the public key file path can not be empty



```
dataos-ctl operate pulsar token create-key-pair [flags]
```

### Examples

```
    #Create a private and public key pair using RS256 signature algorithm.
    pulsarctl token create-key-pair --output-private-key (filepath) --output-public-key (filepath)

    #Create a private and public key pair using the specified signature algorithm.
    pulsarctl toke create-key-pair --signature-algorithm (algorithm) --output-private-key (filepath) --output-public-key (filepath)


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
  -h, --help                               help for create-key-pair
  -o, --output string                      The output format (text,json,yaml) (default "text")
      --output-private-key string          The file that the private key is written to. (default "private.key")
      --output-public-key string           The file that the public key is written to. (default "public.key")
  -a, --signature-algorithm string         The signature algorithm is used for generating the key pair. Valid options are: 'RS256', 'RS384', 'RS512', 'ES256', 'ES384', 'ES512'. (default "RS256")
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

