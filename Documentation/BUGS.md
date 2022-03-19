## Unresolved Bugs
### Terminal Bash Error 1
Terminal Bash in Gitpod Shows the following two blocks:

```
 HISTFILE=/workspace/.gitpod/cmd-0 history -r; {
. ${GITPOD_REPO_ROOT}/.vscode/init_tasks.sh
} && {
/home/gitpod/.pg_ctl/bin/pg_start > /dev/null
}
```

```
  HISTFILE=/workspace/.gitpod/cmd-0 history -r; {
> . ${GITPOD_REPO_ROOT}/.vscode/init_tasks.sh
> } && {
> /home/gitpod/.pg_ctl/bin/pg_start > /dev/null
> }
Setting the greeting
Creating the gitpod user in MySQL
ERROR 2002 (HY000): Can't connect to local MySQL server through socket '/var/run/mysqld/mysqld.sock' (2)
ERROR 2002 (HY000): Can't connect to local MySQL server through socket '/var/run/mysqld/mysqld.sock' (2)
Granting privileges
ERROR 2002 (HY000): Can't connect to local MySQL server through socket '/var/run/mysqld/mysqld.sock' (2)
Creating .sqliterc file
Uninstalling unused dependencies...
ERROR: You must give at least one requirement to uninstall (see "pip help uninstall")
Your workspace is ready to use. Happy coding!
Unable to connect to VS Code server: Error in request.
Error: connect ECONNREFUSED 127.0.0.1:23000
    at TCPConnectWrap.afterConnect [as oncomplete] (net.js:1146:16) {
  errno: -111,
  code: 'ECONNREFUSED',
  syscall: 'connect',
  address: '127.0.0.1',
  port: 23000
}
gitpod /workspace/Portfolio-Project-4 
```

### Line length Bug
Line length exceeded in python
- line break not working
 using / \ \n
 not tried () parentheses
- next steps would be:
  - find out what binary operator is 
  - and is it the same as bitwise operator
  - cannot determine if interchangeable
    - in this case

#### Decision
  - suspend debugging for now

## run server Bug
## Reran command in CLI:

```
python3 manage.py runserver
```

### Output
Watching for file changes with StatReloader
Exception in thread django-main-thread:
Traceback (most recent call last):
  File "/home/gitpod/.pyenv/versions/3.8.11/lib/python3.8/threading.py", line 932, in _bootstrap_inner
    self.run()
  File "/home/gitpod/.pyenv/versions/3.8.11/lib/python3.8/threading.py", line 870, in run
    self._target(*self._args, **self._kwargs)
  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/utils/autoreload.py", line 64, in wrapper
    fn(*args, **kwargs)
  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/core/management/commands/runserver.py", line 110, in inner_run
    autoreload.raise_last_exception()
  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/utils/autoreload.py", line 87, in raise_last_exception
    raise _exception[1]
  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/core/management/__init__.py", line 375, in execute
    autoreload.check_errors(django.setup)()
  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/utils/autoreload.py", line 64, in wrapper
    fn(*args, **kwargs)
  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/__init__.py", line 24, in setup
    apps.populate(settings.INSTALLED_APPS)
  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/apps/registry.py", line 91, in populate
    app_config = AppConfig.create(entry)
  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/apps/config.py", line 224, in create
    import_module(entry)
  File "/home/gitpod/.pyenv/versions/3.8.11/lib/python3.8/importlib/__init__.py", line 127, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1014, in _gcd_import
  File "<frozen importlib._bootstrap>", line 991, in _find_and_load
  File "<frozen importlib._bootstrap>", line 973, in _find_and_load_unlocked
ModuleNotFoundError: No module named 'todo'
