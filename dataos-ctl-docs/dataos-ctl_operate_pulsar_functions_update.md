## dataos-ctl operate pulsar functions update

Update a Pulsar Function that has been deployed to a Pulsar cluster

### Synopsis

USED FOR:
    Update a Pulsar Function that has been deployed to a Pulsar cluster.

REQUIRED PERMISSION:
    This command requires super-user permissions.

OUTPUT:
    #normal output
    Updated (the name of a Pulsar Function) successfully

    #Update contains no change
    [✖]  code: 400 reason: Update contains no change

    #The name of Pulsar Functions doesn't exist, please check the --name args
    [✖]  code: 404 reason: Function (your function name) doesn't exist



```
dataos-ctl operate pulsar functions update [flags]
```

### Examples

```
    #Change the output topic of a Pulsar Function
    pulsarctl functions update 
	--tenant public 
	--namespace default 
	--name update-function 
	--output test-output-topic

    #Update a Pulsar Function using a function config yaml file
    pulsarctl functions update 
	--function-config-file (the path of function config yaml file) 
	--jar (the path of user code jar)

    #Change the log topic of a Pulsar Function
    pulsarctl functions update 
	--log-topic persistent://public/default/test-log-topic
	// Other function parameters 

    #Change the dead letter topic of a Pulsar Function
    pulsarctl functions update 
	--dead-letter-topic persistent://public/default/test-dead-letter-topic
	--max-message-retries 10
	// Other function parameters 

    #Update the user configs of a Pulsar Function
    pulsarctl functions update 
	--user-config "{"publishTopic":"publishTopic", "key":"pulsar"}"
	// Other function parameters 

    #Change the schemas of the input topics for a Pulsar Function
    pulsarctl functions update 
	--custom-schema-inputs "{"topic-1":"schema.STRING", "topic-2":"schema.JSON"}"
	// Other function parameters 

    #Change the schema type of the input topic for a Pulsar Function
    pulsarctl functions update 
	--schema-type schema.STRING
	// Other function parameters 

    #Change the parallelism of a Pulsar Function
    pulsarctl functions update 
	--parallelism 1
	// Other function parameters 

    #Change the resource usage for a Pulsar Function
    pulsarctl functions update 
	--ram 5656565656
	--disk 8080808080808080
	--cpu 5.0
	// Other function parameters 

    #Update the window configurations for a Pulsar Function
    pulsarctl functions update 
	--window-length-count 10
	--window-length-duration-ms 1000
	--sliding-interval-count 3
	--sliding-interval-duration-ms 1000
	// Other function parameters 


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
      --classname string                   The class name of a Pulsar Function
      --cpu float                          The cpu in cores that need to be allocated per function instance(applicable only to docker runtime)
      --custom-schema-inputs string        The map of input topics to Schema class names (as a JSON string)
      --custom-serde-inputs string         The map of input topics to SerDe class names (as a JSON string)
      --dead-letter-topic string           The topic where messages that are not processed successfully are sent to
      --disk int                           The disk in bytes that need to be allocated per function instance(applicable only to docker runtime)
      --fqfn string                        The Fully Qualified Function Name (FQFN) for the function
      --function-config-file string        The path to a YAML config file that specifies the configuration of a Pulsar Function
      --go string                          Path to the main Go executable binary for the function (if the function is written in Go)
  -h, --help                               help for update
      --inputs string                      The input topic or topics (multiple topics can be specified as a comma-separated list) of a Pulsar Function
      --jar string                         Path to the JAR file for the function (if the function is written in Java). It also supports URL path [http/https/file (file protocol assumes that file already exists on worker host)] from which worker can download the package.
      --log-topic string                   The topic to which the logs of a Pulsar Function are produced
      --max-message-retries int            How many times should we try to process a message before giving up
      --name string                        The name of a Pulsar Function
      --namespace string                   The namespace of a Pulsar Function
  -o, --output string                      The output topic of a Pulsar Function (If none is specified, no output is written)
      --output-serde-classname string      The SerDe class to be used for messages output by the function
      --parallelism int                    The parallelism factor of a Pulsar Function (i.e. the number of function instances to run)
      --py string                          Path to the main Python file/Python Wheel file for the function (if the function is written in Python)
      --ram int                            The ram in bytes that need to be allocated per function instance(applicable only to process/docker runtime)
  -t, --schema-type string                 The builtin schema type or custom schema class name to be used for messages output by the function
      --sliding-interval-count int         The number of messages after which the window slides
      --sliding-interval-duration-ms int   The time duration after which the window slides
      --tenant string                      The tenant of a Pulsar Function
      --timeout-ms int                     The message timeout in milliseconds
      --tls-allow-insecure                 Allow TLS insecure connection
      --tls-cert-file string               File path for TLS cert used for authentication
      --tls-enable-hostname-verification   Enable TLS hostname verification
      --tls-key-file string                File path for TLS key used for authentication
      --tls-trust-cert-path string         Allow TLS trust cert file path
      --token string                       Using the token to authentication
      --token-file string                  Using the token file to authentication
      --topics-pattern string              The topic pattern to consume from list of topics under a namespace that match the pattern. [--input] and [--topic-pattern] are mutually exclusive. Add SerDe class name for a pattern in --custom-serde-inputs (supported for java fun only)
      --update-auth-data                   Whether or not to update the auth data
      --user-config string                 User-defined config key/values
      --window-length-count int            The number of messages per window
      --window-length-duration-ms int      The time duration of the window in milliseconds
```

### Options inherited from parent commands

```
  -v, --verbose int   set log level, use 0 to silence, 4 for debugging (default 4)
```

### SEE ALSO

* [dataos-ctl operate pulsar functions](dataos-ctl_operate_pulsar_functions.md)	 - Interface for managing Pulsar Functions (lightweight, Lambda-style compute processes that work with Pulsar)

