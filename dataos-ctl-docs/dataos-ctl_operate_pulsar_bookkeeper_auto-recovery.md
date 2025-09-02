## dataos-ctl operate pulsar bookkeeper auto-recovery

Operations about auto recovering

```
dataos-ctl operate pulsar bookkeeper auto-recovery [flags]
```

### Options

```
  -h, --help   help for auto-recovery
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

* [dataos-ctl operate pulsar bookkeeper](dataos-ctl_operate_pulsar_bookkeeper.md)	 - Operations about bookKeeper
* [dataos-ctl operate pulsar bookkeeper auto-recovery decommission](dataos-ctl_operate_pulsar_bookkeeper_auto-recovery_decommission.md)	 - Decommission a bookie.
* [dataos-ctl operate pulsar bookkeeper auto-recovery get-lost-bookie-recovery-delay](dataos-ctl_operate_pulsar_bookkeeper_auto-recovery_get-lost-bookie-recovery-delay.md)	 - Get the lost bookie recovery delay of a bookie.
* [dataos-ctl operate pulsar bookkeeper auto-recovery list-under-replicated-ledger](dataos-ctl_operate_pulsar_bookkeeper_auto-recovery_list-under-replicated-ledger.md)	 - Get all the under-replicated ledgers which have been marked for re-replication.
* [dataos-ctl operate pulsar bookkeeper auto-recovery recover-bookie](dataos-ctl_operate_pulsar_bookkeeper_auto-recovery_recover-bookie.md)	 - Recover the ledger data of a failed bookie.
* [dataos-ctl operate pulsar bookkeeper auto-recovery set-lost-bookie-recovery-delay](dataos-ctl_operate_pulsar_bookkeeper_auto-recovery_set-lost-bookie-recovery-delay.md)	 - Set the lost bookie recovery delay.
* [dataos-ctl operate pulsar bookkeeper auto-recovery trigger-audit](dataos-ctl_operate_pulsar_bookkeeper_auto-recovery_trigger-audit.md)	 - Trigger audit by resetting the lost bookie recovery delay.
* [dataos-ctl operate pulsar bookkeeper auto-recovery who-is-auditor](dataos-ctl_operate_pulsar_bookkeeper_auto-recovery_who-is-auditor.md)	 - Get the auditor of the bookie.

