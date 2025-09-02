## dataos-ctl operate pulsar token create-secret-key

Create a secret key.

### Synopsis

USED FOR:
    This command is used for creating a secret key.

REQUIRED PERMISSION:
    This command does not need any permission.

OUTPUT:
    #Create a secret key successfully.
    [0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0 0]

    #Write a base64 encoded secret key to the terminal.
    AAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAAA=

    #Write the secret key to a file successfully.
    Write secret to the file (filename) successfully.

    #Writing the secret key to a file was failed.
    [✖]  writing the secret key to the file (filename) was failed

    #Using invalid signature algorithm to generate secret key.
    [✖]  the signature algorithm '(signature algorithm)' is invalid. Valid options are: 'HS256', 'HS384', 'HS512'



```
dataos-ctl operate pulsar token create-secret-key [flags]
```

### Examples

```
    #Create a secret key.
    pulsarctl token create-secret-key

    #Create a base64 encoded secret key.
    pulsarctl token create-secret-key --base64

    #Create a secret key and save it to a file.
    pulsarctl token create-secret-key --output (file path)


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
  -b, --base64                             Generate a base64 encoded secret key.
      --bookie-service-url string          The bookie web service url that pulsarctl connects to.
  -h, --help                               help for create-secret-key
  -o, --output string                      The output format (text,json,yaml) (default "text")
      --output-file string                 The file that the secret key is written to.
  -a, --signature-algorithm string         The signature algorithm used for generating the secret key. Valid options are:'HS256', 'HS384', 'HS512'. (default "HS256")
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

