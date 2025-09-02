## dataos-ctl themis session list

List Sessions DataOS® Themis Resource

### Synopsis

List Sessions of Themis cluster in DataOS®

```
dataos-ctl themis session list [flags]
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

* [dataos-ctl themis session](dataos-ctl_themis_session.md)	 - Manage Sessions of DataOS® Themis Resource

