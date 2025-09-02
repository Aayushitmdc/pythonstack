## dataos-ctl operate pulsar bookkeeper auto-recovery list-under-replicated-ledger

Get all the under-replicated ledgers which have been marked for re-replication.

### Synopsis

USED FOR:
    This command is used for getting all the under-replicated ledgers which have been marked for re-replication.

REQUIRED PERMISSION:
    This command does not need any permission.

OUTPUT:
    #Get the under-replicated ledgers successfully.
    {
        [ledgerId1, ledgerId2...]
    }



```
dataos-ctl operate pulsar bookkeeper auto-recovery list-under-replicated-ledger [flags]
```

### Examples

```
    #Get all the under-replicated ledgers which have been marked for re-replication.
    pulsarctl bookkeeper auto-recovery list-under-replicated-ledger

    #Get all the under-replicated ledgers of a bookie which have been marked for re-replication.
    pulsarctl bookkeeper auto-recovery list-under-replicated-ledger --include (bookie-ip:bookie-port)

    #Get all the under-replicated ledgers except a bookie which have been marked for re-replication.
    pulsarctl bookkeeper auto-recovery list-under-replicated-ledger --exclude (bookie-ip:bookie-port)


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
      --exclude string                     Show the under-replicated ledger exclude the bookie.
  -h, --help                               help for list-under-replicated-ledger
      --include string                     Show the under-replicated ledger of the bookie.
  -o, --output string                      The output format (text,json,yaml) (default "text")
      --show                               Show the replicate ledger list.
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

* [dataos-ctl operate pulsar bookkeeper auto-recovery](dataos-ctl_operate_pulsar_bookkeeper_auto-recovery.md)	 - Operations about auto recovering

