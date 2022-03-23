from TERMINAL-LOGS.md

- author
- possibly setting initial value for migrate command to timezone.now() is causing error.
- find Your_Thoughts_post in models.py
- not found
- find post in Your_Thoughts / migrations / models.py
    - `class Post(models.Model):`
    - `author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts", default=0)`
    - `post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')`
- review 3 found post code lines above
    - combined with earlier author point in TERMINAL-LOGS.md
    - line with both post and author:
        - `author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts", default=0)`
- set above line default to 1, like so:
    - `author = models.ForeignKey(User, on_delete=models.CASCADE, related_name="blog_posts", default=1)`

- run
    - `python3 manage.py makemigrations`
    - `python3 manage.py migrate`
- last 3 lines of output:

```
    raise IntegrityError(
django.db.utils.IntegrityError: The row in table 'Your_Thoughts_post' with primary key '4' has an invalid foreign key: Your_Thoughts_post.author_id contains a value '0' that does not have a corresponding value in auth_user.id.
```

    - from above 3 lines:
        - find 0's in models.py
            - 16 found
        - find =0 in models.py
            - `content = models.TextField(default=0)`
            - `status = models.IntegerField(choices=STATUS, default=0)`
- comment out last lines here listed
- deleted migrations reran 2 migration commands
- error:

```
    File "/workspace/.pip-modules/lib/python3.8/site-packages/django/db/utils.py", line 90, in __exit__
    raise dj_exc_value.with_traceback(traceback) from exc_value
  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/db/backends/utils.py", line 84, in _execute
    return self.cursor.execute(sql, params)
  File "/workspace/.pip-modules/lib/python3.8/site-packages/django/db/backends/sqlite3/base.py", line 423, in execute
    return Database.Cursor.execute(self, query, params)
django.db.utils.IntegrityError: UNIQUE constraint failed: new__Your_Thoughts_post.slug
```

- comment out:
    - `django.db.utils.IntegrityError: UNIQUE constraint failed: new__Your_Thoughts_post.slug`
rerun 2 commands
- new error:
- `django.db.utils.IntegrityError: UNIQUE constraint failed: new__Your_Thoughts_post.title`
- find title in models.py
- line 19:
- `    title = models.CharField(max_length=200, unique=True)`
- comment out line, delete migration, rerun 2 commands

- works
- terminal output:

```
Operations to perform:
  Apply all migrations: Your_Thoughts, admin, auth, contenttypes, sessions
Running migrations:
  Applying Your_Thoughts.0002_auto_20220323_1111... OK
```

- Note changes in form of commented lines
- also aside:
    - option 1 selected from terminal when running
        `python3 manage.py migrate`
        - that is, set initial value
        note: timezone.now() used for 3 initial values.

### commented lines in models.py to make migrate command work in terminal:
Line 19 `    # title = models.CharField(max_length=200, unique=True)`
Line 31 `    # slug = models.SlugField(max_length=200, unique=True)`
Line 41 `    # content = models.TextField(default=0)`
Line 45 `    # status = models.IntegerField(choices=STATUS, default=0)`
Line 50 `    # created_date = models.DateTimeField(default=timezone.now)`

- Review:
    - So, lines:
        - 19 31 41 45 50. So, tens columns are:
            - 1, 3, 4, 4, 5


- uncomment line 19 first line of 5 above (line 1 of 5)
- delete migrations, rerun migration duo of commands

- first push successful to version control system before trying to reintroduce other partslisted in last 3 lines above here.

## new issue on heroku
 
- [heroku app currently shows Server Error 500](https://your-thoughts-app.herokuapp.com/)

- getting 500 Server error
- found:
    - [Heroku giving 500 error with little information + Internal Server Error](https://stackoverflow.com/questions/46021463/heroku-giving-500-error-with-little-information-internal-server-error)
- ran:
    - `heroku logs -t`
- terminal output
    - `heroku: Waiting for login... ⣟`
- from earlier issues with heroku login:
    - Ctrl + C
    - switch to:
        - `heroku login -i`

- still 500 server error after login from GitPod CLI
- why is this occurring, what is the cause?
- add issue on GitHub
- add heroku server live page to GitHub either under issue and / or in commit
- [heroku live server link](https://git.heroku.com/your-thoughts-app.git)
- review changes since stopped working on heroku
- find last working commit, get diff with current commit
