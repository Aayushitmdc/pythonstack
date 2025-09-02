## dataos-ctl operate log-stream

Stream the logs on a specific target

### Synopsis

Stream the logs on a specific target

```
dataos-ctl operate log-stream [flags]
```

### Options

```
      --container string     target container will be calling through peer k8s stream
      --dataplane string     target dataplane will be calling through peer k8s stream
  -h, --help                 help for log-stream
      --name string          target name will be calling through peer k8s stream
      --namespace string     target namespace will be calling through peer k8s stream
      --tailLines int        number of lines to start tailing from through peer k8s stream
      --tls-allow-insecure   Allow insecure TLS connections
```

### SEE ALSO

* [dataos-ctl operate](dataos-ctl_operate.md)	 - Operate the DataOS®

