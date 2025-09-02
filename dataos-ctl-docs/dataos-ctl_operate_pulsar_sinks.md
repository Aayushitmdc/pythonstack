## dataos-ctl operate pulsar sinks

Interface for managing Pulsar IO sinks (egress data from Pulsar)

```
dataos-ctl operate pulsar sinks [flags]
```

### Options

```
  -h, --help   help for sinks
```

### Options inherited from parent commands

```
  -s, --admin-service-url string           The admin web service url that pulsarctl connects to. (default "http://localhost:8080")
      --auth-params string                 Authentication parameters are used to configure the authentication provider specified by "AuthPlugin".
                                            Tls example: "tlsCertFile:val1,tlsKeyFile:val2"
                                            Token example: "authParams=file:///path/to/token/file" or "authParams=token:tokenVal"
      --auth-plugin string                 AuthPlugin is used to specify the plugin to use for authentication,
                                            the supported values are "org.apache.pulsar.client.impl.auth.AuthenticationTls"
                                            and "org.apache.pulsar.client.impl.auth.AuthenticationToken"
      --bookie-service-url string          The bookie web service url that pulsarctl connects to.
      --tls-allow-insecure                 Allow TLS insecure connection
      --tls-cert-file string               File path for TLS cert used for authentication
      --tls-enable-hostname-verification   Enable TLS hostname verification
      --tls-key-file string                File path for TLS key used for authentication
      --tls-trust-cert-path string         Allow TLS trust cert file path
      --token string                       Using the token to authentication
      --token-file string                  Using the token file to authentication
  -v, --verbose int                        set log level, use 0 to silence, 4 for debugging (default 4)
```

### SEE ALSO

* [dataos-ctl operate pulsar](dataos-ctl_operate_pulsar.md)	 - Pulsar management
* [dataos-ctl operate pulsar sinks create](dataos-ctl_operate_pulsar_sinks_create.md)	 - Create a Pulsar IO sink connector to run in a Pulsar cluster
* [dataos-ctl operate pulsar sinks delete](dataos-ctl_operate_pulsar_sinks_delete.md)	 - Delete a Pulsar IO Sink connector
* [dataos-ctl operate pulsar sinks get](dataos-ctl_operate_pulsar_sinks_get.md)	 - Get the information about a Pulsar IO sink connector
* [dataos-ctl operate pulsar sinks list](dataos-ctl_operate_pulsar_sinks_list.md)	 - Get the list of all the running Pulsar IO sink connectors
* [dataos-ctl operate pulsar sinks restart](dataos-ctl_operate_pulsar_sinks_restart.md)	 - Restart sink instance
* [dataos-ctl operate pulsar sinks start](dataos-ctl_operate_pulsar_sinks_start.md)	 - Start sink instance
* [dataos-ctl operate pulsar sinks status](dataos-ctl_operate_pulsar_sinks_status.md)	 - Get the current status of a Pulsar Sink
* [dataos-ctl operate pulsar sinks stop](dataos-ctl_operate_pulsar_sinks_stop.md)	 - Stops sink instance
* [dataos-ctl operate pulsar sinks update](dataos-ctl_operate_pulsar_sinks_update.md)	 - Update a Pulsar IO sink connector

