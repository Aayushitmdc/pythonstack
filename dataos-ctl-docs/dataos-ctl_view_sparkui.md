## dataos-ctl view sparkui



```
dataos-ctl view sparkui [flags]
```

### Options

```
  -h, --help                help for sparkui
  -i, --identifier string   Identifier of resource, like: NAME:VERSION:TYPE:WORKSPACE
  -n, --name string         Name to query
      --node string         Runtime Node name
  -p, --port int            sparkui port (default 4040)
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

* [dataos-ctl view](dataos-ctl_view.md)	 - View DataOS® Applications and Resources

