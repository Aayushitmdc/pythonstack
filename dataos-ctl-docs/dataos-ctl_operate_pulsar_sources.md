## dataos-ctl operate pulsar sources

Interface for managing Pulsar IO Sources (ingress data into Pulsar)

```
dataos-ctl operate pulsar sources [flags]
```

### Options

```
  -h, --help   help for sources
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
* [dataos-ctl operate pulsar sources create](dataos-ctl_operate_pulsar_sources_create.md)	 - Submit a Pulsar IO source connector to run in a Pulsar cluster
* [dataos-ctl operate pulsar sources delete](dataos-ctl_operate_pulsar_sources_delete.md)	 - Delete a Pulsar IO source connector
* [dataos-ctl operate pulsar sources get](dataos-ctl_operate_pulsar_sources_get.md)	 - Gets the information about a Pulsar IO source connector
* [dataos-ctl operate pulsar sources list](dataos-ctl_operate_pulsar_sources_list.md)	 - List all running Pulsar IO source connectors
* [dataos-ctl operate pulsar sources restart](dataos-ctl_operate_pulsar_sources_restart.md)	 - Restart source instance
* [dataos-ctl operate pulsar sources start](dataos-ctl_operate_pulsar_sources_start.md)	 - Start source instance
* [dataos-ctl operate pulsar sources status](dataos-ctl_operate_pulsar_sources_status.md)	 - Check the current status of a Pulsar Source
* [dataos-ctl operate pulsar sources stop](dataos-ctl_operate_pulsar_sources_stop.md)	 - Stops source instance
* [dataos-ctl operate pulsar sources update](dataos-ctl_operate_pulsar_sources_update.md)	 - Update a Pulsar IO source connector

