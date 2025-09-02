## dataos-ctl themis engine list

List Engine DataOS® Themis Resource

### Synopsis

List Engine of Themis cluster in DataOS®

```
dataos-ctl themis engine list [flags]
```

### Options

```
  -d, --dataplane string    The dataplane to connect to the gateway. (default "hub")
  -h, --help                help for list
      --id string           Resource ID, like: TYPE:VERSION:NAME:WORKSPACE(optional), depot:v1:icebase or service:v1:ping:sandbox
  -i, --identifier string   Identifier of resource, like: NAME:VERSION:TYPE
  -u, --user string         List resources of other user, use comma seperated to list multiple users
```

### Options inherited from parent commands

```
      --tls-allow-insecure   Allow insecure TLS connections
```

### SEE ALSO

* [dataos-ctl themis engine](dataos-ctl_themis_engine.md)	 - Manage Engines of DataOS® Themis Resource

