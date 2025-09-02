## dataos-ctl operate pulsar functions start

Starts a stopped function instance

### Synopsis

USED FOR:
    This command is used for starting a stopped function instance.

REQUIRED PERMISSION:
    This command requires super-user permissions.

OUTPUT:
    #normal output
    Started <the name of a Pulsar Function> successfully

    #You must specify a name for the Pulsar Functions or a FQFN, please check the --name args
    [✖]  you must specify a name for the function or a Fully Qualified Function Name (FQFN)

    #The name of Pulsar Functions doesn't exist, please check the --name args
    [✖]  code: 404 reason: Function <your function name> doesn't exist

    #Used an instanceID that does not exist or other impermissible actions
    [✖]  code: 400 reason: Operation not permitted



```
dataos-ctl operate pulsar functions start [flags]
```

### Examples

```
    #Starts a stopped function instance
    pulsarctl functions start 
	--tenant public
	--namespace default
	--name (the name of Pulsar Function)

    #Starts a stopped function instance with instance ID
    pulsarctl functions start 
	--tenant public
	--namespace default
	--name (the name of Pulsar Function)
	--instance-id 1

    #Starts a stopped function instance with FQFN
    pulsarctl functions start 
	--fqfn tenant/namespace/name [eg: public/default/ExampleFunctions]


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
      --fqfn string                        The Fully Qualified Function Name (FQFN) for the function
  -h, --help                               help for start
      --instance-id string                 The function instanceId (start all instances if instance-id is not provided)
      --name string                        The name of a Pulsar Function
      --namespace string                   The namespace of a Pulsar Function
  -o, --output string                      The output format (text,json,yaml) (default "text")
      --tenant string                      The tenant of a Pulsar Function
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

* [dataos-ctl operate pulsar functions](dataos-ctl_operate_pulsar_functions.md)	 - Interface for managing Pulsar Functions (lightweight, Lambda-style compute processes that work with Pulsar)

