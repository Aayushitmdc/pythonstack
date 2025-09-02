## dataos-ctl log

Get DataOS® Resource Logs

### Synopsis

Get the logs for a resource in the DataOS®

```
dataos-ctl log [flags]
```

### Options

```
  -c, --container string    Container name to filter logs
  -f, --follow              Follow the logs
  -h, --help                help for log
  -i, --identifier string   Identifier of resource, like: NAME:VERSION:TYPE
  -r, --includeRunnable     Include runnable system pods and logs
  -n, --name string         Name to query
      --node string         Node name to filter logs
  -l, --tailLines int       Number of tail lines to retrieve, use -1 to get all logs (default 300)
  -t, --type string         The resource type to get, possible values: service, workflow, cluster, depot
  -v, --version string      Version to query (default "v1")
  -w, --workspace string    Workspace to query (default "public")
```

### Options inherited from parent commands

```
      --tls-allow-insecure   Allow insecure TLS connections
```

### SEE ALSO

* [dataos-ctl](dataos-ctl.md)	 - DataOS® command line.

