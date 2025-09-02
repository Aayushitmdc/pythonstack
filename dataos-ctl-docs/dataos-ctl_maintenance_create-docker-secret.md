## dataos-ctl maintenance create-docker-secret

Creates a Docker Secret for K8S

### Synopsis

Creates a Docker Secret for K8S

```
dataos-ctl maintenance create-docker-secret [flags]
```

### Options

```
      --heimdallSecretId string         heimdall secret id to get the docker registry username and password from
  -h, --help                            help for create-docker-secret
  -k, --kubeconfig string               kubeconfig file location
  -n, --namespace string                namespace where to store the docker secret
  -p, --password string                 password of the docker registry
  -g, --region string                   region of the docker registry
  -r, --registry string                 docker registry
  -s, --secretName string               name of the secret to store the docker secret
      --targetHeimdallSecretId string   heimdall secret id to store the resulting docker secret
  -t, --type string                     type of docker registry (docker|ecr)
  -u, --username string                 username of the docker registry
```

### Options inherited from parent commands

```
      --tls-allow-insecure   Allow insecure TLS connections
```

### SEE ALSO

* [dataos-ctl maintenance](dataos-ctl_maintenance.md)	 - Maintenance of the DataOS®

