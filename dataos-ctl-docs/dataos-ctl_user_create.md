## dataos-ctl user create

Create a DataOS® User

### Synopsis

Create a DataOS® User

```
dataos-ctl user create [flags]
```

### Options

```
      --apikeyName string   A specific apikey name to associate with the new user as a token
  -d, --duration string     The duration that the apikey should last before expiring
  -e, --email string        The email
  -h, --help                help for create
  -n, --name string         The user name
      --tags strings        The list of tags to associate with the user
  -t, --type string         The user type: person|application
  -u, --user_id string      The userId
```

### Options inherited from parent commands

```
      --tls-allow-insecure   Allow insecure TLS connections
```

### SEE ALSO

* [dataos-ctl user](dataos-ctl_user.md)	 - Manage DataOS® Users

