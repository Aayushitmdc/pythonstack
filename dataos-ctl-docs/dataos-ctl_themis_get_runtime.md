## dataos-ctl themis get runtime

Get Themis Runtime Details in DataOS®

### Synopsis

Get the runtime details of a themis resource in the DataOS®

```
dataos-ctl themis get runtime [flags]
```

### Options

```
  -h, --help                help for runtime
  -i, --identifier string   Identifier of resource, like: NAME:VERSION:TYPE:WORKSPACE
  -n, --name string         Name to query
  -r, --refresh             Auto refresh the results
      --refreshRate int     Refresh rate in seconds (default 5)
  -t, --type string         The resource type to get. Workspace resources: workflow, service, worker, cluster. Instance resources: depot.
  -v, --version string      Version to query (default "v1")
  -w, --workspace string    Workspace to query
```

### Options inherited from parent commands

```
      --tls-allow-insecure   Allow insecure TLS connections
```

### SEE ALSO

* [dataos-ctl themis get](dataos-ctl_themis_get.md)	 - Get themis resources in the DataOS®

