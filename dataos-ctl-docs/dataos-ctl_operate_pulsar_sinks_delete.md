## dataos-ctl operate pulsar sinks delete

Delete a Pulsar IO Sink connector

### Synopsis

USED FOR:
    This command is used for deleting a Pulsar IO sink connector.

REQUIRED PERMISSION:
    This command requires namespace function permissions.

OUTPUT:
    #normal output
    Deleted (the name of a Pulsar Sink) successfully

    #sink doesn't exist
    code: 404 reason: Sink (the name of a Pulsar Sink) doesn't exist



```
dataos-ctl operate pulsar sinks delete [flags]
```

### Examples

```
    #Delete a Pulsar IO sink connector
    pulsarctl sink delete 
	--tenant public
	--namespace default
	--name (the name of Pulsar Sink)


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
      --name string                        The sink's name
      --namespace string                   The sink's namespace
  -o, --output string                      The output format (text,json,yaml) (default "text")
      --tenant string                      The sink's tenant
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

* [dataos-ctl operate pulsar sinks](dataos-ctl_operate_pulsar_sinks.md)	 - Interface for managing Pulsar IO sinks (egress data from Pulsar)

