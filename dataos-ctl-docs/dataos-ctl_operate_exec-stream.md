## dataos-ctl operate exec-stream

Execute-stream a command on a specific target

### Synopsis

Execute-stream a command on a specific target

```
dataos-ctl operate exec-stream [flags]
```

### Options

```
      --command string       command to exec on the target will be calling through peer k8s stream (default "sh")
      --container string     target container will be calling through peer k8s stream
      --dataplane string     target dataplane will be calling through peer k8s stream
  -h, --help                 help for exec-stream
      --name string          target name will be calling through peer k8s stream
      --namespace string     target namespace will be calling through peer k8s stream
      --tls-allow-insecure   Allow insecure TLS connections
```

### SEE ALSO

* [dataos-ctl operate](dataos-ctl_operate.md)	 - Operate the DataOS®

