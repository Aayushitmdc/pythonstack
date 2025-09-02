## dataos-ctl operate pulsar clusters get-failure-domain

Get the failure domain

### Synopsis

USED FOR:
    This command is used for getting the specified failure domain on the specified cluster.

REQUIRED PERMISSION:
    This command requires super-user permissions.

OUTPUT:
    #output example
    {
      "brokers" : [
        "failure-broker-A",
        "failure-broker-B",
      ]
    }

    #the cluster name and(or) failure domain name is not specified or the name is specified more than one
    [✖]  need to specified the cluster name and the failure domain name

    #the specified cluster does not exist in the broker
    [✖]  code: 412 reason: Cluster (cluster-name) does not exist.



```
dataos-ctl operate pulsar clusters get-failure-domain [flags]
```

### Examples

```
    #getting the broker list in the (cluster-name) cluster failure domain (domain-name)
    pulsarctl clusters get-failure-domain (cluster-name) (domain-name)


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
  -h, --help                               help for get-failure-domain
  -o, --output string                      The output format (text,json,yaml) (default "text")
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

* [dataos-ctl operate pulsar clusters](dataos-ctl_operate_pulsar_clusters.md)	 - Operations about cluster(s)

