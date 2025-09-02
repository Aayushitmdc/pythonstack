## dataos-ctl resource runtime resume

Resume DataOS® Runnable Resources

### Synopsis

Resume runnable resources in the DataOS®

```
dataos-ctl resource runtime resume [flags]
```

### Options

```
  -h, --help                  help for resume
      --id string             Resource ID, like: TYPE:VERSION:NAME:WORKSPACE(optional), depot:v1:icebase or service:v1:ping:sandbox
  -i, --identifier string     Identifier of resource, like: NAME:VERSION:TYPE
  -f, --manifestFile string   Manifest File location
  -n, --name string           Name to resume
      --tls-allow-insecure    Allow insecure TLS connections
  -t, --type string           The resource type to resume. Workspace resources: workflow.
  -v, --version string        Version to resume (default "v1")
  -w, --workspace string      Workspace to target
```

### SEE ALSO

* [dataos-ctl resource runtime](dataos-ctl_resource_runtime.md)	 - DataOS® runtime management commands

