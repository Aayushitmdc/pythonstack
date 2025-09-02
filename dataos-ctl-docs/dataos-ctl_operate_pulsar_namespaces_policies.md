## dataos-ctl operate pulsar namespaces policies

Get the configuration policies of a namespace

### Synopsis

USED FOR:
    Get the configuration policies of a namespace

REQUIRED PERMISSION:
    This command requires tenant admin permissions.

OUTPUT:
    #normal output
    {
      "AuthPolicies": {},
      "ReplicationClusters": null,
      "Bundles": {
        "boundaries": [
          "0x00000000",
          "0x40000000",
          "0x80000000",
          "0xc0000000",
          "0xffffffff"
        ],
        "numBundles": 4
      },
      "BacklogQuotaMap": null,
      "TopicDispatchRate": {
        "standalone": {
          "DispatchThrottlingRateInMsg": 0,
          "DispatchThrottlingRateInByte": 0,
          "RatePeriodInSecond": 1
        }
      },
      "SubscriptionDispatchRate": {
        "standalone": {
          "DispatchThrottlingRateInMsg": 0,
          "DispatchThrottlingRateInByte": 0,
          "RatePeriodInSecond": 1
        }
      },
      "ClusterSubscribeRate": {
        "standalone": {
          "SubscribeThrottlingRatePerConsumer": 0,
          "RatePeriodInSecond": 30
        }
      },
      "Persistence": {
        "BookkeeperEnsemble": 0,
        "BookkeeperWriteQuorum": 0,
        "BookkeeperAckQuorum": 0,
        "ManagedLedgerMaxMarkDeleteRate": 0
      },
      "DeduplicationEnabled": false,
      "LatencyStatsSampleRate": null,
      "MessageTTLInSeconds": 0,
      "RetentionPolicies": {
        "RetentionTimeInMinutes": 0,
        "RetentionSizeInMB": 0
      },
      "Deleted": false,
      "AntiAffinityGroup": "",
      "EncryptionRequired": false,
      "SubscriptionAuthMode": "",
      "MaxProducersPerTopic": 0,
      "MaxConsumersPerTopic": 0,
      "MaxConsumersPerSubscription": 0,
      "CompactionThreshold": 0,
      "OffloadThreshold": 0,
      "OffloadDeletionLagMs": 0,
      "SchemaCompatibilityStrategy": "",
      "SchemaValidationEnforced": false
    }

    #you must specify a tenant/namespace name, please check if the tenant/namespace name is provided
    [✖]  the namespace name is not specified or the namespace name is specified more than one

    #the tenant does not exist
    [✖]  code: 404 reason: Tenant does not exist

    #the namespace does not exist
    [✖]  code: 404 reason: Namespace (tenant/namespace) does not exist



```
dataos-ctl operate pulsar namespaces policies [flags]
```

### Examples

```
    #Get the configuration policies of a namespace
    pulsarctl namespaces policies (tenant/namespace)


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
  -h, --help                               help for policies
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

* [dataos-ctl operate pulsar namespaces](dataos-ctl_operate_pulsar_namespaces.md)	 - Operations about namespaces

