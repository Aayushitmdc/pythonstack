## dataos-ctl view

View DataOS® Applications and Resources

### Synopsis

View applications and resources in the DataOS®

```
dataos-ctl view [flags]
```

### Options

```
  -a, --application string   The application to view in your default browser: home, metis, workbench, operations, bifrost, atlas
  -h, --help                 help for view
  -i, --id string            The entity identifier e.g. 'workflow:v1:system-metadata-sync:system' to open in an app. Supported only by metis as of now.
      --log-url              Whether to show view url
  -t, --tab string           The tab identifier e.g. 'activity_feed, lineage etc' to open a tab in an app. Supported only by metis as of now.
```

### Options inherited from parent commands

```
      --tls-allow-insecure   Allow insecure TLS connections
```

### SEE ALSO

* [dataos-ctl](dataos-ctl.md)	 - DataOS® command line.
* [dataos-ctl view sparkui](dataos-ctl_view_sparkui.md)	 - 

