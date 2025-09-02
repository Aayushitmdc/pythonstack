## dataos-ctl operate pulsar brokers update-dynamic-config

Update dynamic-serviceConfiguration of broker

### Synopsis

USED FOR:
    Update dynamic-serviceConfiguration of broker

REQUIRED PERMISSION:
    This command requires super-user permissions.

OUTPUT:
    #normal output
    Update dynamic config: (configName) successful.

    #Can't update non-dynamic configuration, please check `--config` arg.
    [✖]  code: 412 reason:  Can't update non-dynamic configuration



```
dataos-ctl operate pulsar brokers update-dynamic-config [flags]
```

### Examples

```
    #Update dynamic-serviceConfiguration of broker
    pulsarctl brokers update-dynamic-config --config (config name) --value (config value)


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
      --config string                      service-configuration name
  -h, --help                               help for update-dynamic-config
  -o, --output string                      The output format (text,json,yaml) (default "text")
      --tls-allow-insecure                 Allow TLS insecure connection
      --tls-cert-file string               File path for TLS cert used for authentication
      --tls-enable-hostname-verification   Enable TLS hostname verification
      --tls-key-file string                File path for TLS key used for authentication
      --tls-trust-cert-path string         Allow TLS trust cert file path
      --token string                       Using the token to authentication
      --token-file string                  Using the token file to authentication
      --value string                       service-configuration value
```

### Options inherited from parent commands

```
  -v, --verbose int   set log level, use 0 to silence, 4 for debugging (default 4)
```

### SEE ALSO

* [dataos-ctl operate pulsar brokers](dataos-ctl_operate_pulsar_brokers.md)	 - Operations about broker(s)

