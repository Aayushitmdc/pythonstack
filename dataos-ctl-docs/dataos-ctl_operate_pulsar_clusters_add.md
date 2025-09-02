## dataos-ctl operate pulsar clusters add

Add a pulsar cluster

### Synopsis

USED FOR:
    This command is used for adding the configuration data for a cluster. The configuration data is mainly used for geo-replication between clusters, so please make sure the service urls provided in this command are reachable between clusters. This operation requires Pulsar super-user privileges.

REQUIRED PERMISSION:
    This command requires super-user permissions.

OUTPUT:
    #normal output
    Cluster (cluster-name) added



```
dataos-ctl operate pulsar clusters add [flags]
```

### Examples

```
    #Provisions a new cluster
    pulsarctl clusters create (cluster-name)


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
  -h, --help                               help for add
  -o, --output string                      The output format (text,json,yaml) (default "text")
  -p, --peer-cluster stringArray           Cluster to be registered as a peer-cluster of this cluster.
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

