## Branch Bug [Resolved]
Accidentally opened GitPod from the User Story section of GitHub, and then committed from this repository which git classed as a side branch.
Solution:
- Merged with main
- GitHub advised that this branch can be safely deleted
- Deleted side branch to avoid confusion with main branch
- Option is present to restore side branch.

## run server Bug [Resolved]
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

## Reason for Bug
As swapped from following Django Documentation to video:
Docs give install todo sooner than video
hence this error


### Resolution to runserver bug [Resolved]
#### Solution steps
Step 1: Decided to move on with LMS
Step 2: Noticed that next slide showed Browser 
        running server with:
    - You are seeing this page
        because you have set Debug=TRUE
        in your settings.py file
Step 3: Opened settings.py file 
        with the intention of changing
        or checking that
        this setting was set to
        Debug=True
Step 4: Saw the todo line with inline comment
        - remembered / realised
            that this was the line which was
            or may be causing the 
            runserver Bug
Step 5: Commented out todo line, Saved
        and Committed settings.py file
Step 6: Reran server
Step 7: Went to Remote Explorer 
        in side panel of
        Visual Studio Code
Step 8: Noted PORT 8000 open
Step 9: opened terminal
Step 10: terminal seemed to have automatically reset to 
        18 unapplied migrations Bug (may not be documented yet as such)
Step 11: Went bacck to 
        PORT 8000 in Remote Explorer
        in side bar in 
        Visual Studio Code
        Clicked to Open Browser
Step 12: Server opened,
        showed running in Browser