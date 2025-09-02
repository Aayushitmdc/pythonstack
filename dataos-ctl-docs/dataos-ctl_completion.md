## dataos-ctl completion

Shell completion for the given shell (zsh or bash)

### Synopsis


	Outputs shell completion for the given shell (zsh or bash)

	zsh:
		option 1 (speedy prompt startup time):
			$ dataos-ctl completion zsh > ~/.dataos/.dataos-ctl-completion   # for zsh users
			$ source ~/.dataos/.dataos-ctl-completion
		option 2 (always gets current commands):
			$ source <(dataos-ctl completion zsh)  # for zsh users

	bash:
		This depends on the bash-completion binary.  Example installation instructions:
		OS X:
			$ brew install bash-completion
			$ source $(brew --prefix)/etc/bash_completion
			$ dataos-ctl completion bash > ~/.dataos/.dataos-ctl-completion  # for bash users
			$ source ~/.dataos/.dataos-ctl-completion
		Ubuntu:
			$ apt-get install bash-completion
			$ source /etc/bash-completion
			$ source <(dataos-ctl completion bash)

	Additionally, you may want to output the completion to a file and source in your .bashrc or .zshrc


```
dataos-ctl completion SHELL [flags]
```

### Options

```
  -h, --help   help for completion
```

### Options inherited from parent commands

```
      --tls-allow-insecure   Allow insecure TLS connections
```

### SEE ALSO

* [dataos-ctl](dataos-ctl.md)	 - DataOS® command line.

