## dataos-ctl operate pulsar topics set-publish-rate

Set message publish rate for a topic

### Synopsis

USED FOR:
    Set message publish rate for a topic

REQUIRED PERMISSION:
    This command requires tenant admin permissions.

OUTPUT:
    #normal output
    Set message publish rate successfully for [topic]

    #the topic name is not specified or the topic name is specified more than one
    [✖]  the topic name is not specified or the topic name is specified more than one

    #the topic name is not in the format of <tenant>/<namespace>/<topic> or <topic>
    [✖]  Invalid short topic name '<topic-name>', it should be in the format of <tenant>/<namespace>/<topic> or <topic>

    #the topic name is not in the format of <domain>://<tenant>/<namespace>/<topic>
    [✖]  Invalid complete topic name '<topic-name>', it should be in the format of <domain>://<tenant>/<namespace>/<topic>

    #the topic name is not in the format of <tenant>/<namespace>/<topic>
    [✖]  Invalid topic name '<topic-name>', it should be in the format of<tenant>/<namespace>/<topic>

    #topic-level policy is not enabled
    [✖]  code: 405 reason: Topic level policy is disabled, please enable broker configs of systemTopicEnabled and topicLevelPoliciesEnabled

    #the namespace name is not in the format of <tenant>/<namespace>
    [✖]  The complete name of namespace is invalid. complete name : <namespace-complete-name>

    #the tenant name and(or) namespace name is empty
    [✖]  Invalid tenant or namespace. [<tenant>/<namespace>]

    #the tenant name contains unsupported special chars. the alphanumeric (a-zA-Z0-9) and the special chars (-=:.%)  is allowed
    [✖]  Tenant name include unsupported special chars. tenant : [<namespace>]

    #the namespace name contains unsupported special chars. the  alphanumeric (a-zA-Z0-9) and the special chars (-=:.%) is allowed
    [✖]  Namespace name include unsupported special chars. namespace : [<namespace>]



```
dataos-ctl operate pulsar topics set-publish-rate [flags]
```

### Examples

```
    #Set message publish rate for a topic
    pulsarctl topics set-publish-rate topic --msg-publish-rate 4 --byte-publish-rate 5 --publish-rate-period 6 --relative-to-publish-rate


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
      --byte-publish-rate int              byte-publish-rate (default -1 will be overwrite if not passed) (default -1)
  -h, --help                               help for set-publish-rate
      --msg-publish-rate int               message-publish-rate (default -1 will be overwrite if not passed) (default -1)
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

