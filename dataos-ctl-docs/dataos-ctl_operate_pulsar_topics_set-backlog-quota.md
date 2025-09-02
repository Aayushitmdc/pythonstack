## dataos-ctl operate pulsar topics set-backlog-quota

Set a backlog quota policy for a topic

### Synopsis

USED FOR:
    Set a backlog quota policy for a topic

REQUIRED PERMISSION:
    This command requires tenant admin permissions.

OUTPUT:
    #normal output
    Set backlog quota successfully for [topic]



```
dataos-ctl operate pulsar topics set-backlog-quota [flags]
```

### Examples

```
    #Set a backlog quota policy for a topic
    pulsarctl topics set-backlog-quota topic 
	--limit-size 16G 
	--limit-time -1 
	--policy <producer_request_hold|producer_exception|consumer_backlog_eviction> 
	--type <destination_storage|message_age>


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
  -h, --help                               help for set-backlog-quota
      --limit-size string                  Size limit (eg: 10M, 16G)
      --limit-time int                     Time limit in seconds (default -1)
  -o, --output string                      The output format (text,json,yaml) (default "text")
  -p, --policy string                      Retention policy to enforce when the limit is reached.
                                           Valid options are: [producer_request_hold, producer_exception, consumer_backlog_eviction]
      --tls-allow-insecure                 Allow TLS insecure connection
      --tls-cert-file string               File path for TLS cert used for authentication
      --tls-enable-hostname-verification   Enable TLS hostname verification
      --tls-key-file string                File path for TLS key used for authentication
      --tls-trust-cert-path string         Allow TLS trust cert file path
      --token string                       Using the token to authentication
      --token-file string                  Using the token file to authentication
  -t, --type string                        Backlog quota type to set.
                                           Valid options are: [destination_storage, message_age] (default "destination_storage")
```

### Options inherited from parent commands

```
  -v, --verbose int   set log level, use 0 to silence, 4 for debugging (default 4)
```

### SEE ALSO

* [dataos-ctl operate pulsar topics](dataos-ctl_operate_pulsar_topics.md)	 - Operations about topic(s)

