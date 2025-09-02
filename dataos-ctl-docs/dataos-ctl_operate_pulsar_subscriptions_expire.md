## dataos-ctl operate pulsar subscriptions expire

Expiring messages that older than given expire time (in seconds)

### Synopsis

USED FOR:
    This command is used for expiring messages that older than given expiry time (in seconds) for a subscription.

REQUIRED PERMISSION:
    This command requires tenant admin and namespace produce or consume permissions.

OUTPUT:
    #normal output
    Expire messages after (time)(s) for the subscription (subscription-name) of the topic (topic-name) successfully

    #the topic name and(or) the subscription name is not specified
    [✖]  need to specified the topic name and the subscription name

    #the specified topic does not exist
    [✖]  code: 404 reason: Topic not found

    #the topic name is not in the format of <tenant>/<namespace>/<topic> or <topic>
    [✖]  Invalid short topic name '<topic-name>', it should be in the format of <tenant>/<namespace>/<topic> or <topic>

    #the topic name is not in the format of <domain>://<tenant>/<namespace>/<topic>
    [✖]  Invalid complete topic name '<topic-name>', it should be in the format of <domain>://<tenant>/<namespace>/<topic>

    #the topic name is not in the format of <tenant>/<namespace>/<topic>
    [✖]  Invalid topic name '<topic-name>', it should be in the format of<tenant>/<namespace>/<topic>

    #the namespace name is not in the format of <tenant>/<namespace>
    [✖]  The complete name of namespace is invalid. complete name : <namespace-complete-name>

    #the tenant name and(or) namespace name is empty
    [✖]  Invalid tenant or namespace. [<tenant>/<namespace>]

    #the tenant name contains unsupported special charsthe alphanumeric (a-zA-Z0-9) and the special chars (-=:.%)  is allowed
    [✖]  Tenant name include unsupported special chars. tenant : [<namespace>]

    #the namespace name contains unsupported special charsthe  alphanumeric (a-zA-Z0-9) and the special chars (-=:.%) is allowed
    [✖]  Namespace name include unsupported special chars. namespace : [<namespace>]



```
dataos-ctl operate pulsar subscriptions expire [flags]
```

### Examples

```
expire
```

### Options

```
  -s, --admin-service-url string           The admin web service url that pulsarctl connects to. (default "http://localhost:8080")
  -a, --all                                Expire all messages
      --auth-params string                 Authentication parameters are used to configure the authentication provider specified by "AuthPlugin".
                                            Tls example: "tlsCertFile:val1,tlsKeyFile:val2"
                                            Token example: "authParams=file:///path/to/token/file" or "authParams=token:tokenVal"
      --auth-plugin string                 AuthPlugin is used to specify the plugin to use for authentication,
                                            the supported values are "org.apache.pulsar.client.impl.auth.AuthenticationTls"
                                            and "org.apache.pulsar.client.impl.auth.AuthenticationToken"
      --bookie-service-url string          The bookie web service url that pulsarctl connects to.
  -t, --expire-time int                    Expire messages older than time in seconds
  -h, --help                               help for expire
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

