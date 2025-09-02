## dataos-ctl operate pulsar context

Interface for setting Pulsar Context 

```
dataos-ctl operate pulsar context [flags]
```

### Options

```
  -h, --help   help for context
```

### Options inherited from parent commands

```
  -s, --admin-service-url string           The admin web service url that pulsarctl connects to. (default "http://localhost:8080")
      --auth-params string                 Authentication parameters are used to configure the authentication provider specified by "AuthPlugin".
                                            Tls example: "tlsCertFile:val1,tlsKeyFile:val2"
                                            Token example: "authParams=file:///path/to/token/file" or "authParams=token:tokenVal"
      --auth-plugin string                 AuthPlugin is used to specify the plugin to use for authentication,
                                            the supported values are "org.apache.pulsar.client.impl.auth.AuthenticationTls"
                                            and "org.apache.pulsar.client.impl.auth.AuthenticationToken"
      --bookie-service-url string          The bookie web service url that pulsarctl connects to.
      --tls-allow-insecure                 Allow TLS insecure connection
      --tls-cert-file string               File path for TLS cert used for authentication
      --tls-enable-hostname-verification   Enable TLS hostname verification
      --tls-key-file string                File path for TLS key used for authentication
      --tls-trust-cert-path string         Allow TLS trust cert file path
      --token string                       Using the token to authentication
      --token-file string                  Using the token file to authentication
  -v, --verbose int                        set log level, use 0 to silence, 4 for debugging (default 4)
```

### SEE ALSO

* [dataos-ctl operate pulsar](dataos-ctl_operate_pulsar.md)	 - Pulsar management
* [dataos-ctl operate pulsar context current](dataos-ctl_operate_pulsar_context_current.md)	 - Displays the current context
* [dataos-ctl operate pulsar context delete](dataos-ctl_operate_pulsar_context_delete.md)	 - delete context NAME
* [dataos-ctl operate pulsar context get](dataos-ctl_operate_pulsar_context_get.md)	 - Describe one or many contexts
* [dataos-ctl operate pulsar context rename](dataos-ctl_operate_pulsar_context_rename.md)	 - Renames a context from the pulsarconfig file.
* [dataos-ctl operate pulsar context set](dataos-ctl_operate_pulsar_context_set.md)	 - Sets a context entry in pulsarconfig
* [dataos-ctl operate pulsar context use](dataos-ctl_operate_pulsar_context_use.md)	 - use-context CONTEXT_NAME

