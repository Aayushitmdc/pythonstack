## dataos-ctl operate pulsar functions

Interface for managing Pulsar Functions (lightweight, Lambda-style compute processes that work with Pulsar)

```
dataos-ctl operate pulsar functions [flags]
```

### Options

```
  -h, --help   help for functions
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
* [dataos-ctl operate pulsar functions create](dataos-ctl_operate_pulsar_functions_create.md)	 - Create a Pulsar Function to run on a Pulsar cluster
* [dataos-ctl operate pulsar functions delete](dataos-ctl_operate_pulsar_functions_delete.md)	 - Delete a Pulsar Function that is running on a Pulsar cluster
* [dataos-ctl operate pulsar functions download](dataos-ctl_operate_pulsar_functions_download.md)	 - Download File Data from Pulsar
* [dataos-ctl operate pulsar functions get](dataos-ctl_operate_pulsar_functions_get.md)	 - Fetch information about a Pulsar Function
* [dataos-ctl operate pulsar functions list](dataos-ctl_operate_pulsar_functions_list.md)	 - List all Pulsar Functions running under a specific tenant and namespace
* [dataos-ctl operate pulsar functions putstate](dataos-ctl_operate_pulsar_functions_putstate.md)	 - Put a key/value pair to the state associated with a Pulsar Function
* [dataos-ctl operate pulsar functions querystate](dataos-ctl_operate_pulsar_functions_querystate.md)	 - Fetch a key/value pair from the state associated with a Pulsar Function
* [dataos-ctl operate pulsar functions restart](dataos-ctl_operate_pulsar_functions_restart.md)	 - Restart function instance
* [dataos-ctl operate pulsar functions start](dataos-ctl_operate_pulsar_functions_start.md)	 - Starts a stopped function instance
* [dataos-ctl operate pulsar functions stats](dataos-ctl_operate_pulsar_functions_stats.md)	 - Get the current stats of a Pulsar Function
* [dataos-ctl operate pulsar functions status](dataos-ctl_operate_pulsar_functions_status.md)	 - Check the current status of a Pulsar Function
* [dataos-ctl operate pulsar functions stop](dataos-ctl_operate_pulsar_functions_stop.md)	 - Stops function instance
* [dataos-ctl operate pulsar functions trigger](dataos-ctl_operate_pulsar_functions_trigger.md)	 - Trigger the specified Pulsar Function with a supplied value
* [dataos-ctl operate pulsar functions update](dataos-ctl_operate_pulsar_functions_update.md)	 - Update a Pulsar Function that has been deployed to a Pulsar cluster
* [dataos-ctl operate pulsar functions upload](dataos-ctl_operate_pulsar_functions_upload.md)	 - Upload a local file to Pulsar

