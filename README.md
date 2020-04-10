# fabrq

Provides a couple of useful commands to manage [Redis Queue](https://python-rq.org) across hosts with [Fabric](http://www.fabfile.org), most notably starting and stopping many workers at once. 


After cloning, install with:
```
pip install -e .
```

On all hosts redis connection information should be stored in environment variables. The following snippet can be helpful, edit to match your configuration:
```
export REDIS_HOST="localhost"
export REDIS_PORT="6379"
export REDIS_DB="0"
export REDIS_PASSWORD=""
export REDIS_URL="redis://:$REDIS_PASSWORD@$REDIS_HOST:$REDIS_PORT/$REDIS_DB"
```

If you are using [rq-dashboard](https://github.com/Parallels/rq-dashboard) also include:
```
export RQ_DASHBOARD_URL="https://..."
```

`fabrq` provides a fabfiles and uses the [`fab` command line tool](http://docs.fabfile.org/en/2.5/getting-started.html#addendum-the-fab-command-line-tool): Calling `fabrq` on the shell translates into `fab -r fabrq/fabfile.py` and forwards all arguments.

For a list of available commands thus use:
```
fabrq --list
```

A quick way to set up host information, is [using `ssh_config`](http://docs.fabfile.org/en/2.5/concepts/configuration.html#loading-and-using-ssh-config-files). 
