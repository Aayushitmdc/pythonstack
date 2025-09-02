## dataos-ctl operate pulsar sources get

Gets the information about a Pulsar IO source connector

### Synopsis

USED FOR:
    Gets the information about a Pulsar IO source connector

REQUIRED PERMISSION:
    This command requires namespace function permissions.

OUTPUT:
    #normal output
    {
      "tenant": "public",
      "namespace": "default",
      "name": "kafka",
      "className": "org.apache.pulsar.io.kafka.KafkaBytesSource",
      "topicName": "my-topic",
      "configs": {
        "bootstrapServers": "pulsar-kafka:9092",
        "groupId": "test-pulsar-io1",
        "topic": "my-topic",
        "sessionTimeoutMs": "10000",
        "autoCommitEnabled": "false"
      },
      "parallelism": 1,
      "processingGuarantees": "ATLEAST_ONCE"
    }
    

    #source doesn't exist
    code: 404 reason: Source (the name of a Pulsar Source) doesn't exist



```
dataos-ctl operate pulsar sources get [flags]
```

### Examples

```
    #Gets the information about a Pulsar IO source connector
    pulsarctl source get 
	--tenant public
	--namespace default 
	--name (the name of Pulsar Source)


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
  -h, --help                               help for get
      --name string                        The source's name
      --namespace string                   The source's namespace
  -o, --output string                      The output format (text,json,yaml) (default "text")
      --tenant string                      The source's tenant
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

* [dataos-ctl operate pulsar sources](dataos-ctl_operate_pulsar_sources.md)	 - Interface for managing Pulsar IO Sources (ingress data into Pulsar)

