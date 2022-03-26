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

# New
## Line Length Bug [Resolved]

### Search String

`line too long (91 > 79 characters)flake8(E501)`

### Results
- [Line too long (82 &gt; 79 characters) (E501)](https://www.flake8rules.com/rules/E501.html)
- [PEP 8 – Style Guide for Python Code](https://peps.python.org/pep-0008/#maximum-line-length)

### Content

```
Backslashes may still be appropriate at times. For example, long, multiple with-statements could not use implicit continuation before Python 3.10, so backslashes were acceptable for that case:

with open('/path/to/some/file/you/want/to/read') as file_1, \
     open('/path/to/some/file/being/written', 'w') as file_2:
    file_2.write(file_1.read())
```

### Action

- Break lines
- Resolve pylint Problem

## no attribute 'sit' in admin.py Bug [Resolved]

### Summary of error (post resolution)
`AttributeError: module 'django.contrib.admin' has no attribute 'sit' in admin.py`

### Terminal output
gitpod /workspace/Portfolio-Project-4 (main) $ python3 manage.py runserver
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
  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/apps/registry.py", line 122, in populate
    app_config.ready()
  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/contrib/admin/apps.py", line 27, in ready
    self.module.autodiscover()
  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/contrib/admin/__init__.py", line 24, in autodiscover
    autodiscover_modules('admin', register_to=site)
  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/utils/module_loading.py", line 47, in autodiscover_modules
    import_module('%s.%s' % (app_config.name, module_to_search))
  File "/home/gitpod/.pyenv/versions/3.8.11/lib/python3.8/importlib/__init__.py", line 127, in import_module
    return _bootstrap._gcd_import(name[level:], package, level)
  File "<frozen importlib._bootstrap>", line 1014, in _gcd_import
  File "<frozen importlib._bootstrap>", line 991, in _find_and_load
  File "<frozen importlib._bootstrap>", line 975, in _find_and_load_unlocked
  File "<frozen importlib._bootstrap>", line 671, in _load_unlocked
  File "<frozen importlib._bootstrap_external>", line 843, in exec_module
  File "<frozen importlib._bootstrap>", line 219, in _call_with_frames_removed
  File "/workspace/Portfolio-Project-4/Your_Thoughts/admin.py", line 4, in <module>
    admin.sit.register(Post)
AttributeError: module 'django.contrib.admin' has no attribute 'sit'

## Search String
AttributeError: module 'django.contrib.admin' has no attribute 'sit'

## Result
- [In django i got AttributeError: module 'django.contrib.admin' has no attribute 'display'](https://stackoverflow.com/questions/67418161/in-django-i-got-attributeerror-module-django-contrib-admin-has-no-attribute)

## Actions
- Answer not found in above Reference
- Reread end of error, including line before last line (which was used as search string)

```
  File "/workspace/Portfolio-Project-4/Your_Thoughts/admin.py", line 4, in <module>
    admin.sit.register(Post)
```

- Edited `sit` to `site` in admin.py
- correction above allowed server launch without rerunning terminal commands

# New [Resolved]
## Bug 
Page not loading
## Further description of Issue and Solution
- In one of the urls.py files, under urlpatterns:
- two contradictory paths so, 
- commented the first:

```
    # path('', views.get_comment, name='get_comment'),
    path('', include('Your_Thoughts.urls'), name='Your_Thoughts_urls'),
```

# New [Resolved]
## Not deploying to heroku
## steps to solve

- look at models in models.py
- [Reference django docs](https://docs.djangoproject.com/en/4.0/ref/models/fields/)

### Completely remove Django migrations and reset database

1. Remove the all migrations files in project. Go through each of project apps' migration folders and remove everything inside, except the __init__.py file.

2. Drop the database. If using Heroku Postgres, the command for this is: 
`heroku pg:reset DATABASE_URL`.
Locally, just delete the db.sqlite3  file.

3.  Run the commands python3 manage.py makemigrations and python3 manage.py migrate to remake migrations and setup the new database.


