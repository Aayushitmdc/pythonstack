## dataos-ctl apply

Apply DataOS® Resources

### Synopsis

Apply resources in the DataOS®

```
dataos-ctl apply [flags]
```

### Options

```
  -d, --de-ref                  De-reference the files, do not apply
      --disable-interpolation   Disable interpolation, do not interpolate $ENV|${ENV}
      --disable-resolve-stack   Disable resolve stack
  -h, --help                    help for apply
  -l, --lint                    Lint the files, do not apply
  -f, --manifestFile string     Manifest file location
  -r, --re-run                  Re-run resource after apply
  -R, --recursive               Get manifest files recursively from the provided directory
      --tls-allow-insecure      Allow insecure TLS connections
  -w, --workspace string        Workspace to target resource (default "public")
```

### SEE ALSO

* [dataos-ctl](dataos-ctl.md)	 - DataOS® command line.

