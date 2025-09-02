## dataos-ctl operate pulsar schemas delete

Delete the latest schema for a topic

### Synopsis

USED FOR:
    Delete the latest schema for a topic

REQUIRED PERMISSION:
    This command requires namespace admin permissions.

OUTPUT:
    #normal output
    Deleted (topic name) successfully

    #you must specify a topic name, please check if the topic name is provided
    [✖]  the topic name is not specified or the topic name is specified more than one



```
dataos-ctl operate pulsar schemas delete [flags]
```

### Examples

```
    #Delete the latest schema for a topic
    pulsarctl schemas delete (topic name)


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

* [dataos-ctl operate pulsar schemas](dataos-ctl_operate_pulsar_schemas.md)	 - Operations related to Schemas associated with Pulsar topics

