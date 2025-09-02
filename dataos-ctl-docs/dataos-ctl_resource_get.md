## dataos-ctl resource get

Get DataOS® Resources

### Synopsis

Get resources in the DataOS®

```
dataos-ctl resource get [flags]
```

### Options

```
  -a, --all                   Get resources for all owners
  -d, --details               Set to true to include details in the result
      --errorDetails          Set to true to include error details in specific columns in the result
  -h, --help                  help for get
      --id string             Resource ID, like: TYPE:VERSION:NAME:WORKSPACE(optional), depot:v1:icebase or service:v1:ping:sandbox
  -i, --identifier string     Identifier of resource, like: NAME:VERSION:TYPE
  -f, --manifestFile string   Manifest File location
  -n, --name string           Name to query
  -o, --owner string          Get resources for a specific owner id, defaults to your id.
  -r, --refresh               Auto refresh the results
      --refreshRate int       Refresh rate in seconds (default 5)
      --tags                  Set to true to include tags in the result
      --tls-allow-insecure    Allow insecure TLS connections
  -t, --type string           The resource type to get. Workspace resources: workflow,service,worker,secret,database,cluster,volume,resource,monitor,pager,lakehouse,lens. Instance resources: policy,depot,compute,dataplane,stack,operator,bundle,instance-secret,grant.
      --unSanitize            Get the resources un-sanitized, this includes sensitive fields.
  -v, --version string        Version to query (default "v1")
      --workflowDetails       Set to true to include workflow details in specific columns in the result
  -w, --workspace string      Workspace to query
```

### SEE ALSO

* [dataos-ctl resource](dataos-ctl_resource.md)	 - Manage resources in the DataOS®
* [dataos-ctl resource get runtime](dataos-ctl_resource_get_runtime.md)	 - Get DataOS® Runtime Details

