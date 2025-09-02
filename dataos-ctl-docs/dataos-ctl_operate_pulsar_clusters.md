## dataos-ctl operate pulsar clusters

Operations about cluster(s)

```
dataos-ctl operate pulsar clusters [flags]
```

### Options

```
  -h, --help   help for clusters
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
* [dataos-ctl operate pulsar clusters add](dataos-ctl_operate_pulsar_clusters_add.md)	 - Add a pulsar cluster
* [dataos-ctl operate pulsar clusters create-failure-domain](dataos-ctl_operate_pulsar_clusters_create-failure-domain.md)	 - Create a failure domain
* [dataos-ctl operate pulsar clusters delete](dataos-ctl_operate_pulsar_clusters_delete.md)	 - Delete an existing cluster
* [dataos-ctl operate pulsar clusters delete-failure-domain](dataos-ctl_operate_pulsar_clusters_delete-failure-domain.md)	 - Delete a failure domain
* [dataos-ctl operate pulsar clusters get](dataos-ctl_operate_pulsar_clusters_get.md)	 - Get the configuration data for the specified cluster
* [dataos-ctl operate pulsar clusters get-failure-domain](dataos-ctl_operate_pulsar_clusters_get-failure-domain.md)	 - Get the failure domain
* [dataos-ctl operate pulsar clusters get-peer-clusters](dataos-ctl_operate_pulsar_clusters_get-peer-clusters.md)	 - Getting list of peer clusters
* [dataos-ctl operate pulsar clusters list](dataos-ctl_operate_pulsar_clusters_list.md)	 - List the available pulsar clusters
* [dataos-ctl operate pulsar clusters list-failure-domains](dataos-ctl_operate_pulsar_clusters_list-failure-domains.md)	 - List the existing failure domains for a cluster
* [dataos-ctl operate pulsar clusters update](dataos-ctl_operate_pulsar_clusters_update.md)	 - Update a pulsar cluster
* [dataos-ctl operate pulsar clusters update-failure-domain](dataos-ctl_operate_pulsar_clusters_update-failure-domain.md)	 - Update a failure domain
* [dataos-ctl operate pulsar clusters update-peer-clusters](dataos-ctl_operate_pulsar_clusters_update-peer-clusters.md)	 - Update the peer clusters

