## dataos-ctl operate pulsar sources update

Update a Pulsar IO source connector

### Synopsis

USED FOR:
    Update a Pulsar IO source connector.

REQUIRED PERMISSION:
    This command requires namespace function permissions.

OUTPUT:
    #normal output
    Updated (the name of a Pulsar Source) successfully

    #source doesn't exist
    code: 404 reason: Source (the name of a Pulsar Source) doesn't exist



```
dataos-ctl operate pulsar sources update [flags]
```

### Examples

```
    #Update a Pulsar IO source connector
    pulsarctl source update 
	--tenant public 
	--namespace default 
	--name update-source 
	--archive pulsar-io-kafka-2.4.0.nar 
	--classname org.apache.pulsar.io.kafka.KafkaBytesSource 
	--destination-topic-name my-topic 
	--cpu 2

    #Update a Pulsar IO source connector with source config
    pulsarctl source create 
	--source-config "{"publishTopic":"publishTopic", "key":"pulsar"}"
	// Other source parameters 

    #Update a Pulsar IO source connector with resource
    pulsarctl source create 
	--ram 5656565656
	--disk 8080808080808080
	--cpu 5.0
	// Other source parameters 

    #Update a Pulsar IO source connector with parallelism
    pulsarctl source create 
	--parallelism 1
	// Other source parameters 

    #Update a Pulsar IO source connector with schema type
    pulsarctl source create 
	--schema-type schema.STRING
	// Other source parameters 


```

### Options

```
  -s, --admin-service-url string           The admin web service url that pulsarctl connects to. (default "http://localhost:8080")
  -a, --archive string                     The path to the NAR archive for the Source. It also supports url-path [http/https/file (file protocol assumes that file already exists on worker host)] from which worker can download the package
      --auth-params string                 Authentication parameters are used to configure the authentication provider specified by "AuthPlugin".
                                            Tls example: "tlsCertFile:val1,tlsKeyFile:val2"
                                            Token example: "authParams=file:///path/to/token/file" or "authParams=token:tokenVal"
      --auth-plugin string                 AuthPlugin is used to specify the plugin to use for authentication,
                                            the supported values are "org.apache.pulsar.client.impl.auth.AuthenticationTls"
                                            and "org.apache.pulsar.client.impl.auth.AuthenticationToken"
      --bookie-service-url string          The bookie web service url that pulsarctl connects to.
      --className string                   The source's class name if archive is file-url-path (file://)
      --cpu float                          The CPU (in cores) that needs to be allocated per source instance (applicable only to Docker runtime)
      --deserialization-classname string   The SerDe classname for the source
      --destination-topic-name string      The Pulsar topic to which data is sent
      --disk int                           The disk (in bytes) that need to be allocated per source instance (applicable only to Docker runtime)
  -h, --help                               help for update
      --name string                        The source's name
      --namespace string                   The source's namespace
      --parallelism int                    The source's parallelism factor (i.e. the number of source instances to run)
      --processing-guarantees string       The processing guarantees (aka delivery semantics) applied to the source
      --ram int                            The RAM (in bytes) that need to be allocated per source instance (applicable only to the process and Docker runtimes)
      --schema-type string                 The schema type (either a builtin schema like 'avro', 'json', etc.. or custom Schema class name to be used to encode messages emitted from the source
      --source-config string               Source config key/values
      --source-config-file string          he path to a YAML config file specifying the 
  -t, --source-type string                 The source's connector provider
      --tenant string                      The source's tenant
      --tls-allow-insecure                 Allow TLS insecure connection
      --tls-cert-file string               File path for TLS cert used for authentication
      --tls-enable-hostname-verification   Enable TLS hostname verification
      --tls-key-file string                File path for TLS key used for authentication
      --tls-trust-cert-path string         Allow TLS trust cert file path
      --token string                       Using the token to authentication
      --token-file string                  Using the token file to authentication
      --update-auth-data                   Whether or not to update the auth data
```

### Options inherited from parent commands

```
  -v, --verbose int   set log level, use 0 to silence, 4 for debugging (default 4)
```

### SEE ALSO

* [dataos-ctl operate pulsar sources](dataos-ctl_operate_pulsar_sources.md)	 - Interface for managing Pulsar IO Sources (ingress data into Pulsar)

