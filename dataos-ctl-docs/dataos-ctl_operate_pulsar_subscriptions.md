## dataos-ctl operate pulsar subscriptions

Operations about subscription(s)

```
dataos-ctl operate pulsar subscriptions [flags]
```

### Options

```
  -h, --help   help for subscriptions
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
* [dataos-ctl operate pulsar subscriptions create](dataos-ctl_operate_pulsar_subscriptions_create.md)	 - Create a subscription on a topic from latest or a specific position
* [dataos-ctl operate pulsar subscriptions delete](dataos-ctl_operate_pulsar_subscriptions_delete.md)	 - Delete a subscription of a topic
* [dataos-ctl operate pulsar subscriptions expire](dataos-ctl_operate_pulsar_subscriptions_expire.md)	 - Expiring messages that older than given expire time (in seconds)
* [dataos-ctl operate pulsar subscriptions list](dataos-ctl_operate_pulsar_subscriptions_list.md)	 - list all the existing subscriptions of a topic
* [dataos-ctl operate pulsar subscriptions peek](dataos-ctl_operate_pulsar_subscriptions_peek.md)	 - Peek some messages of a subscription
* [dataos-ctl operate pulsar subscriptions seek](dataos-ctl_operate_pulsar_subscriptions_seek.md)	 - Reset the cursor to a position that is closest to the provided timestamp or messageId
* [dataos-ctl operate pulsar subscriptions skip](dataos-ctl_operate_pulsar_subscriptions_skip.md)	 - Skip messages for the subscription of a topic

