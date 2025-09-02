## dataos-ctl get runtime

Get DataOS® Runtime Details

### Synopsis

Get the runtime details of a resource in the DataOS®

```
dataos-ctl get runtime [flags]
```

### Options

```
  -d, --details               Print lots of details
  -h, --help                  help for runtime
      --id string             Resource ID, like: TYPE:VERSION:NAME:WORKSPACE(optional), depot:v1:icebase or service:v1:ping:sandbox
  -i, --identifier string     Identifier of resource, like: NAME:VERSION:TYPE:WORKSPACE
  -f, --manifestFile string   Manifest file location
  -n, --name string           Name to query
      --node string           Node name to get details
  -r, --refresh               Auto refresh the results
      --refreshRate int       Refresh rate in seconds (default 5)
  -t, --type string           The resource type to get. Workspace resources: workflow, service, worker, cluster. Instance resources: depot.
  -v, --version string        Version to query (default "v1")
  -w, --workspace string      Workspace to query
  -y, --yaml                  Print the full node as yaml
```

### Options inherited from parent commands

```
      --tls-allow-insecure   Allow insecure TLS connections
```

### SEE ALSO

* [dataos-ctl get](dataos-ctl_get.md)	 - Get DataOS® Resources

