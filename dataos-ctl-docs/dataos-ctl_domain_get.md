## dataos-ctl domain get

Get DataOS® Domains

### Synopsis

Get domains in the DataOS®

```
dataos-ctl domain get [flags]
```

### Options

```
  -a, --all                   Get domains for all owners
  -d, --details               Set to true to include details in the result
  -i, --domainId string       Domain ID, like: TYPE:VERSION:NAME
  -h, --help                  help for get
  -f, --manifestFile string   Manifest File location
  -n, --name string           Domain name to query
  -o, --owner string          Get domains for a specific owner id, defaults to your id.
  -r, --refresh               Auto refresh the results
      --refreshRate int       Refresh rate in seconds (default 5)
      --tags                  Set to true to include tags in the result
      --tls-allow-insecure    Allow insecure TLS connections
  -t, --type string           Domain type to query
  -v, --version string        Domain version to query
```

### SEE ALSO

* [dataos-ctl domain](dataos-ctl_domain.md)	 - Manage domains in the DataOS®

