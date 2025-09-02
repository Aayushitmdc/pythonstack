## dataos-ctl operate pulsar namespaces set-persistence

Set the persistence policy for a namespace

### Synopsis

USED FOR:
    Set the persistence policy for a namespace

REQUIRED PERMISSION:
    This command requires tenant admin permissions.

OUTPUT:
    #normal output
    Set the persistence policies successfully for [tenant/namespace]

    #you must specify a tenant/namespace name, please check if the tenant/namespace name is provided
    [✖]  the namespace name is not specified or the namespace name is specified more than one

    #the tenant does not exist
    [✖]  code: 404 reason: Tenant does not exist

    #the namespace does not exist
    [✖]  code: 404 reason: Namespace (tenant/namespace) does not exist

    #Bookkeeper Ensemble >= WriteQuorum >= AckQuoru, please c 
    code: 412 reason: Bookkeeper Ensemble >= WriteQuorum >= AckQuoru



```
dataos-ctl operate pulsar namespaces set-persistence [flags]
```

### Examples

```
    #Set the persistence policy for a namespace
    pulsarctl namespaces set-persistence tenant/namespace 
	--ensemble-size 2 
	--write-quorum-size 2 
	--ack-quorum-size 2 
	--ml-mark-delete-max-rate 2.0


```

### Options

```
  -a, --ack-quorum-size int                Number of acks (guaranteed copies) to wait for each entry
  -s, --admin-service-url string           The admin web service url that pulsarctl connects to. (default "http://localhost:8080")
      --auth-params string                 Authentication parameters are used to configure the authentication provider specified by "AuthPlugin".
                                            Tls example: "tlsCertFile:val1,tlsKeyFile:val2"
                                            Token example: "authParams=file:///path/to/token/file" or "authParams=token:tokenVal"
      --auth-plugin string                 AuthPlugin is used to specify the plugin to use for authentication,
                                            the supported values are "org.apache.pulsar.client.impl.auth.AuthenticationTls"
                                            and "org.apache.pulsar.client.impl.auth.AuthenticationToken"
      --bookie-service-url string          The bookie web service url that pulsarctl connects to.
  -e, --ensemble-size int                  Number of bookies to use for a topic
  -h, --help                               help for set-persistence
  -r, --ml-mark-delete-max-rate float      Throttling rate of mark-delete operation (0 means no throttle)
  -o, --output string                      The output format (text,json,yaml) (default "text")
      --tls-allow-insecure                 Allow TLS insecure connection
      --tls-cert-file string               File path for TLS cert used for authentication
      --tls-enable-hostname-verification   Enable TLS hostname verification
      --tls-key-file string                File path for TLS key used for authentication
      --tls-trust-cert-path string         Allow TLS trust cert file path
      --token string                       Using the token to authentication
      --token-file string                  Using the token file to authentication
  -w, --write-quorum-size int              How many writes to make of each entry
```

### Options inherited from parent commands

```
  -v, --verbose int   set log level, use 0 to silence, 4 for debugging (default 4)
```

### SEE ALSO

* [dataos-ctl operate pulsar namespaces](dataos-ctl_operate_pulsar_namespaces.md)	 - Operations about namespaces

