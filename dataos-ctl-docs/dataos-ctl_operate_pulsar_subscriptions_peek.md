## dataos-ctl operate pulsar subscriptions peek

Peek some messages of a subscription

### Synopsis

USED FOR:
    This command is used for peeking some messages of a subscription.

REQUIRED PERMISSION:
    This command requires tenant admin permissions or namespace consumer permissions.

OUTPUT:
    #normal output
    Message ID :
    ledgerID:entryID:PartitionIndex:BatchIndex
    Properties :
    Message :

    #the topic name and(or) the subscription name is not specified
    [✖]  need to specified the topic name and the subscription name

    #the topic name is not in the format of <tenant>/<namespace>/<topic> or <topic>
    [✖]  Invalid short topic name '<topic-name>', it should be in the format of <tenant>/<namespace>/<topic> or <topic>

    #the topic name is not in the format of <domain>://<tenant>/<namespace>/<topic>
    [✖]  Invalid complete topic name '<topic-name>', it should be in the format of <domain>://<tenant>/<namespace>/<topic>

    #the topic name is not in the format of <tenant>/<namespace>/<topic>
    [✖]  Invalid topic name '<topic-name>', it should be in the format of<tenant>/<namespace>/<topic>



```
dataos-ctl operate pulsar subscriptions peek [flags]
```

### Examples

```
    #Peek some messages of a subscription
    pulsarctl subscriptions peek --count (n) (topic-name) (subscription-name)


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
  -n, --count int                          Number of messages (default 1) (default 1)
  -h, --help                               help for peek
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

* [dataos-ctl operate pulsar subscriptions](dataos-ctl_operate_pulsar_subscriptions.md)	 - Operations about subscription(s)

