## dataos-ctl runtime stop

Stop DataOS® Runnable Resources

### Synopsis

Stop runnable resources in the DataOS®

```
dataos-ctl runtime stop [flags]
```

### Options

```
  -h, --help                  help for stop
      --id string             Resource ID, like: TYPE:VERSION:NAME:WORKSPACE(optional), depot:v1:icebase or service:v1:ping:sandbox
  -i, --identifier string     Identifier of resource, like: NAME:VERSION:TYPE
  -f, --manifestFile string   Manifest File location
  -n, --name string           Name to stop
      --tls-allow-insecure    Allow insecure TLS connections
  -t, --type string           The resource type to stop. Workspace resources: workflow.
  -v, --version string        Version to stop (default "v1")
  -w, --workspace string      Workspace to target
```

### SEE ALSO

* [dataos-ctl runtime](dataos-ctl_runtime.md)	 - DataOS® runtime management commands

