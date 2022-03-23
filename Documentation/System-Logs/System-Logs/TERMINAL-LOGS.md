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

## CLI input
`python3 manage.py makemigrations`

- get rid of default value as mutually exclusive with auto_now and other auto_ setting(s).

- However, due to issue at time of running above migration command: 

- need to remove default value in code, to avoid error,

- then set value to `timezone.now()` when prompted while above migration commmand running.

## Debug
### Search String

```
SystemCheckError: System check identified some issues: ERRORS: Your_Thoughts.Post.created_on: (fields.E160) The options auto_now, auto_now_add, and default are mutually exclusive. Only one of these options may be present.
```

### Reference
- [The options auto_now, auto_now_add, and default are mutually exclusive. Only one of these options may be present](https://stackoverflow.com/questions/45874365/the-options-auto-now-auto-now-add-and-default-are-mutually-exclusive-only-one)

### Content

```
Just use:

class Users(models.Model):
    ctime = models.DateTimeField(auto_now_add=True)
    uptime = models.DateTimeField(auto_now=True)
It will work.

Explanation:

These both are mutually exclusive means you should use only one of them, not both.
```

#### Solution to problem:
##### Search String

```
field 'created_on' with 'auto_now_add=True' to post without a default; the database needs something to populate existing rows.  SystemCheckError: System check identified some issues: ERRORS: Your_Thoughts.Post.created_on: (fields.E160) The options auto_now, auto_now_add, and default are mutually exclusive. Only one of these options may be present.
```

##### Reference
- [Django DateTimeField with auto_now_add asks for default](https://stackoverflow.com/questions/56310322/django-datetimefield-with-auto-now-add-asks-for-default)
##### Content

```
You have already some rows without created_at value. But when you added following field and run migration

created_at = models.DateTimeField( auto_now_add = True)
It expects the existing row has created_at value. So, It warns you at the time of migrations.

To solve this problem. You can choose the 1st option which says Provide a one-off default now (will be set on all existing rows). By choosing the 1st option you are asking for value. Here you can enter timezone.now(). It will populate existing rows with the current timestamp.
```

## CLI Output
gitpod /workspace/Portfolio-Project-4 (main) $ python3 manage.py makemigrations

SystemCheckError: System check identified some issues:

ERRORS:
Your_Thoughts.Post.created_on: (fields.E160) The options auto_now, auto_now_add, and default are mutually exclusive. Only one of these options may be present.
gitpod /workspace/Portfolio-Project-4 (main) $ python3 manage.py makemigrations
You are trying to add the field 'created_on' with 'auto_now_add=True' to post without a default; the database needs something to populate existing rows.

 1) Provide a one-off default now (will be set on all existing rows)
 2) Quit, and let me add a default in models.py
Select an option: 1
Please enter the default value now, as valid Python
You can accept the default 'timezone.now' by pressing 'Enter' or you can provide another value.
The datetime and django.utils.timezone modules are available, so you can do e.g. timezone.now
Type 'exit' to exit this prompt
[default: timezone.now] >>> timezone.now()
You are trying to add a non-nullable field 'slug' to post without a default; we can't do that (the database needs something to populate existing rows).
Please select a fix:
 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
 2) Quit, and let me add a default in models.py
Select an option: 1
Please enter the default value now, as valid Python
The datetime and django.utils.timezone modules are available, so you can do e.g. timezone.now
Type 'exit' to exit this prompt
>>> timezone.now()
You are trying to add a non-nullable field 'title' to post without a default; we can't do that (the database needs something to populate existing rows).
Please select a fix:
 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
 2) Quit, and let me add a default in models.py
Select an option: 1
Please enter the default value now, as valid Python
The datetime and django.utils.timezone modules are available, so you can do e.g. timezone.now
Type 'exit' to exit this prompt
>>> timezone.now()
Migrations for 'Your_Thoughts':
  Your_Thoughts/migrations/0002_auto_20220323_0645.py
    - Change Meta options on post
    - Add field author to post
    - Add field content to post
    - Add field created_on to post
    - Add field excerpt to post
    - Add field featured_image to post
    - Add field likes to post
    - Add field slug to post
    - Add field status to post
    - Add field title to post
    - Add field updated_on to post
    - Create model Comment

### DEBUG_Steps: 1, CLI_Input 2Error, 3Search_String, 4Reference, 5Content, 6Action, 7Result
- `python3 manage.py migrate`
- For Error see below
- `ValueError: Field 'id' expected a number but got 'author'.` 
- [ValueError: Field 'id' expected a number but got 'Processing'](https://stackoverflow.com/questions/59266635/valueerror-field-id-expected-a-number-but-got-processing)
- `Just delete all the migration files except the init python file the run python manage.py makemigrations then python manage.py migrate`
- Deleted migration files
- New error after ong print out of error below, referred to above

- Error:
Operations to perform:
  Apply all migrations: Your_Thoughts, admin, auth, contenttypes, sessions
Running migrations:
  Applying Your_Thoughts.0002_auto_20220323_0645...Traceback (most recent call last):
  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/db/models/fields/__init__.py", line 1823, in get_prep_value
    return int(value)
ValueError: invalid literal for int() with base 10: 'author'

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "manage.py", line 22, in <module>
    main()
  File "manage.py", line 18, in main
    execute_from_command_line(sys.argv)
  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/core/management/__init__.py", line 419, in execute_from_command_line
    utility.execute()
  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/core/management/__init__.py", line 413, in execute
    self.fetch_command(subcommand).run_from_argv(self.argv)
  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/core/management/base.py", line 354, in run_from_argv
    self.execute(*args, **cmd_options)
  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/core/management/base.py", line 398, in execute
    output = self.handle(*args, **options)
  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/core/management/base.py", line 89, in wrapped
    res = handle_func(*args, **kwargs)
  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/core/management/commands/migrate.py", line 244, in handle
    post_migrate_state = executor.migrate(
  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/db/migrations/executor.py", line 117, in migrate
    state = self._migrate_all_forwards(state, plan, full_plan, fake=fake, fake_initial=fake_initial)
  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/db/migrations/executor.py", line 147, in _migrate_all_forwards
    state = self.apply_migration(state, migration, fake=fake, fake_initial=fake_initial)
  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/db/migrations/executor.py", line 227, in apply_migration
    state = migration.apply(state, schema_editor)
  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/db/migrations/migration.py", line 126, in apply
    operation.database_forwards(self.app_label, schema_editor, old_state, project_state)
  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/db/migrations/operations/fields.py", line 104, in database_forwards
    schema_editor.add_field(
  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/db/backends/sqlite3/schema.py", line 330, in add_field
    self._remake_table(model, create_field=field)
  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/db/backends/sqlite3/schema.py", line 191, in _remake_table
    self.effective_default(create_field)
  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/db/backends/base/schema.py", line 310, in effective_default
    return field.get_db_prep_save(self._effective_default(field), self.connection)
  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/db/models/fields/related.py", line 971, in get_db_prep_save
    return self.target_field.get_db_prep_save(value, connection=connection)
  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/db/models/fields/__init__.py", line 842, in get_db_prep_save
    return self.get_db_prep_value(value, connection=connection, prepared=False)
  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/db/models/fields/__init__.py", line 2486, in get_db_prep_value
    value = self.get_prep_value(value)
  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/db/models/fields/__init__.py", line 1825, in get_prep_value
    raise e.__class__(
ValueError: Field 'id' expected a number but got 'author'.

### DEBUG_Steps: 1, CLI_Input 2Error, 3Search_String, 4Reference, 5Content, 6Action, 7Result
- `python3 manage.py makemigrations`
  `python3 manage.py migrate`
- For Error see below
- `raise IntegrityError( django.db.utils.IntegrityError: The row in table 'Your_Thoughts_post' with primary key '4' has an invalid foreign key: Your_Thoughts_post.author_id contains a value '0' that does not have a corresponding value in auth_user.id.` 
- [django.db.utils.IntegrityError: The row in table 'main_page_projects' with primary key '1' has an invalid foreign key](https://stackoverflow.com/questions/71083957/django-db-utils-integrityerror-the-row-in-table-main-page-projects-with-prima)
- ```You can not create an entry in a database table (or modify one by adding a field via migrations) with a ForeignKey that points to a non existing entry on the target table ("Profile" in your case). It does not make sense - so you get the integrity error. Leave away the default=1 and make it "blank=True, null=True" so you can leave it empty upon creation or during migration.```
- Result
  - Key quote for determining next move:
    - `ForeignKey that points to a non existing entry on the target table`
  - Find ForeignKeys:
    - `author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts", default=0)`
    - `post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')`
  - reinspect terminal
    - `django.db.utils.IntegrityError`
      - `django.db.utils.IntegrityError: The row in table 'Your_Thoughts_post' with primary key '4' has an invalid foreign key: Your_Thoughts_post.author_id contains a value '0' that does not have a corresponding value in auth_user.id.`
      - `author_id contains a value '0'`
      - find author_id
        - ` author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts", default=0)`
            - secondary importance:
            - ` created_on = models.DateTimeField(auto_now_add=True) #, default='author'`
            - move discussion / Log to TERMINAL-LOGS2.md
- Error:

```
Running migrations:
  Applying Your_Thoughts.0002_auto_20220323_0729...Traceback (most recent call last):
  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/db/backends/utils.py", line 84, in _execute
    return self.cursor.execute(sql, params)
  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/db/backends/sqlite3/base.py", line 423, in execute
    return Database.Cursor.execute(self, query, params)
sqlite3.IntegrityError: UNIQUE constraint failed: new__Your_Thoughts_post.slug

The above exception was the direct cause of the following exception:

Traceback (most recent call last):
  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/db/migrations/executor.py", line 227, in apply_migration
    state = migration.apply(state, schema_editor)
  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/db/migrations/migration.py", line 126, in apply
    operation.database_forwards(self.app_label, schema_editor, old_state, project_state)
  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/db/migrations/operations/fields.py", line 104, in database_forwards
    schema_editor.add_field(
  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/db/backends/sqlite3/schema.py", line 330, in add_field
    self._remake_table(model, create_field=field)
  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/db/backends/sqlite3/schema.py", line 285, in _remake_table
    self.execute("INSERT INTO %s (%s) SELECT %s FROM %s" % (
  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/db/backends/base/schema.py", line 145, in execute
    cursor.execute(sql, params)
  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/db/backends/utils.py", line 98, in execute
    return super().execute(sql, params)
  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/db/backends/utils.py", line 66, in execute
    return self._execute_with_wrappers(sql, params, many=False, executor=self._execute)
  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/db/backends/utils.py", line 75, in _execute_with_wrappers
    return executor(sql, params, many, context)
  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/db/backends/utils.py", line 84, in _execute
    return self.cursor.execute(sql, params)
  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/db/utils.py", line 90, in __exit__
    raise dj_exc_value.with_traceback(traceback) from exc_value
  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/db/backends/utils.py", line 84, in _execute
    return self.cursor.execute(sql, params)
  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/db/backends/sqlite3/base.py", line 423, in execute
    return Database.Cursor.execute(self, query, params)
django.db.utils.IntegrityError: UNIQUE constraint failed: new__Your_Thoughts_post.slug

During handling of the above exception, another exception occurred:

Traceback (most recent call last):
  File "manage.py", line 22, in <module>
    main()
  File "manage.py", line 18, in main
    execute_from_command_line(sys.argv)
  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/core/management/__init__.py", line 419, in execute_from_command_line
    utility.execute()
  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/core/management/__init__.py", line 413, in execute
    self.fetch_command(subcommand).run_from_argv(self.argv)
  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/core/management/base.py", line 354, in run_from_argv
    self.execute(*args, **cmd_options)
  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/core/management/base.py", line 398, in execute
    output = self.handle(*args, **options)
  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/core/management/base.py", line 89, in wrapped
    res = handle_func(*args, **kwargs)
  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/core/management/commands/migrate.py", line 244, in handle
    post_migrate_state = executor.migrate(
  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/db/migrations/executor.py", line 117, in migrate
    state = self._migrate_all_forwards(state, plan, full_plan, fake=fake, fake_initial=fake_initial)
  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/db/migrations/executor.py", line 147, in _migrate_all_forwards
    state = self.apply_migration(state, migration, fake=fake, fake_initial=fake_initial)
  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/db/migrations/executor.py", line 230, in apply_migration
    migration_recorded = True
  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/db/backends/sqlite3/schema.py", line 35, in __exit__
    self.connection.check_constraints()
  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/db/backends/sqlite3/base.py", line 353, in check_constraints
    raise IntegrityError(
django.db.utils.IntegrityError: The row in table 'Your_Thoughts_post' with primary key '4' has an invalid foreign key: Your_Thoughts_post.author_id contains a value '0' that does not have a corresponding value in auth_user.id.
```