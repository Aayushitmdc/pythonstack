## dataos-ctl delete

Delete DataOS® Resources

### Synopsis

Delete resources in the DataOS®

```
dataos-ctl delete [flags]
```

### Options

```
      --force                 Force delete even though dependencies are not allowing it
  -h, --help                  help for delete
      --id string             Resource ID, like: TYPE:VERSION:NAME:WORKSPACE(optional), depot:v1:icebase or service:v1:ping:sandbox
  -i, --identifier string     Identifier of resource, like: NAME:VERSION:TYPE
  -f, --manifestFile string   Manifest file location
  -n, --name string           Names of resources (space-separated)
      --tls-allow-insecure    Allow Insecure TLS connections
  -t, --type string           The resource type to delete. Workspace resources: workflow,service,worker,secret,database,cluster,volume,resource,monitor,pager,lakehouse,lens. Instance resources: policy,depot,compute,dataplane,stack,operator,bundle,instance-secret,grant.
  -v, --version string        Version of resource (default "v1")
  -w, --workspace string      Workspace to target resource (default "public")
```

### SEE ALSO

* [dataos-ctl](dataos-ctl.md)	 - DataOS® command line.

