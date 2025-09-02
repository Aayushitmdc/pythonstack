## dataos-ctl operate pulsar topics stats

Get the stats of an existing topic

### Synopsis

USED FOR:
    This command is used for getting the stats for an existing topic and its connected producers and consumers. (All the rates are computed over a 1 minute window and are relative the last completed 1 minute period)

REQUIRED PERMISSION:
    This command requires namespace admin permissions.

OUTPUT:
    #Get the non-partitioned topic stats
    {
      "msgRateIn": 0,
      "msgRateOut": 0,
      "msgThroughputIn": 0,
      "msgThroughputOut": 0,
      "averageMsgSize": 0,
      "storageSize": 0,
      "publishers": [],
      "subscriptions": {},
      "replication": {},
      "deduplicationStatus": "Disabled"
    }

    #Get the partitioned topic stats
    {
      "msgRateIn": 0,
      "msgRateOut": 0,
      "msgThroughputIn": 0,
      "msgThroughputOut": 0,
      "averageMsgSize": 0,
      "storageSize": 0,
      "publishers": [],
      "subscriptions": {},
      "replication": {},
      "deduplicationStatus": "",
      "metadata": {
        "partitions": 1
      },
      "partitions": {}
    }

    #Get the partitioned topic stats and per partition topic stats
    {
      "msgRateIn": 0,
      "msgRateOut": 0,
      "msgThroughputIn": 0,
      "msgThroughputOut": 0,
      "averageMsgSize": 0,
      "storageSize": 0,
      "publishers": [],
      "subscriptions": {},
      "replication": {},
      "deduplicationStatus": "",
      "metadata": {
        "partitions": 1
      },
      "partitions": {
        "<topic-name>": {
          "msgRateIn": 0,
          "msgRateOut": 0,
          "msgThroughputIn": 0,
          "msgThroughputOut": 0,
          "averageMsgSize": 0,
          "storageSize": 0,
          "publishers": [],
          "subscriptions": {},
          "replication": {},
          "deduplicationStatus": ""
        }
      }
    }

    #the topic name is not specified or the topic name is specified more than one
    [✖]  the topic name is not specified or the topic name is specified more than one

    #the specified topic does not exist or the specified topic is a partitioned-topic and you don't specified --partitioned-topic or the specified topic is a non-partitioned topic and you specified --partitioned-topic
    code: 404 reason: Topic not found

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

    #the tenant name contains unsupported special chars. the alphanumeric (a-zA-Z0-9) and the special chars (-=:.%)  is allowed
    [✖]  Tenant name include unsupported special chars. tenant : [<namespace>]

    #the namespace name contains unsupported special chars. the  alphanumeric (a-zA-Z0-9) and the special chars (-=:.%) is allowed
    [✖]  Namespace name include unsupported special chars. namespace : [<namespace>]

SCOPE:
    non-partitioned topic, a partition of a partitioned topic, partitioned topic



```
dataos-ctl operate pulsar topics stats [flags]
```

### Examples

```
    #Get the non-partitioned topic (topic-name) stats
    pulsarctl topic stats (topic-name)

    #Get the partitioned topic (topic-name) stats
    pulsarctl topic stats --partitioned-topic (topic-name)

    #Get the partitioned topic (topic-name) stats and per partition stats
    pulsarctl topic stats --partitioned-topic --per-partition (topic-name)


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
  -h, --help                               help for stats
  -o, --output string                      The output format (text,json,yaml) (default "text")
  -p, --partitioned-topic                  Get the partitioned topic stats
      --per-partition                      Get the per partition topic stats
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

