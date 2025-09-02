## dataos-ctl product get

Get DataOS® Products

### Synopsis

Get products in the DataOS®

```
dataos-ctl product get [flags]
```

### Options

```
  -a, --all                   Get products for all owners
  -d, --details               Set to true to include details in the result
  -h, --help                  help for get
  -f, --manifestFile string   Manifest File location
  -n, --name string           Product name to query
  -o, --owner string          Get products for a specific owner id, defaults to your id.
  -i, --productId string      Product ID, like: TYPE:VERSION:NAME
  -r, --refresh               Auto refresh the results
      --refreshRate int       Refresh rate in seconds (default 5)
      --tags                  Set to true to include tags in the result
      --tls-allow-insecure    Allow insecure TLS connections
  -t, --type string           Product type to query
  -v, --version string        Product version to query
```

### SEE ALSO

* [dataos-ctl product](dataos-ctl_product.md)	 - Manage products in the DataOS®

