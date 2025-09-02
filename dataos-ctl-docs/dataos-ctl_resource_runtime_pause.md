## dataos-ctl resource runtime pause

Pause DataOS® Runnable Resources

### Synopsis

Pause runnable resources in the DataOS®

```
dataos-ctl resource runtime pause [flags]
```

### Options

```
  -h, --help                  help for pause
      --id string             Resource ID, like: TYPE:VERSION:NAME:WORKSPACE(optional), depot:v1:icebase or service:v1:ping:sandbox
  -i, --identifier string     Identifier of resource, like: NAME:VERSION:TYPE
  -f, --manifestFile string   Manifest File location
  -n, --name string           Name to pause
      --tls-allow-insecure    Allow insecure TLS connections
  -t, --type string           The resource type to pause. Workspace resources: workflow.
  -v, --version string        Version to pause (default "v1")
  -w, --workspace string      Workspace to target
```

### SEE ALSO

* [dataos-ctl resource runtime](dataos-ctl_resource_runtime.md)	 - DataOS® runtime management commands

