## dataos-ctl operate pulsar brokers get-internal-config

Get internal configuration information

### Synopsis

USED FOR:
    Get internal configuration information

REQUIRED PERMISSION:
    This command requires super-user permissions.

OUTPUT:
    #normal output
    {
      "zookeeperServers": "127.0.0.1:2181",
      "configurationStoreServers": "127.0.0.1:2181",
      "ledgersRootPath": "/ledgers",
      "stateStorageServiceUrl": "bk://127.0.0.1:4181"
    }



```
dataos-ctl operate pulsar brokers get-internal-config [flags]
```

### Examples

```
    #Get internal configuration information
    pulsarctl brokers get-internal-config


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
  -h, --help                               help for get-internal-config
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

* [dataos-ctl operate pulsar brokers](dataos-ctl_operate_pulsar_brokers.md)	 - Operations about broker(s)

