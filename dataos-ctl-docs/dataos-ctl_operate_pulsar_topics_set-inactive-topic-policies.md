## dataos-ctl operate pulsar topics set-inactive-topic-policies

Set the inactive topic policies on a topic

### Synopsis

USED FOR:
    Set the inactive topic policies on a topic

REQUIRED PERMISSION:
    This command requires tenant admin permissions.

OUTPUT:


```
dataos-ctl operate pulsar topics set-inactive-topic-policies [flags]
```

### Examples

```
    #Set the inactive topic policies on a topic
    pulsarctl topics set-inactive-topic-policies [topic] 
	--enable-delete-while-inactive true 
	--max-inactive-duration 1h 
	--delete-mode delete_when_no_subscriptions


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
  -m, --delete-mode string                 Mode of delete inactive topic, Valid options are: [delete_when_no_subscriptions, delete_when_subscriptions_caught_up]
  -e, --enable-delete-while-inactive       Control whether deletion is enabled while inactive
  -h, --help                               help for set-inactive-topic-policies
  -t, --max-inactive-duration string       Max duration of topic inactivity in seconds, topics that are inactive for longer than this value will be deleted (eg: 1s, 10s, 1m, 5h, 3d)
  -o, --output string                      The output format (text,json,yaml) (default "text")
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

* [dataos-ctl operate pulsar topics](dataos-ctl_operate_pulsar_topics.md)	 - Operations about topic(s)

