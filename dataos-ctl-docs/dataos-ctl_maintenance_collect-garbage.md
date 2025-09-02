## dataos-ctl maintenance collect-garbage

Collect Garbage on the DataOS®

### Synopsis

Collect Garbage on the DataOS®

```
dataos-ctl maintenance collect-garbage [flags]
```

### Options

```
  -d, --duration string     the duration to calculate the age of resources that are eligible for garbage collection (default "168h")
  -h, --help                help for collect-garbage
  -k, --kubeconfig string   kubeconfig file location
  -l, --layer string        the layer to target in the DataOS, user|system (default "user")
```

### Options inherited from parent commands

```
      --tls-allow-insecure   Allow insecure TLS connections
```

### SEE ALSO

* [dataos-ctl maintenance](dataos-ctl_maintenance.md)	 - Maintenance of the DataOS®

