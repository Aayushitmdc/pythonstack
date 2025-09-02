## dataos-ctl operate pulsar namespaces

Operations about namespaces

```
dataos-ctl operate pulsar namespaces [flags]
```

### Options

```
  -h, --help   help for namespaces
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
* [dataos-ctl operate pulsar namespaces clear-backlog](dataos-ctl_operate_pulsar_namespaces_clear-backlog.md)	 - Clear backlog for all topics of a namespace
* [dataos-ctl operate pulsar namespaces clear-offload-deletion-lag](dataos-ctl_operate_pulsar_namespaces_clear-offload-deletion-lag.md)	 - Clear offload deletion lag of a namespace
* [dataos-ctl operate pulsar namespaces create](dataos-ctl_operate_pulsar_namespaces_create.md)	 - Create a new namespace
* [dataos-ctl operate pulsar namespaces delete](dataos-ctl_operate_pulsar_namespaces_delete.md)	 - Delete a namespace. The namespace needs to be empty
* [dataos-ctl operate pulsar namespaces delete-anti-affinity-group](dataos-ctl_operate_pulsar_namespaces_delete-anti-affinity-group.md)	 - Delete an anti-affinity group of a namespace
* [dataos-ctl operate pulsar namespaces get-anti-affinity-group](dataos-ctl_operate_pulsar_namespaces_get-anti-affinity-group.md)	 - Get the anti-affinity group of a namespace
* [dataos-ctl operate pulsar namespaces get-anti-affinity-namespaces](dataos-ctl_operate_pulsar_namespaces_get-anti-affinity-namespaces.md)	 - Get the list of namespaces in the same anti-affinity group.
* [dataos-ctl operate pulsar namespaces get-backlog-quotas](dataos-ctl_operate_pulsar_namespaces_get-backlog-quotas.md)	 - Get the backlog quota policy of a namespace
* [dataos-ctl operate pulsar namespaces get-clusters](dataos-ctl_operate_pulsar_namespaces_get-clusters.md)	 - Get the replicated clusters of a namespace
* [dataos-ctl operate pulsar namespaces get-compaction-threshold](dataos-ctl_operate_pulsar_namespaces_get-compaction-threshold.md)	 - Get compaction threshold of a namespace
* [dataos-ctl operate pulsar namespaces get-dispatch-rate](dataos-ctl_operate_pulsar_namespaces_get-dispatch-rate.md)	 - Get the default message dispatch rate of a namespace
* [dataos-ctl operate pulsar namespaces get-max-consumers-per-subscription](dataos-ctl_operate_pulsar_namespaces_get-max-consumers-per-subscription.md)	 - Get the max consumers per subscription of a namespace
* [dataos-ctl operate pulsar namespaces get-max-consumers-per-topic](dataos-ctl_operate_pulsar_namespaces_get-max-consumers-per-topic.md)	 - Get the max consumers per topic of a namespace
* [dataos-ctl operate pulsar namespaces get-max-producers-per-topic](dataos-ctl_operate_pulsar_namespaces_get-max-producers-per-topic.md)	 - Get the max producers per topic of namespace
* [dataos-ctl operate pulsar namespaces get-message-ttl](dataos-ctl_operate_pulsar_namespaces_get-message-ttl.md)	 - Get message TTL settings of a namespace
* [dataos-ctl operate pulsar namespaces get-offload-deletion-lag](dataos-ctl_operate_pulsar_namespaces_get-offload-deletion-lag.md)	 - Get the offload deletion lag of a namespace
* [dataos-ctl operate pulsar namespaces get-offload-threshold](dataos-ctl_operate_pulsar_namespaces_get-offload-threshold.md)	 - Get the offload threshold of a namespace
* [dataos-ctl operate pulsar namespaces get-persistence](dataos-ctl_operate_pulsar_namespaces_get-persistence.md)	 - Get the persistence policy of a namespace
* [dataos-ctl operate pulsar namespaces get-publish-rate](dataos-ctl_operate_pulsar_namespaces_get-publish-rate.md)	 - Get the default message publish rate of a namespace
* [dataos-ctl operate pulsar namespaces get-replicator-dispatch-rate](dataos-ctl_operate_pulsar_namespaces_get-replicator-dispatch-rate.md)	 - Get the default replicator message dispatch rate of a namespace
* [dataos-ctl operate pulsar namespaces get-retention](dataos-ctl_operate_pulsar_namespaces_get-retention.md)	 - Get the retention policy of a namespace
* [dataos-ctl operate pulsar namespaces get-schema-autoupdate-strategy](dataos-ctl_operate_pulsar_namespaces_get-schema-autoupdate-strategy.md)	 - Get the schema auto-update strategy of a namespace
* [dataos-ctl operate pulsar namespaces get-schema-validation-enforced](dataos-ctl_operate_pulsar_namespaces_get-schema-validation-enforced.md)	 - Enable/Disable schema validation enforced
* [dataos-ctl operate pulsar namespaces get-subscribe-rate](dataos-ctl_operate_pulsar_namespaces_get-subscribe-rate.md)	 - Get the default subscribe rate per consumer of a namespace
* [dataos-ctl operate pulsar namespaces get-subscription-dispatch-rate](dataos-ctl_operate_pulsar_namespaces_get-subscription-dispatch-rate.md)	 - Get the default subscription message dispatch rate of a namespace
* [dataos-ctl operate pulsar namespaces grant-permission](dataos-ctl_operate_pulsar_namespaces_grant-permission.md)	 - Grant permissions to a client role to access a namespace
* [dataos-ctl operate pulsar namespaces grant-subscription-permission](dataos-ctl_operate_pulsar_namespaces_grant-subscription-permission.md)	 - Grant a client role to access a subscription of a namespace
* [dataos-ctl operate pulsar namespaces list](dataos-ctl_operate_pulsar_namespaces_list.md)	 - Get the list of namespaces of a tenant
* [dataos-ctl operate pulsar namespaces messages-encryption](dataos-ctl_operate_pulsar_namespaces_messages-encryption.md)	 - Enable or disable messages encryption of a namespace
* [dataos-ctl operate pulsar namespaces permissions](dataos-ctl_operate_pulsar_namespaces_permissions.md)	 - Get permissions configure data of a namespace
* [dataos-ctl operate pulsar namespaces policies](dataos-ctl_operate_pulsar_namespaces_policies.md)	 - Get the configuration policies of a namespace
* [dataos-ctl operate pulsar namespaces remove-backlog-quota](dataos-ctl_operate_pulsar_namespaces_remove-backlog-quota.md)	 - Remove a backlog quota policy from a namespace
* [dataos-ctl operate pulsar namespaces remove-topic-auto-creation](dataos-ctl_operate_pulsar_namespaces_remove-topic-auto-creation.md)	 - Remove topic auto-creation for a namespace
* [dataos-ctl operate pulsar namespaces revoke-permission](dataos-ctl_operate_pulsar_namespaces_revoke-permission.md)	 - Revoke a client role permissions of accessing a namespace
* [dataos-ctl operate pulsar namespaces revoke-subscription-permission](dataos-ctl_operate_pulsar_namespaces_revoke-subscription-permission.md)	 - Revoke a client role permissions of accessing a subscription of a namespace
* [dataos-ctl operate pulsar namespaces set-anti-affinity-group](dataos-ctl_operate_pulsar_namespaces_set-anti-affinity-group.md)	 - Set the anti-affinity group for a namespace
* [dataos-ctl operate pulsar namespaces set-backlog-quota](dataos-ctl_operate_pulsar_namespaces_set-backlog-quota.md)	 - Set a backlog quota policy for a namespace
* [dataos-ctl operate pulsar namespaces set-clusters](dataos-ctl_operate_pulsar_namespaces_set-clusters.md)	 - Set the replicated clusters for a namespace
* [dataos-ctl operate pulsar namespaces set-compaction-threshold](dataos-ctl_operate_pulsar_namespaces_set-compaction-threshold.md)	 - Set compaction threshold for a namespace
* [dataos-ctl operate pulsar namespaces set-deduplication](dataos-ctl_operate_pulsar_namespaces_set-deduplication.md)	 - Enable or disable deduplication for a namespace
* [dataos-ctl operate pulsar namespaces set-dispatch-rate](dataos-ctl_operate_pulsar_namespaces_set-dispatch-rate.md)	 - Set the default message dispatch rate of a namespace
* [dataos-ctl operate pulsar namespaces set-max-consumers-per-subscription](dataos-ctl_operate_pulsar_namespaces_set-max-consumers-per-subscription.md)	 - Set the max consumers per subscription of a namespace
* [dataos-ctl operate pulsar namespaces set-max-consumers-per-topic](dataos-ctl_operate_pulsar_namespaces_set-max-consumers-per-topic.md)	 - Set the max consumers per topic of a namespace
* [dataos-ctl operate pulsar namespaces set-max-producers-per-topic](dataos-ctl_operate_pulsar_namespaces_set-max-producers-per-topic.md)	 - Set max producers per topic of namespace
* [dataos-ctl operate pulsar namespaces set-message-ttl](dataos-ctl_operate_pulsar_namespaces_set-message-ttl.md)	 - Set Message TTL for a namespace
* [dataos-ctl operate pulsar namespaces set-offload-deletion-lag](dataos-ctl_operate_pulsar_namespaces_set-offload-deletion-lag.md)	 - Set the offload deletion lag of a namespace
* [dataos-ctl operate pulsar namespaces set-offload-threshold](dataos-ctl_operate_pulsar_namespaces_set-offload-threshold.md)	 - Set the offload threshold of a namespace
* [dataos-ctl operate pulsar namespaces set-persistence](dataos-ctl_operate_pulsar_namespaces_set-persistence.md)	 - Set the persistence policy for a namespace
* [dataos-ctl operate pulsar namespaces set-publish-rate](dataos-ctl_operate_pulsar_namespaces_set-publish-rate.md)	 - Set the default message publish rate of a namespace per second
* [dataos-ctl operate pulsar namespaces set-replicator-dispatch-rate](dataos-ctl_operate_pulsar_namespaces_set-replicator-dispatch-rate.md)	 - Set the default replicator message dispatch rate of a namespace
* [dataos-ctl operate pulsar namespaces set-retention](dataos-ctl_operate_pulsar_namespaces_set-retention.md)	 - Set the retention policy for a namespace
* [dataos-ctl operate pulsar namespaces set-schema-autoupdate-strategy](dataos-ctl_operate_pulsar_namespaces_set-schema-autoupdate-strategy.md)	 - Set the schema auto-update strategy of a namespace
* [dataos-ctl operate pulsar namespaces set-schema-validation-enforced](dataos-ctl_operate_pulsar_namespaces_set-schema-validation-enforced.md)	 - Enable/Disable schema validation enforced
* [dataos-ctl operate pulsar namespaces set-subscribe-rate](dataos-ctl_operate_pulsar_namespaces_set-subscribe-rate.md)	 - Set the default subscribe rate per consumer of a namespace
* [dataos-ctl operate pulsar namespaces set-subscription-auth-mode](dataos-ctl_operate_pulsar_namespaces_set-subscription-auth-mode.md)	 - Set the default subscription auth mode of a namespace
* [dataos-ctl operate pulsar namespaces set-subscription-dispatch-rate](dataos-ctl_operate_pulsar_namespaces_set-subscription-dispatch-rate.md)	 - Set the default subscription message dispatch rate of a namespace
* [dataos-ctl operate pulsar namespaces set-topic-auto-creation](dataos-ctl_operate_pulsar_namespaces_set-topic-auto-creation.md)	 - Set topic auto-creation for a namespace
* [dataos-ctl operate pulsar namespaces split-bundle](dataos-ctl_operate_pulsar_namespaces_split-bundle.md)	 - Split a namespace-bundle from the current serving broker
* [dataos-ctl operate pulsar namespaces topics](dataos-ctl_operate_pulsar_namespaces_topics.md)	 - Get the list of topics for a namespace
* [dataos-ctl operate pulsar namespaces unload](dataos-ctl_operate_pulsar_namespaces_unload.md)	 - Unload a namespace from the current serving broker
* [dataos-ctl operate pulsar namespaces unsubscribe](dataos-ctl_operate_pulsar_namespaces_unsubscribe.md)	 - Unsubscribe the specified subscription for all topic of a namespace

