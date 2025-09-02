## dataos-ctl operate pulsar sinks create

Create a Pulsar IO sink connector to run in a Pulsar cluster

### Synopsis

USED FOR:
    Create a Pulsar IO sink connector to run in a Pulsar cluster.

REQUIRED PERMISSION:
    This command requires namespace function permissions.

OUTPUT:
    #normal output
    Created (the name of a Pulsar Sinks) successfully

    #sink archive not specified, please check --archive arg
    [✖]  Sink archive not specified

    #Cannot specify both archive and sink-type, please check --archive and --sink-type args
    [✖]  Cannot specify both archive and sink-type



```
dataos-ctl operate pulsar sinks create [flags]
```

### Examples

```
    #Create a Pulsar Sink in cluster mode
    pulsarctl sink create 
	--tenant public 
	--namespace default 
	--name (the name of Pulsar Sink) 
	--inputs test-jdbc  
	--archive connectors/pulsar-io-jdbc-2.4.0.nar 
	--sink-config-file connectors/mysql-jdbc-sink.yaml 
	--parallelism 1

    #Create a Pulsar Sink in cluster mode with pkg URL
    pulsarctl sink create 
	--tenant public 
	--namespace default 
	--name (the name of Pulsar Sink) 
	--inputs test-jdbc  
	--archive file:/http: + connectors/pulsar-io-jdbc-2.4.0.nar

    #Create a Pulsar Sink in cluster mode with schema type
    pulsarctl sink create 
	--schema-type schema.STRING
	// Other sink parameters 

    #Create a Pulsar Sink in cluster mode with parallelism
    pulsarctl sink create 
	--parallelism 1
	// Other sink parameters 

    #Create a Pulsar Sink in cluster mode with resource
    pulsarctl sink create 
	--ram 5656565656
	--disk 8080808080808080
	--cpu 5.0
	// Other sink parameters 

    #Create a Pulsar Sink in cluster mode with sink config
    pulsarctl sink create 
	--sink-config "{"publishTopic":"publishTopic", "key":"pulsar"}"
	// Other sink parameters 

    #Create a Pulsar Sink in cluster mode with processing guarantees
    pulsarctl sink create 
	--processing-guarantees EFFECTIVELY_ONCE
	// Other sink parameters 


```

### Options

```
  -s, --admin-service-url string           The admin web service url that pulsarctl connects to. (default "http://localhost:8080")
      --archive string                     Path to the archive file for the sink. It also supports url-path [http/https/file (file protocol assumes that file already exists on worker host)] from which worker can download the package.
      --auth-params string                 Authentication parameters are used to configure the authentication provider specified by "AuthPlugin".
                                            Tls example: "tlsCertFile:val1,tlsKeyFile:val2"
                                            Token example: "authParams=file:///path/to/token/file" or "authParams=token:tokenVal"
      --auth-plugin string                 AuthPlugin is used to specify the plugin to use for authentication,
                                            the supported values are "org.apache.pulsar.client.impl.auth.AuthenticationTls"
                                            and "org.apache.pulsar.client.impl.auth.AuthenticationToken"
      --auto-ack                           Whether or not the framework will automatically acknowledge messages
      --bookie-service-url string          The bookie web service url that pulsarctl connects to.
      --classname string                   The sink's class name if archive is file-url-path (file://)
      --cpu float                          The CPU (in cores) that needs to be allocated per sink instance (applicable only to Docker runtime)
      --custom-schema-inputs string        The map of input topics to Schema types or class names (as a JSON string)
      --custom-serde-inputs string         The map of input topics to SerDe class names (as a JSON string)
      --disk int                           The disk (in bytes) that need to be allocated per sink instance (applicable only to Docker runtime)
  -h, --help                               help for create
  -i, --inputs string                      The sink's input topic or topics (multiple topics can be specified as a comma-separated list)
      --name string                        The sink's name
      --namespace string                   The sink's namespace
  -o, --output string                      The output format (text,json,yaml) (default "text")
      --parallelism int                    The sink's parallelism factor (i.e. the number of sink instances to run)
      --processing-guarantees string       The processing guarantees (aka delivery semantics) applied to the sink
      --ram int                            The RAM (in bytes) that need to be allocated per sink instance (applicable only to the process and Docker runtimes)
      --retain-ordering                    Sink consumes and sinks messages in order
      --sink-config string                 User defined configs key/values
      --sink-config-file string            The path to a YAML config file specifying the sink's configuration
  -t, --sink-type string                   The sink's connector provider
      --subs-name string                   Pulsar source subscription name if user wants a specific subscription-name for input-topic consumer
      --subs-position string               Pulsar source subscription position if user wants to consume messages from the specified location. Possible Values: [Latest, Earliest]
      --tenant string                      The sink's tenant
      --timeout-ms int                     The message timeout in milliseconds
      --tls-allow-insecure                 Allow TLS insecure connection
      --tls-cert-file string               File path for TLS cert used for authentication
      --tls-enable-hostname-verification   Enable TLS hostname verification
      --tls-key-file string                File path for TLS key used for authentication
      --tls-trust-cert-path string         Allow TLS trust cert file path
      --token string                       Using the token to authentication
      --token-file string                  Using the token file to authentication
      --topics-pattern string              TopicsPattern to consume from list of topics under a namespace that match the pattern. [--input] and [--topicsPattern] are mutually exclusive. Add SerDe class name for a pattern in --customSerdeInputs  (supported for java fun only)
```

### Options inherited from parent commands

```
  -v, --verbose int   set log level, use 0 to silence, 4 for debugging (default 4)
```

### SEE ALSO

* [dataos-ctl operate pulsar sinks](dataos-ctl_operate_pulsar_sinks.md)	 - Interface for managing Pulsar IO sinks (egress data from Pulsar)

