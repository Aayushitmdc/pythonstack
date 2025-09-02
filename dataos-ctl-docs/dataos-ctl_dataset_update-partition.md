## dataos-ctl dataset update-partition

Update Partition

### Synopsis

Update Partition

```
dataos-ctl dataset update-partition [flags]
```

### Options

```
  -a, --address string       The address of Dataset
  -n, --count int            --count 2
  -h, --help                 help for update-partition
  -p, --partitions strings   --partitions <identity>:<column_name> 
                             --partitions <year/month/day/hour>:<column_name>:<partition_name> 
                             --partitions <bucket>:<column_name>:<partition_name>:<num_buckets> 
```

### Options inherited from parent commands

```
      --tls-allow-insecure   Allow insecure TLS connections
```

### SEE ALSO

* [dataos-ctl dataset](dataos-ctl_dataset.md)	 - Apply DataOS® data toolbox commands

