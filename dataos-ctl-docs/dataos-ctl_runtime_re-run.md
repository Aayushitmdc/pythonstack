## dataos-ctl runtime re-run

Re-run DataOS® Runnable Resources

### Synopsis

Re-run runnable resources in the DataOS®

```
dataos-ctl runtime re-run [flags]
```

### Options

```
  -h, --help                  help for re-run
      --id string             Resource ID, like: TYPE:VERSION:NAME:WORKSPACE(optional), depot:v1:icebase or service:v1:ping:sandbox
  -i, --identifier string     Identifier of resource, like: NAME:VERSION:TYPE
  -f, --manifestFile string   Manifest File location
  -n, --name string           Name to re-run
      --tls-allow-insecure    Allow insecure TLS connections
  -t, --type string           The resource type to re-run. Workspace resources: workflow.
  -v, --version string        Version to re-run (default "v1")
  -w, --workspace string      Workspace to target
```

### SEE ALSO

* [dataos-ctl runtime](dataos-ctl_runtime.md)	 - DataOS® runtime management commands

