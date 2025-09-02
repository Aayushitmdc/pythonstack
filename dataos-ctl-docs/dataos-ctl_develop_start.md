## dataos-ctl develop start

Start development container

### Synopsis

Start development container

```
dataos-ctl develop start [flags]
```

### Options

```
  -d, --dataDir string          Directory containing the data.
      --disable-interpolation   Disable interpolation, do not interpolate $ENV|${ENV}
  -h, --help                    help for start
  -i, --image string            Optional image provided
  -f, --manifestFile string     Manifest file location.
  -p, --password string         Docker registry password.
  -P, --port int32              Exposed Port
      --region string           Docker registry region.
  -r, --registry string         Docker registry.
  -s, --stack string            Job stack.
  -u, --username string         Docker registry username.
```

### Options inherited from parent commands

```
      --tls-allow-insecure   Allow insecure TLS connections
```

### SEE ALSO

* [dataos-ctl develop](dataos-ctl_develop.md)	 - Manage DataOS® Development

