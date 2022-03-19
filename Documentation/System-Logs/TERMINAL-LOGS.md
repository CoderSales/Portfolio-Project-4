## Command
pip3 install Django==3.2
## Output
Collecting Django==3.2
  Downloading Django-3.2-py3-none-any.whl (7.9 MB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 7.9/7.9 MB 30.1 MB/s eta 0:00:00
Collecting sqlparse>=0.2.2
  Downloading sqlparse-0.4.2-py3-none-any.whl (42 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 42.3/42.3 KB 11.3 MB/s eta 0:00:00
Collecting pytz
  Downloading pytz-2021.3-py2.py3-none-any.whl (503 kB)
     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 503.5/503.5 KB 23.2 MB/s eta 0:00:00
Collecting asgiref<4,>=3.3.2
  Downloading asgiref-3.5.0-py3-none-any.whl (22 kB)
Installing collected packages: pytz, sqlparse, asgiref, Django
Successfully installed Django-3.2 asgiref-3.5.0 pytz-2021.3 sqlparse-0.4.2

## Command
python3 manage.py runserver

## Output
Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
March 19, 2022 - 09:29:09
Django version 3.2, using settings 'Profile_Project_4.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.Watching for file changes with StatReloader
Performing system checks...

System check identified no issues (0 silenced).

You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): admin, auth, contenttypes, sessions.
Run 'python manage.py migrate' to apply them.
March 19, 2022 - 09:29:09
Django version 3.2, using settings 'Profile_Project_4.settings'
Starting development server at http://127.0.0.1:8000/
Quit the server with CONTROL-C.

## Command

```
python manage.py migrate
```

## Output

```
Traceback (most recent call last):
  File "manage.py", line 22, in <module>
    main()
  File "manage.py", line 18, in main
    execute_from_command_line(sys.argv)
  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/core/management/__init__.py", line 419, in execute_from_command_line
    utility.execute()
  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/core/management/__init__.py", line 395, in execute
    django.setup()
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
```

## Command

```
python3 manage.py runserver
```

## Output
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