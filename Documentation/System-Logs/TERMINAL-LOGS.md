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