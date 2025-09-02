## dataos-ctl operate pulsar ns-isolation-policy brokers

List all brokers with namespace-isolation policies attached to it

### Synopsis

USED FOR:
    List all brokers with namespace-isolation policies attached to it.

REQUIRED PERMISSION:
    This command requires super-user permissions.

OUTPUT:
    #normal output
    [
      {
        "brokerName": "127.0.0.1:8080",
        "policyName": "",
        "isPrimary": false,
        "namespaceRegex": null
      }
    ]

    #Reason: Cluster name does not exist, please check cluster name.
    Reason: Cluster name does not exist.

    #need to specified the cluster name and the policy name, please add cluster name and policy name
    need to specified the cluster name and the policy name

    #namespace-isolation policies not found for standalone
    [✖]  code: 404 reason: namespace-isolation policies not found for standalone



```
dataos-ctl operate pulsar ns-isolation-policy brokers [flags]
```

### Examples

```
    #List all brokers with namespace-isolation policies attached to it
    pulsarctl ns-isolation-policy brokers (cluster-name)


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
  -h, --help                               help for brokers
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

* [dataos-ctl operate pulsar ns-isolation-policy](dataos-ctl_operate_pulsar_ns-isolation-policy.md)	 - Operations about namespace isolation policy

