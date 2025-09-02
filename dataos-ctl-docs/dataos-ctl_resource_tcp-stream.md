## dataos-ctl resource tcp-stream

Open a tcp stream for DataOS® Resources

### Synopsis

Open a tcp stream for resources in the DataOS®

```
dataos-ctl resource tcp-stream [flags]
```

### Options

```
      --dataplane string       Dataplane name (default "hub")
  -h, --help                   help for tcp-stream
  -i, --identifier string      Identifier of resource, like: NAME:VERSION:TYPE
      --listenPort int         Port the local client will listen on to tcp stream (default 14040)
  -n, --name string            Name of resource
      --node string            Node name to open tcp stream in resource runtime
      --servicePort int        Service port to be forwarded (default 4040)
      --serviceSuffix string   Suffix to override default service suffix: ui-svc (default "ui-svc")
      --tls-allow-insecure     Allow Insecure TLS connections
  -t, --type string            The resource type to tcp-stream. Workspace resources: workflow,service,worker,secret,database,cluster,volume,resource,monitor,pager,lakehouse,lens. Instance resources: policy,depot,compute,dataplane,stack,operator,bundle,instance-secret,grant.
  -w, --workspace string       Workspace to target resource (default "public")
```

### SEE ALSO

* [dataos-ctl resource](dataos-ctl_resource.md)	 - Manage resources in the DataOS®

