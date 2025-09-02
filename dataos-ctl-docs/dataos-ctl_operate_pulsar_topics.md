## dataos-ctl operate pulsar topics

Operations about topic(s)

```
dataos-ctl operate pulsar topics [flags]
```

### Options

```
  -h, --help   help for topics
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
* [dataos-ctl operate pulsar topics bundle-range](dataos-ctl_operate_pulsar_topics_bundle-range.md)	 - Get the namespace bundle range of a topic
* [dataos-ctl operate pulsar topics compact](dataos-ctl_operate_pulsar_topics_compact.md)	 - Compact a topic
* [dataos-ctl operate pulsar topics compact-status](dataos-ctl_operate_pulsar_topics_compact-status.md)	 - Get status of compaction on a topic
* [dataos-ctl operate pulsar topics create](dataos-ctl_operate_pulsar_topics_create.md)	 - Create a topic with n partitions
* [dataos-ctl operate pulsar topics delete](dataos-ctl_operate_pulsar_topics_delete.md)	 - Delete a topic
* [dataos-ctl operate pulsar topics get](dataos-ctl_operate_pulsar_topics_get.md)	 - Get the specified topic metadata
* [dataos-ctl operate pulsar topics get-backlog-quotas](dataos-ctl_operate_pulsar_topics_get-backlog-quotas.md)	 - Get the backlog quota policy for a topic
* [dataos-ctl operate pulsar topics get-compaction-threshold](dataos-ctl_operate_pulsar_topics_get-compaction-threshold.md)	 - Get the compaction threshold for a topic
* [dataos-ctl operate pulsar topics get-deduplication](dataos-ctl_operate_pulsar_topics_get-deduplication.md)	 - Get the deduplication policy for a topic
* [dataos-ctl operate pulsar topics get-delayed-delivery](dataos-ctl_operate_pulsar_topics_get-delayed-delivery.md)	 - Get delayed delivery policy for a topic
* [dataos-ctl operate pulsar topics get-dispatch-rate](dataos-ctl_operate_pulsar_topics_get-dispatch-rate.md)	 - Get message dispatch rate for a topic
* [dataos-ctl operate pulsar topics get-inactive-topic-policies](dataos-ctl_operate_pulsar_topics_get-inactive-topic-policies.md)	 - Get the inactive topic policies on a topic
* [dataos-ctl operate pulsar topics get-max-consumers](dataos-ctl_operate_pulsar_topics_get-max-consumers.md)	 - Get max number of consumers for a topic
* [dataos-ctl operate pulsar topics get-max-producers](dataos-ctl_operate_pulsar_topics_get-max-producers.md)	 - Get max number of producers for a topic
* [dataos-ctl operate pulsar topics get-max-unacked-messages-per-consumer](dataos-ctl_operate_pulsar_topics_get-max-unacked-messages-per-consumer.md)	 - Get max unacked messages per consumer for a topic
* [dataos-ctl operate pulsar topics get-max-unacked-messages-per-subscription](dataos-ctl_operate_pulsar_topics_get-max-unacked-messages-per-subscription.md)	 - Get max unacked messages per subscription for a topic
* [dataos-ctl operate pulsar topics get-message-ttl](dataos-ctl_operate_pulsar_topics_get-message-ttl.md)	 - Get message TTL settings of a topic
* [dataos-ctl operate pulsar topics get-permissions](dataos-ctl_operate_pulsar_topics_get-permissions.md)	 - Get the permissions of a topic
* [dataos-ctl operate pulsar topics get-persistence](dataos-ctl_operate_pulsar_topics_get-persistence.md)	 - Get the persistence of a topic
* [dataos-ctl operate pulsar topics get-publish-rate](dataos-ctl_operate_pulsar_topics_get-publish-rate.md)	 - Get message publish rate for a topic
* [dataos-ctl operate pulsar topics get-retention](dataos-ctl_operate_pulsar_topics_get-retention.md)	 - Get the retention policy for a topic
* [dataos-ctl operate pulsar topics grant-permissions](dataos-ctl_operate_pulsar_topics_grant-permissions.md)	 - Grant permissions to a client on a topic
* [dataos-ctl operate pulsar topics internal-info](dataos-ctl_operate_pulsar_topics_internal-info.md)	 - Get the topic internal info
* [dataos-ctl operate pulsar topics internal-stats](dataos-ctl_operate_pulsar_topics_internal-stats.md)	 - Get the internal stats of the specified topic
* [dataos-ctl operate pulsar topics last-message-id](dataos-ctl_operate_pulsar_topics_last-message-id.md)	 - Get the last message id of a topic
* [dataos-ctl operate pulsar topics list](dataos-ctl_operate_pulsar_topics_list.md)	 - List all exist topics under the specified namespace
* [dataos-ctl operate pulsar topics lookup](dataos-ctl_operate_pulsar_topics_lookup.md)	 - Look up a topic
* [dataos-ctl operate pulsar topics offload](dataos-ctl_operate_pulsar_topics_offload.md)	 - Offload the messages of a topic to a long-term storage
* [dataos-ctl operate pulsar topics offload-status](dataos-ctl_operate_pulsar_topics_offload-status.md)	 - Check the status of data offloading
* [dataos-ctl operate pulsar topics remove-backlog-quota](dataos-ctl_operate_pulsar_topics_remove-backlog-quota.md)	 - Remove a backlog quota policy from a topic
* [dataos-ctl operate pulsar topics remove-compaction-threshold](dataos-ctl_operate_pulsar_topics_remove-compaction-threshold.md)	 - Remove the compaction threshold for a topic
* [dataos-ctl operate pulsar topics remove-deduplication](dataos-ctl_operate_pulsar_topics_remove-deduplication.md)	 - Remove the deduplication policy for a topic
* [dataos-ctl operate pulsar topics remove-delayed-delivery](dataos-ctl_operate_pulsar_topics_remove-delayed-delivery.md)	 - Remove delayed delivery policy for a topic
* [dataos-ctl operate pulsar topics remove-dispatch-rate](dataos-ctl_operate_pulsar_topics_remove-dispatch-rate.md)	 - Remove message dispatch rate for a topic
* [dataos-ctl operate pulsar topics remove-dispatch-rate](dataos-ctl_operate_pulsar_topics_remove-dispatch-rate.md)	 - Remove message dispatch rate for a topic
* [dataos-ctl operate pulsar topics remove-inactive-topic-policies](dataos-ctl_operate_pulsar_topics_remove-inactive-topic-policies.md)	 - Remove inactive topic policies from a topic
* [dataos-ctl operate pulsar topics remove-max-consumers](dataos-ctl_operate_pulsar_topics_remove-max-consumers.md)	 - Remove max number of consumers for a topic
* [dataos-ctl operate pulsar topics remove-max-producers](dataos-ctl_operate_pulsar_topics_remove-max-producers.md)	 - Remove max number of producers for a topic
* [dataos-ctl operate pulsar topics remove-max-unacked-messages-per-consumer](dataos-ctl_operate_pulsar_topics_remove-max-unacked-messages-per-consumer.md)	 - Remove max unacked messages per consumer for a topic
* [dataos-ctl operate pulsar topics remove-max-unacked-messages-per-subscription](dataos-ctl_operate_pulsar_topics_remove-max-unacked-messages-per-subscription.md)	 - Remove max unacked messages per subscription for a topic
* [dataos-ctl operate pulsar topics remove-message-ttl](dataos-ctl_operate_pulsar_topics_remove-message-ttl.md)	 - Remove Message TTL for a topic
* [dataos-ctl operate pulsar topics remove-persistence](dataos-ctl_operate_pulsar_topics_remove-persistence.md)	 - Remove persistence for a topic
* [dataos-ctl operate pulsar topics remove-publish-rate](dataos-ctl_operate_pulsar_topics_remove-publish-rate.md)	 - Remove message publish rate for a topic
* [dataos-ctl operate pulsar topics remove-retention](dataos-ctl_operate_pulsar_topics_remove-retention.md)	 - Remove the retention policy for a topic
* [dataos-ctl operate pulsar topics revoke-permissions](dataos-ctl_operate_pulsar_topics_revoke-permissions.md)	 - Revoke a client role permissions on a topic
* [dataos-ctl operate pulsar topics set-backlog-quota](dataos-ctl_operate_pulsar_topics_set-backlog-quota.md)	 - Set a backlog quota policy for a topic
* [dataos-ctl operate pulsar topics set-compaction-threshold](dataos-ctl_operate_pulsar_topics_set-compaction-threshold.md)	 - Set the compaction threshold for a topic
* [dataos-ctl operate pulsar topics set-deduplication](dataos-ctl_operate_pulsar_topics_set-deduplication.md)	 - Set the deduplication policy for a topic
* [dataos-ctl operate pulsar topics set-delayed-delivery](dataos-ctl_operate_pulsar_topics_set-delayed-delivery.md)	 - Set delayed delivery policy for a topic
* [dataos-ctl operate pulsar topics set-dispatch-rate](dataos-ctl_operate_pulsar_topics_set-dispatch-rate.md)	 - Set message dispatch rate for a topic
* [dataos-ctl operate pulsar topics set-dispatch-rate](dataos-ctl_operate_pulsar_topics_set-dispatch-rate.md)	 - Set message dispatch rate for a topic
* [dataos-ctl operate pulsar topics set-inactive-topic-policies](dataos-ctl_operate_pulsar_topics_set-inactive-topic-policies.md)	 - Set the inactive topic policies on a topic
* [dataos-ctl operate pulsar topics set-max-consumers](dataos-ctl_operate_pulsar_topics_set-max-consumers.md)	 - Set max number of consumers for a topic
* [dataos-ctl operate pulsar topics set-max-producers](dataos-ctl_operate_pulsar_topics_set-max-producers.md)	 - Set max number of producers for a topic
* [dataos-ctl operate pulsar topics set-max-unacked-messages-per-consumer](dataos-ctl_operate_pulsar_topics_set-max-unacked-messages-per-consumer.md)	 - Set max unacked messages per consumer for a topic
* [dataos-ctl operate pulsar topics set-max-unacked-messages-per-subscription](dataos-ctl_operate_pulsar_topics_set-max-unacked-messages-per-subscription.md)	 - Set max unacked messages per subscription for a topic
* [dataos-ctl operate pulsar topics set-message-ttl](dataos-ctl_operate_pulsar_topics_set-message-ttl.md)	 - Set Message TTL for a topic
* [dataos-ctl operate pulsar topics set-persistence](dataos-ctl_operate_pulsar_topics_set-persistence.md)	 - Set persistence for a topic
* [dataos-ctl operate pulsar topics set-publish-rate](dataos-ctl_operate_pulsar_topics_set-publish-rate.md)	 - Set message publish rate for a topic
* [dataos-ctl operate pulsar topics set-retention](dataos-ctl_operate_pulsar_topics_set-retention.md)	 - Set the retention policy for a topic
* [dataos-ctl operate pulsar topics stats](dataos-ctl_operate_pulsar_topics_stats.md)	 - Get the stats of an existing topic
* [dataos-ctl operate pulsar topics terminate](dataos-ctl_operate_pulsar_topics_terminate.md)	 - Terminate a non-partitioned topic
* [dataos-ctl operate pulsar topics unload](dataos-ctl_operate_pulsar_topics_unload.md)	 - Unloading a topic
* [dataos-ctl operate pulsar topics update](dataos-ctl_operate_pulsar_topics_update.md)	 - Update partitioned topic partitions

