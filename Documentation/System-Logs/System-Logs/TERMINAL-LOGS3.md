gitpod /workspace/Portfolio-Project-4 (main) $ git diff 53238b56f515120dc2e50bebd4b8c85e70694a61..2270ef64781ec97e58912f64f9cddde3b19eab11
diff --git a/Documentation/System-Logs/System-Logs/TERMINAL-LOGS.md b/Documentation/System-Logs/System-Logs/TERMINAL-LOGS.md
deleted file mode 100644
index 2e5d3d2..0000000
--- a/Documentation/System-Logs/System-Logs/TERMINAL-LOGS.md
+++ /dev/null
@@ -1,414 +0,0 @@
-## Command
-pip3 install Django==3.2
-## Output
-Collecting Django==3.2
-  Downloading Django-3.2-py3-none-any.whl (7.9 MB)
-     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 7.9/7.9 MB 30.1 MB/s eta 0:00:00
-Collecting sqlparse>=0.2.2
-  Downloading sqlparse-0.4.2-py3-none-any.whl (42 kB)
-     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 42.3/42.3 KB 11.3 MB/s eta 0:00:00
-Collecting pytz
-  Downloading pytz-2021.3-py2.py3-none-any.whl (503 kB)
-     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 503.5/503.5 KB 23.2 MB/s eta 0:00:00
-Collecting asgiref<4,>=3.3.2
-  Downloading asgiref-3.5.0-py3-none-any.whl (22 kB)
-Installing collected packages: pytz, sqlparse, asgiref, Django
-Successfully installed Django-3.2 asgiref-3.5.0 pytz-2021.3 sqlparse-0.4.2
-
-## Command
-python3 manage.py runserver
-
-## Output
-Watching for file changes with StatReloader
-Performing system checks...
-
-System check identified no issues (0 silenced).
-
-You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): adm
in, auth, contenttypes, sessions.
-Run 'python manage.py migrate' to apply them.
-March 19, 2022 - 09:29:09
-Django version 3.2, using settings 'Profile_Project_4.settings'
-Starting development server at http://127.0.0.1:8000/
-Quit the server with CONTROL-C.Watching for file changes with StatReloader
-Performing system checks...
-
-System check identified no issues (0 silenced).
-
-You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): adm
in, auth, contenttypes, sessions.
-Run 'python manage.py migrate' to apply them.
-March 19, 2022 - 09:29:09
-Django version 3.2, using settings 'Profile_Project_4.settings'
-Starting development server at http://127.0.0.1:8000/
-Quit the server with CONTROL-C.
-
-## Command
-
-```
-python manage.py migrate
-```
-
-## Output
-
-```
-Traceback (most recent call last):
-  File "manage.py", line 22, in <module>
-    main()
-  File "manage.py", line 18, in main
-    execute_from_command_line(sys.argv)
-  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/core/management/__init__.py", line 419, in execute
_from_command_line
-    utility.execute()
-  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/core/management/__init__.py", line 395, in execute
-    django.setup()
-  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/__init__.py", line 24, in setup
-    apps.populate(settings.INSTALLED_APPS)
-  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/apps/registry.py", line 91, in populate
-    app_config = AppConfig.create(entry)
-  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/apps/config.py", line 224, in create
-    import_module(entry)
-  File "/home/gitpod/.pyenv/versions/3.8.11/lib/python3.8/importlib/__init__.py", line 127, in import_module
-    return _bootstrap._gcd_import(name[level:], package, level)
-  File "<frozen importlib._bootstrap>", line 1014, in _gcd_import
-  File "<frozen importlib._bootstrap>", line 991, in _find_and_load
-  File "<frozen importlib._bootstrap>", line 973, in _find_and_load_unlocked
-ModuleNotFoundError: No module named 'todo'
-```
-
-## Command
-
-```
-python3 manage.py runserver
-```
-
-## Output
-Watching for file changes with StatReloader
-Exception in thread django-main-thread:
-Traceback (most recent call last):
-  File "/home/gitpod/.pyenv/versions/3.8.11/lib/python3.8/threading.py", line 932, in _bootstrap_inner
-    self.run()
-  File "/home/gitpod/.pyenv/versions/3.8.11/lib/python3.8/threading.py", line 870, in run
-    self._target(*self._args, **self._kwargs)
-  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/utils/autoreload.py", line 64, in wrapper
-    fn(*args, **kwargs)
-  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/core/management/commands/runserver.py", line 110, 
in inner_run
-    autoreload.raise_last_exception()
-  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/utils/autoreload.py", line 87, in raise_last_excep
tion
-    raise _exception[1]
-  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/core/management/__init__.py", line 375, in execute
-    autoreload.check_errors(django.setup)()
-  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/utils/autoreload.py", line 64, in wrapper
-    fn(*args, **kwargs)
-  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/__init__.py", line 24, in setup
-    apps.populate(settings.INSTALLED_APPS)
-  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/apps/registry.py", line 91, in populate
-    app_config = AppConfig.create(entry)
-  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/apps/config.py", line 224, in create
-    import_module(entry)
-  File "/home/gitpod/.pyenv/versions/3.8.11/lib/python3.8/importlib/__init__.py", line 127, in import_module
-    return _bootstrap._gcd_import(name[level:], package, level)
-  File "<frozen importlib._bootstrap>", line 1014, in _gcd_import
-  File "<frozen importlib._bootstrap>", line 991, in _find_and_load
-  File "<frozen importlib._bootstrap>", line 973, in _find_and_load_unlocked
-ModuleNotFoundError: No module named 'todo'
-
-## Reran command in CLI:
-
-```
-python3 manage.py runserver
-```
-
-### Output
-Watching for file changes with StatReloader
-Exception in thread django-main-thread:
-Traceback (most recent call last):
-  File "/home/gitpod/.pyenv/versions/3.8.11/lib/python3.8/threading.py", line 932, in _bootstrap_inner
-    self.run()
-  File "/home/gitpod/.pyenv/versions/3.8.11/lib/python3.8/threading.py", line 870, in run
-    self._target(*self._args, **self._kwargs)
-  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/utils/autoreload.py", line 64, in wrapper
-    fn(*args, **kwargs)
-  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/core/management/commands/runserver.py", line 110, 
in inner_run
-    autoreload.raise_last_exception()
-  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/utils/autoreload.py", line 87, in raise_last_excep
tion
-    raise _exception[1]
-  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/core/management/__init__.py", line 375, in execute
-    autoreload.check_errors(django.setup)()
-  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/utils/autoreload.py", line 64, in wrapper
-    fn(*args, **kwargs)
-  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/__init__.py", line 24, in setup
-    apps.populate(settings.INSTALLED_APPS)
-  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/apps/registry.py", line 91, in populate
-    app_config = AppConfig.create(entry)
-  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/apps/config.py", line 224, in create
-    import_module(entry)
-  File "/home/gitpod/.pyenv/versions/3.8.11/lib/python3.8/importlib/__init__.py", line 127, in import_module
-    return _bootstrap._gcd_import(name[level:], package, level)
-  File "<frozen importlib._bootstrap>", line 1014, in _gcd_import
-  File "<frozen importlib._bootstrap>", line 991, in _find_and_load
-  File "<frozen importlib._bootstrap>", line 973, in _find_and_load_unlocked
-ModuleNotFoundError: No module named 'todo'
-
-## CLI input
-`python3 manage.py makemigrations`
-
-- get rid of default value as mutually exclusive with auto_now and other auto_ setting(s).
-
-- However, due to issue at time of running above migration command: 
-
-- need to remove default value in code, to avoid error,
-
-- then set value to `timezone.now()` when prompted while above migration commmand running.
-
-## Debug
-### Search String
-
-```
-SystemCheckError: System check identified some issues: ERRORS: Your_Thoughts.Post.created_on: (fields.E160) The optio
ns auto_now, auto_now_add, and default are mutually exclusive. Only one of these options may be present.
-```
-
-### Reference
-- [The options auto_now, auto_now_add, and default are mutually exclusive. Only one of these options may be present](
https://stackoverflow.com/questions/45874365/the-options-auto-now-auto-now-add-and-default-are-mutually-exclusive-only
-one)
-
-### Content
-
-```
-Just use:
-
-class Users(models.Model):
-    ctime = models.DateTimeField(auto_now_add=True)
-    uptime = models.DateTimeField(auto_now=True)
-It will work.
-
-Explanation:
-
-These both are mutually exclusive means you should use only one of them, not both.
-```
-
-#### Solution to problem:
-##### Search String
-
-```
-field 'created_on' with 'auto_now_add=True' to post without a default; the database needs something to populate exist
ing rows.  SystemCheckError: System check identified some issues: ERRORS: Your_Thoughts.Post.created_on: (fields.E160)
 The options auto_now, auto_now_add, and default are mutually exclusive. Only one of these options may be present.
-```
-
-##### Reference
-- [Django DateTimeField with auto_now_add asks for default](https://stackoverflow.com/questions/56310322/django-datet
imefield-with-auto-now-add-asks-for-default)
-##### Content
-
-```
-You have already some rows without created_at value. But when you added following field and run migration
-
-created_at = models.DateTimeField( auto_now_add = True)
-It expects the existing row has created_at value. So, It warns you at the time of migrations.
-
-To solve this problem. You can choose the 1st option which says Provide a one-off default now (will be set on all exi
sting rows). By choosing the 1st option you are asking for value. Here you can enter timezone.now(). It will populate 
existing rows with the current timestamp.
-```
-
-## CLI Output
-gitpod /workspace/Portfolio-Project-4 (main) $ python3 manage.py makemigrations
-
-SystemCheckError: System check identified some issues:
-
-ERRORS:
-Your_Thoughts.Post.created_on: (fields.E160) The options auto_now, auto_now_add, and default are mutually exclusive. 
Only one of these options may be present.
-gitpod /workspace/Portfolio-Project-4 (main) $ python3 manage.py makemigrations
-You are trying to add the field 'created_on' with 'auto_now_add=True' to post without a default; the database needs s
omething to populate existing rows.
-
- 1) Provide a one-off default now (will be set on all existing rows)
- 2) Quit, and let me add a default in models.py
-Select an option: 1
-Please enter the default value now, as valid Python
-You can accept the default 'timezone.now' by pressing 'Enter' or you can provide another value.
-The datetime and django.utils.timezone modules are available, so you can do e.g. timezone.now
-Type 'exit' to exit this prompt
-[default: timezone.now] >>> timezone.now()
-You are trying to add a non-nullable field 'slug' to post without a default; we can't do that (the database needs som
ething to populate existing rows).
-Please select a fix:
- 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
- 2) Quit, and let me add a default in models.py
-Select an option: 1
-Please enter the default value now, as valid Python
-The datetime and django.utils.timezone modules are available, so you can do e.g. timezone.now
-Type 'exit' to exit this prompt
->>> timezone.now()
-You are trying to add a non-nullable field 'title' to post without a default; we can't do that (the database needs so
mething to populate existing rows).
-Please select a fix:
- 1) Provide a one-off default now (will be set on all existing rows with a null value for this column)
- 2) Quit, and let me add a default in models.py
-Select an option: 1
-Please enter the default value now, as valid Python
-The datetime and django.utils.timezone modules are available, so you can do e.g. timezone.now
-Type 'exit' to exit this prompt
->>> timezone.now()
-Migrations for 'Your_Thoughts':
-  Your_Thoughts/migrations/0002_auto_20220323_0645.py
-    - Change Meta options on post
-    - Add field author to post
-    - Add field content to post
-    - Add field created_on to post
-    - Add field excerpt to post
-    - Add field featured_image to post
-    - Add field likes to post
-    - Add field slug to post
-    - Add field status to post
-    - Add field title to post
-    - Add field updated_on to post
-    - Create model Comment
-
-### DEBUG_Steps: 1, CLI_Input 2Error, 3Search_String, 4Reference, 5Content, 6Action, 7Result
-- `python3 manage.py migrate`
-- For Error see below
-- `ValueError: Field 'id' expected a number but got 'author'.` 
-- [ValueError: Field 'id' expected a number but got 'Processing'](https://stackoverflow.com/questions/59266635/valuee
rror-field-id-expected-a-number-but-got-processing)
-- `Just delete all the migration files except the init python file the run python manage.py makemigrations then pytho
n manage.py migrate`
-- Deleted migration files
-- New error after ong print out of error below, referred to above
-
-- Error:
-Operations to perform:
-  Apply all migrations: Your_Thoughts, admin, auth, contenttypes, sessions
-Running migrations:
-  Applying Your_Thoughts.0002_auto_20220323_0645...Traceback (most recent call last):
-  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/db/models/fields/__init__.py", line 1823, in get_p
rep_value
-    return int(value)
-ValueError: invalid literal for int() with base 10: 'author'
-
-The above exception was the direct cause of the following exception:
-
-Traceback (most recent call last):
-  File "manage.py", line 22, in <module>
-    main()
-  File "manage.py", line 18, in main
-    execute_from_command_line(sys.argv)
-  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/core/management/__init__.py", line 419, in execute
_from_command_line
-    utility.execute()
-  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/core/management/__init__.py", line 413, in execute
-    self.fetch_command(subcommand).run_from_argv(self.argv)
-  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/core/management/base.py", line 354, in run_from_ar
gv
-    self.execute(*args, **cmd_options)
-  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/core/management/base.py", line 398, in execute
-    output = self.handle(*args, **options)
-  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/core/management/base.py", line 89, in wrapped
-    res = handle_func(*args, **kwargs)
-  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/core/management/commands/migrate.py", line 244, in
 handle
-    post_migrate_state = executor.migrate(
-  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/db/migrations/executor.py", line 117, in migrate
-    state = self._migrate_all_forwards(state, plan, full_plan, fake=fake, fake_initial=fake_initial)
-  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/db/migrations/executor.py", line 147, in _migrate_
all_forwards
-    state = self.apply_migration(state, migration, fake=fake, fake_initial=fake_initial)
-  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/db/migrations/executor.py", line 227, in apply_mig
ration
-    state = migration.apply(state, schema_editor)
-  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/db/migrations/migration.py", line 126, in apply
-    operation.database_forwards(self.app_label, schema_editor, old_state, project_state)
-  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/db/migrations/operations/fields.py", line 104, in 
database_forwards
-    schema_editor.add_field(
-  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/db/backends/sqlite3/schema.py", line 330, in add_f
ield
-    self._remake_table(model, create_field=field)
-  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/db/backends/sqlite3/schema.py", line 191, in _rema
ke_table
-    self.effective_default(create_field)
-  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/db/backends/base/schema.py", line 310, in effectiv
e_default
-    return field.get_db_prep_save(self._effective_default(field), self.connection)
-  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/db/models/fields/related.py", line 971, in get_db_
prep_save
-    return self.target_field.get_db_prep_save(value, connection=connection)
-  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/db/models/fields/__init__.py", line 842, in get_db
_prep_save
-    return self.get_db_prep_value(value, connection=connection, prepared=False)
-  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/db/models/fields/__init__.py", line 2486, in get_d
b_prep_value
-    value = self.get_prep_value(value)
-  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/db/models/fields/__init__.py", line 1825, in get_p
rep_value
-    raise e.__class__(
-ValueError: Field 'id' expected a number but got 'author'.
-
-### DEBUG_Steps: 1, CLI_Input 2Error, 3Search_String, 4Reference, 5Content, 6Action, 7Result
-- `python3 manage.py makemigrations`
-  `python3 manage.py migrate`
-- For Error see below
-- `raise IntegrityError( django.db.utils.IntegrityError: The row in table 'Your_Thoughts_post' with primary key '4' h
as an invalid foreign key: Your_Thoughts_post.author_id contains a value '0' that does not have a corresponding value 
in auth_user.id.` 
-- [django.db.utils.IntegrityError: The row in table 'main_page_projects' with primary key '1' has an invalid foreign 
key](https://stackoverflow.com/questions/71083957/django-db-utils-integrityerror-the-row-in-table-main-page-projects-w
ith-prima)
-- ```You can not create an entry in a database table (or modify one by adding a field via migrations) with a ForeignK
ey that points to a non existing entry on the target table ("Profile" in your case). It does not make sense - so you g
et the integrity error. Leave away the default=1 and make it "blank=True, null=True" so you can leave it empty upon cr
eation or during migration.```
-- Result
-  - Key quote for determining next move:
-    - `ForeignKey that points to a non existing entry on the target table`
-  - Find ForeignKeys:
-    - `author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts", default=0)`
-    - `post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')`
-  - reinspect terminal
-    - `django.db.utils.IntegrityError`
-      - `django.db.utils.IntegrityError: The row in table 'Your_Thoughts_post' with primary key '4' has an invalid fo
reign key: Your_Thoughts_post.author_id contains a value '0' that does not have a corresponding value in auth_user.id.
`
-      - `author_id contains a value '0'`
-      - find author_id
-        - ` author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts", default=0)`
-            - secondary importance:
-            - ` created_on = models.DateTimeField(auto_now_add=True) #, default='author'`
-            - move discussion / Log to TERMINAL-LOGS2.md
-- Error:
-
-```
-Running migrations:
-  Applying Your_Thoughts.0002_auto_20220323_0729...Traceback (most recent call last):
-  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/db/backends/utils.py", line 84, in _execute
-    return self.cursor.execute(sql, params)
-  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/db/backends/sqlite3/base.py", line 423, in execute
-    return Database.Cursor.execute(self, query, params)
-sqlite3.IntegrityError: UNIQUE constraint failed: new__Your_Thoughts_post.slug
-
-The above exception was the direct cause of the following exception:
-
-Traceback (most recent call last):
-  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/db/migrations/executor.py", line 227, in apply_mig
ration
-    state = migration.apply(state, schema_editor)
-  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/db/migrations/migration.py", line 126, in apply
-    operation.database_forwards(self.app_label, schema_editor, old_state, project_state)
-  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/db/migrations/operations/fields.py", line 104, in 
database_forwards
-    schema_editor.add_field(
-  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/db/backends/sqlite3/schema.py", line 330, in add_f
ield
-    self._remake_table(model, create_field=field)
-  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/db/backends/sqlite3/schema.py", line 285, in _rema
ke_table
-    self.execute("INSERT INTO %s (%s) SELECT %s FROM %s" % (
-  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/db/backends/base/schema.py", line 145, in execute
-    cursor.execute(sql, params)
-  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/db/backends/utils.py", line 98, in execute
-    return super().execute(sql, params)
-  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/db/backends/utils.py", line 66, in execute
-    return self._execute_with_wrappers(sql, params, many=False, executor=self._execute)
-  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/db/backends/utils.py", line 75, in _execute_with_w
rappers
-    return executor(sql, params, many, context)
-  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/db/backends/utils.py", line 84, in _execute
-    return self.cursor.execute(sql, params)
-  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/db/utils.py", line 90, in __exit__
-    raise dj_exc_value.with_traceback(traceback) from exc_value
-  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/db/backends/utils.py", line 84, in _execute
-    return self.cursor.execute(sql, params)
-  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/db/backends/sqlite3/base.py", line 423, in execute
-    return Database.Cursor.execute(self, query, params)
-django.db.utils.IntegrityError: UNIQUE constraint failed: new__Your_Thoughts_post.slug
-
-During handling of the above exception, another exception occurred:
-
-Traceback (most recent call last):
-  File "manage.py", line 22, in <module>
-    main()
-  File "manage.py", line 18, in main
-    execute_from_command_line(sys.argv)
-  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/core/management/__init__.py", line 419, in execute
_from_command_line
-    utility.execute()
-  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/core/management/__init__.py", line 413, in execute
-    self.fetch_command(subcommand).run_from_argv(self.argv)
-  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/core/management/base.py", line 354, in run_from_ar
gv
-    self.execute(*args, **cmd_options)
-  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/core/management/base.py", line 398, in execute
-    output = self.handle(*args, **options)
-  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/core/management/base.py", line 89, in wrapped
-    res = handle_func(*args, **kwargs)
-  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/core/management/commands/migrate.py", line 244, in
 handle
-    post_migrate_state = executor.migrate(
-  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/db/migrations/executor.py", line 117, in migrate
-    state = self._migrate_all_forwards(state, plan, full_plan, fake=fake, fake_initial=fake_initial)
-  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/db/migrations/executor.py", line 147, in _migrate_
all_forwards
-    state = self.apply_migration(state, migration, fake=fake, fake_initial=fake_initial)
-  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/db/migrations/executor.py", line 230, in apply_mig
ration
-    migration_recorded = True
-  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/db/backends/sqlite3/schema.py", line 35, in __exit
__
-    self.connection.check_constraints()
-  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/db/backends/sqlite3/base.py", line 353, in check_c
onstraints
-    raise IntegrityError(
-django.db.utils.IntegrityError: The row in table 'Your_Thoughts_post' with primary key '4' has an invalid foreign key
: Your_Thoughts_post.author_id contains a value '0' that does not have a corresponding value in auth_user.id.
-```
\ No newline at end of file
diff --git a/Documentation/System-Logs/System-Logs/TERMINAL-LOGS2.md b/Documentation/System-Logs/System-Logs/TERMINAL-
LOGS2.md
deleted file mode 100644
index 5304333..0000000
--- a/Documentation/System-Logs/System-Logs/TERMINAL-LOGS2.md
+++ /dev/null
@@ -1,115 +0,0 @@
-from TERMINAL-LOGS.md
-
-- author
-- possibly setting initial value for migrate command to timezone.now() is causing error.
-- find Your_Thoughts_post in models.py
-- not found
-- find post in Your_Thoughts / migrations / models.py
-    - `class Post(models.Model):`
-    - `author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts", default=0)`
-    - `post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')`
-- review 3 found post code lines above
-    - combined with earlier author point in TERMINAL-LOGS.md
-    - line with both post and author:
-        - `author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts", default=0)`
-- set above line default to 1, like so:
-    - `author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts", default=1)`
-
-- run
-    - `python3 manage.py makemigrations`
-    - `python3 manage.py migrate`
-- last 3 lines of output:
-
-```
-    raise IntegrityError(
-django.db.utils.IntegrityError: The row in table 'Your_Thoughts_post' with primary key '4' has an invalid foreign key
: Your_Thoughts_post.author_id contains a value '0' that does not have a corresponding value in auth_user.id.
-```
-
-    - from above 3 lines:
-        - find 0's in models.py
-            - 16 found
-        - find =0 in models.py
-            - `content = models.TextField(default=0)`
-            - `status = models.IntegerField(choices=STATUS, default=0)`
-- comment out last lines here listed
-- deleted migrations reran 2 migration commands
-- error:
-
-```
-    File "/workspace/.pip-modules/lib/python3.8/site-packages/django/db/utils.py", line 90, in __exit__
-    raise dj_exc_value.with_traceback(traceback) from exc_value
-  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/db/backends/utils.py", line 84, in _execute
-    return self.cursor.execute(sql, params)
-  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/db/backends/sqlite3/base.py", line 423, in execute
-    return Database.Cursor.execute(self, query, params)
-django.db.utils.IntegrityError: UNIQUE constraint failed: new__Your_Thoughts_post.slug
-```
-
-- comment out:
-    - `django.db.utils.IntegrityError: UNIQUE constraint failed: new__Your_Thoughts_post.slug`
-rerun 2 commands
-- new error:
-- `django.db.utils.IntegrityError: UNIQUE constraint failed: new__Your_Thoughts_post.title`
-- find title in models.py
-- line 19:
-- `    title = models.CharField(max_length=200, unique=True)`
-- comment out line, delete migration, rerun 2 commands
-
-- works
-- terminal output:
-
-```
-Operations to perform:
-  Apply all migrations: Your_Thoughts, admin, auth, contenttypes, sessions
-Running migrations:
-  Applying Your_Thoughts.0002_auto_20220323_1111... OK
-```
-
-- Note changes in form of commented lines
-- also aside:
-    - option 1 selected from terminal when running
-        `python3 manage.py migrate`
-        - that is, set initial value
-        note: timezone.now() used for 3 initial values.
-
-### commented lines in models.py to make migrate command work in terminal:
-Line 19 `    # title = models.CharField(max_length=200, unique=True)`
-Line 31 `    # slug = models.SlugField(max_length=200, unique=True)`
-Line 41 `    # content = models.TextField(default=0)`
-Line 45 `    # status = models.IntegerField(choices=STATUS, default=0)`
-Line 50 `    # created_date = models.DateTimeField(default=timezone.now)`
-
-- Review:
-    - So, lines:
-        - 19 31 41 45 50. So, tens columns are:
-            - 1, 3, 4, 4, 5
-
-
-- uncomment line 19 first line of 5 above (line 1 of 5)
-- delete migrations, rerun migration duo of commands
-
-- first push successful to version control system before trying to reintroduce other partslisted in last 3 lines abov
e here.
-
-## new issue on heroku
- 
-- [heroku app currently shows Server Error 500](https://your-thoughts-app.herokuapp.com/)
-
-- getting 500 Server error
-- found:
-    - [Heroku giving 500 error with little information + Internal Server Error](https://stackoverflow.com/questions/4
6021463/heroku-giving-500-error-with-little-information-internal-server-error)
-- ran:
-    - `heroku logs -t`
-- terminal output
-    - `heroku: Waiting for login... ⣟`
-- from earlier issues with heroku login:
-    - Ctrl + C
-    - switch to:
-        - `heroku login -i`
-
-- still 500 server error after login from GitPod CLI
-- why is this occurring, what is the cause?
-- add issue on GitHub
-- add heroku server live page to GitHub either under issue and / or in commit
-- [heroku live server link](https://git.heroku.com/your-thoughts-app.git)
-- review changes since stopped working on heroku
-- find last working commit, get diff with current commit
diff --git a/Documentation/System-Logs/TERMINAL-LOGS.md b/Documentation/System-Logs/TERMINAL-LOGS.md
new file mode 100644
index 0000000..e254967
--- /dev/null
+++ b/Documentation/System-Logs/TERMINAL-LOGS.md
@@ -0,0 +1,148 @@
+## Command
+pip3 install Django==3.2
+## Output
+Collecting Django==3.2
+  Downloading Django-3.2-py3-none-any.whl (7.9 MB)
+     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 7.9/7.9 MB 30.1 MB/s eta 0:00:00
+Collecting sqlparse>=0.2.2
+  Downloading sqlparse-0.4.2-py3-none-any.whl (42 kB)
+     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 42.3/42.3 KB 11.3 MB/s eta 0:00:00
+Collecting pytz
+  Downloading pytz-2021.3-py2.py3-none-any.whl (503 kB)
+     ━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━━ 503.5/503.5 KB 23.2 MB/s eta 0:00:00
+Collecting asgiref<4,>=3.3.2
+  Downloading asgiref-3.5.0-py3-none-any.whl (22 kB)
+Installing collected packages: pytz, sqlparse, asgiref, Django
+Successfully installed Django-3.2 asgiref-3.5.0 pytz-2021.3 sqlparse-0.4.2
+
+## Command
+python3 manage.py runserver
+
+## Output
+Watching for file changes with StatReloader
+Performing system checks...
+
+System check identified no issues (0 silenced).
+
+You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): adm
in, auth, contenttypes, sessions.
+Run 'python manage.py migrate' to apply them.
+March 19, 2022 - 09:29:09
+Django version 3.2, using settings 'Profile_Project_4.settings'
+Starting development server at http://127.0.0.1:8000/
+Quit the server with CONTROL-C.Watching for file changes with StatReloader
+Performing system checks...
+
+System check identified no issues (0 silenced).
+
+You have 18 unapplied migration(s). Your project may not work properly until you apply the migrations for app(s): adm
in, auth, contenttypes, sessions.
+Run 'python manage.py migrate' to apply them.
+March 19, 2022 - 09:29:09
+Django version 3.2, using settings 'Profile_Project_4.settings'
+Starting development server at http://127.0.0.1:8000/
+Quit the server with CONTROL-C.
+
+## Command
+
+```
+python manage.py migrate
+```
+
+## Output
+
+```
+Traceback (most recent call last):
+  File "manage.py", line 22, in <module>
+    main()
+  File "manage.py", line 18, in main
+    execute_from_command_line(sys.argv)
+  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/core/management/__init__.py", line 419, in execute
_from_command_line
+    utility.execute()
+  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/core/management/__init__.py", line 395, in execute
+    django.setup()
+  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/__init__.py", line 24, in setup
+    apps.populate(settings.INSTALLED_APPS)
+  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/apps/registry.py", line 91, in populate
+    app_config = AppConfig.create(entry)
+  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/apps/config.py", line 224, in create
+    import_module(entry)
+  File "/home/gitpod/.pyenv/versions/3.8.11/lib/python3.8/importlib/__init__.py", line 127, in import_module
+    return _bootstrap._gcd_import(name[level:], package, level)
+  File "<frozen importlib._bootstrap>", line 1014, in _gcd_import
+  File "<frozen importlib._bootstrap>", line 991, in _find_and_load
+  File "<frozen importlib._bootstrap>", line 973, in _find_and_load_unlocked
+ModuleNotFoundError: No module named 'todo'
+```
+
+## Command
+
+```
+python3 manage.py runserver
+```
+
+## Output
+Watching for file changes with StatReloader
+Exception in thread django-main-thread:
+Traceback (most recent call last):
+  File "/home/gitpod/.pyenv/versions/3.8.11/lib/python3.8/threading.py", line 932, in _bootstrap_inner
+    self.run()
+  File "/home/gitpod/.pyenv/versions/3.8.11/lib/python3.8/threading.py", line 870, in run
+    self._target(*self._args, **self._kwargs)
+  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/utils/autoreload.py", line 64, in wrapper
+    fn(*args, **kwargs)
+  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/core/management/commands/runserver.py", line 110, 
in inner_run
+    autoreload.raise_last_exception()
+  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/utils/autoreload.py", line 87, in raise_last_excep
tion
+    raise _exception[1]
+  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/core/management/__init__.py", line 375, in execute
+    autoreload.check_errors(django.setup)()
+  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/utils/autoreload.py", line 64, in wrapper
+    fn(*args, **kwargs)
+  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/__init__.py", line 24, in setup
+    apps.populate(settings.INSTALLED_APPS)
+  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/apps/registry.py", line 91, in populate
+    app_config = AppConfig.create(entry)
+  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/apps/config.py", line 224, in create
+    import_module(entry)
+  File "/home/gitpod/.pyenv/versions/3.8.11/lib/python3.8/importlib/__init__.py", line 127, in import_module
+    return _bootstrap._gcd_import(name[level:], package, level)
+  File "<frozen importlib._bootstrap>", line 1014, in _gcd_import
+  File "<frozen importlib._bootstrap>", line 991, in _find_and_load
+  File "<frozen importlib._bootstrap>", line 973, in _find_and_load_unlocked
+ModuleNotFoundError: No module named 'todo'
+
+## Reran command in CLI:
+
+```
+python3 manage.py runserver
+```
+
+### Output
+Watching for file changes with StatReloader
+Exception in thread django-main-thread:
+Traceback (most recent call last):
+  File "/home/gitpod/.pyenv/versions/3.8.11/lib/python3.8/threading.py", line 932, in _bootstrap_inner
+    self.run()
+  File "/home/gitpod/.pyenv/versions/3.8.11/lib/python3.8/threading.py", line 870, in run
+    self._target(*self._args, **self._kwargs)
+  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/utils/autoreload.py", line 64, in wrapper
+    fn(*args, **kwargs)
+  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/core/management/commands/runserver.py", line 110, 
in inner_run
+    autoreload.raise_last_exception()
+  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/utils/autoreload.py", line 87, in raise_last_excep
tion
+    raise _exception[1]
+  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/core/management/__init__.py", line 375, in execute
+    autoreload.check_errors(django.setup)()
+  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/utils/autoreload.py", line 64, in wrapper
+    fn(*args, **kwargs)
+  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/__init__.py", line 24, in setup
+    apps.populate(settings.INSTALLED_APPS)
+  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/apps/registry.py", line 91, in populate
+    app_config = AppConfig.create(entry)
+  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/apps/config.py", line 224, in create
+    import_module(entry)
+  File "/home/gitpod/.pyenv/versions/3.8.11/lib/python3.8/importlib/__init__.py", line 127, in import_module
+    return _bootstrap._gcd_import(name[level:], package, level)
+  File "<frozen importlib._bootstrap>", line 1014, in _gcd_import
+  File "<frozen importlib._bootstrap>", line 991, in _find_and_load
+  File "<frozen importlib._bootstrap>", line 973, in _find_and_load_unlocked
+ModuleNotFoundError: No module named 'todo'
diff --git a/Your_Thoughts/migrations/0002_auto_20220323_1111.py b/Your_Thoughts/migrations/0002_auto_20220323_1111.py
deleted file mode 100644
index 0d1d0b0..0000000
--- a/Your_Thoughts/migrations/0002_auto_20220323_1111.py
+++ /dev/null
@@ -1,69 +0,0 @@
-# Generated by Django 3.2 on 2022-03-23 11:11
-
-import cloudinary.models
-import datetime
-from django.conf import settings
-from django.db import migrations, models
-import django.db.models.deletion
-from django.utils.timezone import utc
-
-
-class Migration(migrations.Migration):
-
-    dependencies = [
-        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
-        ('Your_Thoughts', '0001_initial'),
-    ]
-
-    operations = [
-        migrations.AlterModelOptions(
-            name='post',
-            options={'ordering': ['-created_on']},
-        ),
-        migrations.AddField(
-            model_name='post',
-            name='author',
-            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='blog_posts'
, to=settings.AUTH_USER_MODEL),
-        ),
-        migrations.AddField(
-            model_name='post',
-            name='created_on',
-            field=models.DateTimeField(auto_now_add=True, default=datetime.datetime(2022, 3, 23, 11, 11, 28, 560062, 
tzinfo=utc)),
-            preserve_default=False,
-        ),
-        migrations.AddField(
-            model_name='post',
-            name='excerpt',
-            field=models.TextField(blank=True),
-        ),
-        migrations.AddField(
-            model_name='post',
-            name='featured_image',
-            field=cloudinary.models.CloudinaryField(default='placeholder', max_length=255, verbose_name='image'),
-        ),
-        migrations.AddField(
-            model_name='post',
-            name='likes',
-            field=models.ManyToManyField(blank=True, related_name='blog_likes', to=settings.AUTH_USER_MODEL),
-        ),
-        migrations.AddField(
-            model_name='post',
-            name='updated_on',
-            field=models.DateTimeField(auto_now=True),
-        ),
-        migrations.CreateModel(
-            name='Comment',
-            fields=[
-                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
-                ('name', models.CharField(max_length=80)),
-                ('email', models.EmailField(max_length=254)),
-                ('body', models.TextField()),
-                ('created_on', models.DateTimeField(auto_now_add=True)),
-                ('approved', models.BooleanField(default=False)),
-                ('post', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='comments', to='
Your_Thoughts.post')),
-            ],
-            options={
-                'ordering': ['created_on'],
-            },
-        ),
-    ]
diff --git a/Your_Thoughts/models.py b/Your_Thoughts/models.py
index 7bdb0f2..61ee598 100644
--- a/Your_Thoughts/models.py
+++ b/Your_Thoughts/models.py
@@ -2,12 +2,9 @@
 import models
 """
 from django.db import models
-from django.contrib.auth.models import User
-from cloudinary.models import CloudinaryField  # LMS Django Blog 006b: Building The Models
 
 
 # Create your models here.
-STATUS = ((0, "Draft"), (1, "Published"))  # LMS Django Blog 006b: Building The Models
 
 
 class Post(models.Model):
@@ -15,35 +12,6 @@ class Post(models.Model):
     """
     allows creation of a post with name comment text and Completed fields
     """
-    # LMS Django Blog 006b: Building The Models:
-    # title = models.CharField(max_length=200, unique=True)
-    
-    # Error in terminal: 
-    """You are trying to add a non-nullable field 'author' to post without a default; we can't do that (the database 
needs something to populate existing rows)."""
-    # Solution Reference for subsequent code block
-    # https://stackoverflow.com/questions/26185687/you-are-trying-to-add-a-non-nullable-field-new-field-to-userprofil
e-without-a
-    # You need to provide a default value:
-    # new_field = models.CharField(max_length=140, default='SOME STRING')
-
-
-
-    
-    # slug = models.SlugField(max_length=200, unique=True)
-    author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts", default=1)
-    # above, "on_delete=CASCADE" in Foreign Key
-    # means that if the one record in the 
-    # one-to-many relationship 
-    # is deleted, then the 
-    # related records will be deleted too.
-    # So deleting a user will also 
-    # delete their blog posts.
-    updated_on = models.DateTimeField(auto_now=True)
-    # content = models.TextField(default=0)
-    featured_image = CloudinaryField('image', default='placeholder')
-    excerpt = models.TextField(blank=True)
-    created_on = models.DateTimeField(auto_now_add=True) #, default='author'
-    # status = models.IntegerField(choices=STATUS, default=0)
-    likes = models.ManyToManyField(User, related_name='blog_likes', blank=True)
     name = models.CharField(max_length=50, null=False, blank=False)
     # https://tutorial-extensions.djangogirls.org/en/homework_create_more_models
     comment = models.TextField(null=False, blank=False)
@@ -51,30 +19,9 @@ class Post(models.Model):
     # LMS
     done = models.BooleanField(null=False, blank=False, default=False)
 
-    class Meta:
-        ordering = ['-created_on']
-
     # Note:
     # in
     # PROBLEMS in Console View
     # __str__ does not return str
     def __str__(self):
         return self.name
-
-    def number_of_likes(self):
-        return self.likes.count()
-
-class Comment(models.Model):
-
-    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
-    name = models.CharField(max_length=80)
-    email = models.EmailField()
-    body = models.TextField()
-    created_on = models.DateTimeField(auto_now_add=True)
-    approved = models.BooleanField(default=False)
-
-    class Meta:
-        ordering = ['created_on']
-    
-    def __str__(self):
-        return f"Comment {self.body} by {self.name}"
diff --git a/db.sqlite3 b/db.sqlite3
index a983586..b83bc2d 100644
Binary files a/db.sqlite3 and b/db.sqlite3 differ
(END)