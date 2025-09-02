## dataos-ctl operate pulsar functions download

Download File Data from Pulsar

### Synopsis

USED FOR:
    This command is used for download File Data from Pulsar.

REQUIRED PERMISSION:
    This command requires super-user permissions.

OUTPUT:
    #normal output
    Downloaded <the name of a Pulsar Function> successfully

    #You must specify a name for the Pulsar Functions or a FQFN, please check the --name args
    [✖]  you must specify a name for the function or a Fully Qualified Function Name (FQFN)



```
dataos-ctl operate pulsar functions download [flags]
```

### Examples

```
    #Download File Data from Pulsar
    pulsarctl functions download 
	--destination-file public
	--path default


    #Download File Data from Pulsar
    pulsarctl functions download 
	--destination-file public
	--tenant public
	--namespace default
	--name <function-name>



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
      --destination-file string            The file to store downloaded content
      --fqfn string                        The Fully Qualified Function Name (FQFN) for the function
  -h, --help                               help for download
      --name string                        Function name
      --namespace string                   Namespace name
  -o, --output string                      The output format (text,json,yaml) (default "text")
      --path string                        Path to store the content
      --tenant string                      Tenant name
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

