## dataos-ctl operate pulsar bookkeeper bookie

Operations about one bookie

```
dataos-ctl operate pulsar bookkeeper bookie [flags]
```

### Options

```
  -h, --help   help for bookie
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

* [dataos-ctl operate pulsar bookkeeper](dataos-ctl_operate_pulsar_bookkeeper.md)	 - Operations about bookKeeper
* [dataos-ctl operate pulsar bookkeeper bookie expand-storage](dataos-ctl_operate_pulsar_bookkeeper_bookie_expand-storage.md)	 - Expand storage for a bookie.
* [dataos-ctl operate pulsar bookkeeper bookie gc](dataos-ctl_operate_pulsar_bookkeeper_bookie_gc.md)	 - Trigger garbage collection for a bookie.
* [dataos-ctl operate pulsar bookkeeper bookie gc-details](dataos-ctl_operate_pulsar_bookkeeper_bookie_gc-details.md)	 - Get the garbage collection details of a bookie.
* [dataos-ctl operate pulsar bookkeeper bookie gc-status](dataos-ctl_operate_pulsar_bookkeeper_bookie_gc-status.md)	 - Get the garbage collection status of a bookie.
* [dataos-ctl operate pulsar bookkeeper bookie last-log-marker](dataos-ctl_operate_pulsar_bookkeeper_bookie_last-log-marker.md)	 - Get the last log marker of the journals on a bookie.
* [dataos-ctl operate pulsar bookkeeper bookie list-disk-file](dataos-ctl_operate_pulsar_bookkeeper_bookie_list-disk-file.md)	 - Get all the files on the disk of a bookie.
* [dataos-ctl operate pulsar bookkeeper bookie state](dataos-ctl_operate_pulsar_bookkeeper_bookie_state.md)	 - Get the state of a bookie.

