## dataos-ctl operate pulsar schemas get

Get the schema for a topic

### Synopsis

USED FOR:
    Get the schema for a topic.

REQUIRED PERMISSION:
    This command requires namespace admin permissions.

OUTPUT:
    #normal output
    {
      "name": "test-schema",
      "schema": {
        "type": "record",
        "name": "Test",
        "fields": [
          {
            "name": "id",
            "type": [
              "null",
              "int"
            ]
          },
          {
            "name": "name",
            "type": [
              "null",
              "string"
            ]
          }
        ]
      },
      "type": "AVRO",
      "properties": {}
    }

    #HTTP 404 Not Found, please check if the topic name you entered is correct
    [✖]  code: 404 reason: Not Found

    #you must specify a topic name, please check if the topic name is provided
    [✖]  the topic name is not specified or the topic name is specified more than one



```
dataos-ctl operate pulsar schemas get [flags]
```

### Examples

```
    #Get the schema for a topic
    pulsarctl schemas get (topic name)

    #Get the schema for a topic with version
    pulsarctl schemas get (topic name) 
	--version 2


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
  -h, --help                               help for get
  -o, --output string                      The output format (text,json,yaml) (default "text")
      --tls-allow-insecure                 Allow TLS insecure connection
      --tls-cert-file string               File path for TLS cert used for authentication
      --tls-enable-hostname-verification   Enable TLS hostname verification
      --tls-key-file string                File path for TLS key used for authentication
      --tls-trust-cert-path string         Allow TLS trust cert file path
      --token string                       Using the token to authentication
      --token-file string                  Using the token file to authentication
      --version int                        the schema version info
```

### Options inherited from parent commands

```
  -v, --verbose int   set log level, use 0 to silence, 4 for debugging (default 4)
```

### SEE ALSO

* [dataos-ctl operate pulsar schemas](dataos-ctl_operate_pulsar_schemas.md)	 - Operations related to Schemas associated with Pulsar topics

