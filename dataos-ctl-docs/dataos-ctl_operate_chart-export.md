## dataos-ctl operate chart-export

Exports a Helm Chart from a Chart Registry

### Synopsis

Exports a Helm Chart from a Chart Registry

```
dataos-ctl operate chart-export [flags]
```

### Options

```
      --accessKey string      The AWS Access Key for ECR Chart Registry
      --accessSecret string   The AWS Access Secret for ECR Chart Registry
  -c, --chart string          The chart ref
  -d, --exportDir string      The directory to export the Helm chart
  -h, --help                  help for chart-export
      --region string         The AWS Region for ECR Chart Registry
      --registry string       The AWS ECR Chart Registry
```

### Options inherited from parent commands

```
      --tls-allow-insecure   Allow insecure TLS connections
```

### SEE ALSO

* [dataos-ctl operate](dataos-ctl_operate.md)	 - Operate the DataOS®

