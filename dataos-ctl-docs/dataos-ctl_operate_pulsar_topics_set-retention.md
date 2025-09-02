## dataos-ctl operate pulsar topics set-retention

Set the retention policy for a topic

### Synopsis

USED FOR:
    Set the retention policy for a topic

REQUIRED PERMISSION:
    This command requires tenant admin permissions.

OUTPUT:
    #normal output
    Set the retention policy for [topic] successfully

    #you must specify a tenant/namespace/topic name, please check if the tenant/namespace/topic name is provided
    [✖]  the topic name is not specified or the topic name is specified more than one

    #the tenant does not exist
    [✖]  code: 404 reason: Tenant does not exist

    #the namespace does not exist
    [✖]  code: 404 reason: Namespace (tenant/namespace) does not exist

    #topic-level policy is not enabled
    [✖]  code: 405 reason: Topic level policy is disabled, please enable broker configs of systemTopicEnabled and topicLevelPoliciesEnabled



```
dataos-ctl operate pulsar topics set-retention [flags]
```

### Examples

```
    #Set the retention policy for a topic
    pulsarctl topics set-retention tenant/namespace/topic --time 100m --size 1G


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
  -h, --help                               help for set-retention
  -o, --output string                      The output format (text,json,yaml) (default "text")
      --size string                        Retention size limit (eg: 10M, 16G, 3T). 0 or less than 1MB means no retention and -1 means infinite size retention
      --time string                        Retention time in minutes (or minutes, hours, days, weeks eg: 100m, 3h, 2d, 5w). 0 means no retention and -1 means infinite time retention
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

