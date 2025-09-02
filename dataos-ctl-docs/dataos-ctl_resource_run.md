## dataos-ctl resource run

Run DataOS® Resource

### Synopsis

Create and Run a Resource in the DataOS®

```
dataos-ctl resource run [flags]
```

### Options

```
  -c, --configFile string                     Config file location
      --disable-interpolation                 Disable interpolation, do not interpolate $ENV|${ENV}
      --do-not-delete-on-failure              Do not delete the resource on completion with failure (default true)
      --do-not-delete-on-success              Do not delete the resource on completion with success
      --failure-strings strings               Runtime strings that indicates this resource is complete with failure (default [failed])
  -h, --help                                  help for run
  -f, --manifestFile string                   Manifest file location
      --run-start-timeout-duration duration   The runtime start timeout duration (default 2m0s)
      --run-string string                     Runtime string that indicates this resource is running (default "running")
      --run-timeout-duration duration         The runtime timeout duration (default 5m0s)
      --stream-logs                           Stream logs from primary runtime node to stdout
      --success-strings strings               Runtime strings that indicates this resource is complete with success (default [succeeded])
  -w, --workspace string                      Workspace to target resource (default "public")
```

### Options inherited from parent commands

```
      --tls-allow-insecure   Allow insecure TLS connections
```

### SEE ALSO

* [dataos-ctl resource](dataos-ctl_resource.md)	 - Manage resources in the DataOS®

