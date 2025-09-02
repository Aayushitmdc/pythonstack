## dataos-ctl operate pulsar context set

Sets a context entry in pulsarconfig

### Synopsis

USED FOR:
    Sets a context entry in pulsarconfig, Specifying a name that already exists will merge new fields on top of existing values for those fields.

REQUIRED PERMISSION:
    This command does not need any permission

OUTPUT:
    #normal output
    Set context successful



```
dataos-ctl operate pulsar context set [flags]
```

### Examples

```
    #Sets the user field on the gce context entry without touching other values
    pulsarctl context set [options]

    #Use set of context to define your cluster
    pulsarctl context set development --admin-service-url="http://{host}:8080" --bookie-service-url="http://{host}:8083"


```

### Options

```
  -s, --admin-service-url string           The admin web service url that pulsarctl connects to.
  -a, --audience string                    The audience identifier for the Pulsar instance
      --auth-params string                 Authentication parameters are used to configure the authentication provider specified by "AuthPlugin".
                                            Tls example: "tlsCertFile:val1,tlsKeyFile:val2"
                                            Token example: "authParams=file:///path/to/token/file" or "authParams=token:tokenVal"
      --auth-plugin string                 AuthPlugin is used to specify the plugin to use for authentication,
                                            the supported values are "org.apache.pulsar.client.impl.auth.AuthenticationTls"
                                            and "org.apache.pulsar.client.impl.auth.AuthenticationToken"
      --bookie-service-url string          The bookie web service url that pulsarctl connects to.
  -c, --client-id string                   The OAuth 2.0 client identifier for pulsarctl
  -h, --help                               help for set
  -i, --issuer-endpoint string             The OAuth 2.0 issuer endpoint
  -k, --key-file string                    The path to the private key file
      --scope string                       The OAuth 2.0 scope(s) to request
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

* [dataos-ctl operate pulsar context](dataos-ctl_operate_pulsar_context.md)	 - Interface for setting Pulsar Context 

