## dataos-ctl operate pulsar topics internal-stats

Get the internal stats of the specified topic

### Synopsis

USED FOR:
    This command is used for getting the internal stats for a non-partitioned topic or a partition of a partitioned topic.

REQUIRED PERMISSION:
    This command requires namespace admin permissions.

OUTPUT:
    #normal output
    {
      "entriesAddedCounter": 0,
      "numberOfEntries": 0,
      "totalSize": 0,
      "currentLedgerEntries": 0,
      "currentLedgerSize": 0,
      "lastLedgerCreatedTimestamp": "",
      "lastLedgerCreationFailureTimestamp": "",
      "waitingCursorsCount": 0,
      "pendingAddEntriesCount": 0,
      "lastConfirmedEntry": "",
      "state": "",
      "ledgers": [
        {
          "ledgerId": 0,
          "entries": 0,
          "size": 0,
          "offloaded": false
        }
      ],
      "cursors": {}
    }

    #the topic name is not specified or the topic name is specified more than one
    [✖]  the topic name is not specified or the topic name is specified more than one

    #the specified topic is not exist or the specified topic is a partitioned topic
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

    #the tenant name contains unsupported special chars. the alphanumeric (a-zA-Z0-9) and the special chars (-=:.%)  is allowed
    [✖]  Tenant name include unsupported special chars. tenant : [<namespace>]

    #the namespace name contains unsupported special chars. the  alphanumeric (a-zA-Z0-9) and the special chars (-=:.%) is allowed
    [✖]  Namespace name include unsupported special chars. namespace : [<namespace>]

SCOPE:
    non-partitioned topic, a partition of a partitioned topic, partitioned topic



```
dataos-ctl operate pulsar topics internal-stats [flags]
```

### Examples

```
    #Get internal stats for an existing non-partitioned-topic (topic-name)
    pulsarctl topic internal-stats (topic-name)

    #Get internal stats for a partition of a partitioned topic
    pulsarctl topic internal-stats --partition (partition) (topic-name)


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
  -h, --help                               help for internal-stats
  -o, --output string                      The output format (text,json,yaml) (default "text")
  -p, --partition int                      The partitioned topic index value (default -1)
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

