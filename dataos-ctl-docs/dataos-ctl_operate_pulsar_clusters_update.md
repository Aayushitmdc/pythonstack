## dataos-ctl operate pulsar clusters update

Update a pulsar cluster

### Synopsis

USED FOR:
    This command is used for updating the cluster data of the specified cluster.

REQUIRED PERMISSION:
    This command requires super-user permissions.

OUTPUT:
    #normal output
    Cluster (cluster-name) updated

    #the cluster name is not specified or the cluster name is specified more than one
    [✖]  the cluster name is not specified or the cluster name is specified more than one

    #the specified cluster does not exist in the broker
    [✖]  code: 412 reason: Cluster (cluster-name) does not exist.



```
dataos-ctl operate pulsar clusters update [flags]
```

### Examples

```
    #updating the web service url of the (cluster-name)
    pulsarctl clusters update --url http://example:8080 (cluster-name)

    #updating the tls secured web service url of the (cluster-name)
    pulsarctl clusters update --url-tls https://example:8080 (cluster-name)

    #updating the broker service url of the (cluster-name)
    pulsarctl clusters update --broker-url pulsar://example:6650 (cluster-name)

    #updating the tls secured web service url of the (cluster-name)
    pulsarctl clusters update --broker-url-tls pulsar+ssl://example:6650 (cluster-name)

    #registered as a peer-cluster of the (cluster-name) clusters
    pulsarctl clusters update -p (cluster-a) -p (cluster-b) (cluster)


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
      --broker-url string                  Pulsar cluster broker service url, e.g. pulsar://example.pulsar.io:6650
      --broker-url-tls string              Pulsar cluster tls secured broker service url, e.g. pulsar+ssl://example.pulsar.io:6651
  -h, --help                               help for update
  -o, --output string                      The output format (text,json,yaml) (default "text")
  -p, --peer-cluster strings               Cluster to be registered as a peer-cluster of this cluster.
      --tls-allow-insecure                 Allow TLS insecure connection
      --tls-cert-file string               File path for TLS cert used for authentication
      --tls-enable-hostname-verification   Enable TLS hostname verification
      --tls-key-file string                File path for TLS key used for authentication
      --tls-trust-cert-path string         Allow TLS trust cert file path
      --token string                       Using the token to authentication
      --token-file string                  Using the token file to authentication
      --url string                         Pulsar cluster web service url, e.g. http://example.pulsar.io:8080
      --url-tls string                     Pulsar cluster tls secured web service url, e.g. https://example.pulsar.io:8443
```

### Options inherited from parent commands

```
  -v, --verbose int   set log level, use 0 to silence, 4 for debugging (default 4)
```

### SEE ALSO

* [dataos-ctl operate pulsar clusters](dataos-ctl_operate_pulsar_clusters.md)	 - Operations about cluster(s)

