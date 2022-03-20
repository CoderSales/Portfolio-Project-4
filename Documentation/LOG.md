## Completed Tasks

- Create Wireframe using [Google Slides](https://www.google.com/slides/about/)
- Upload Wireframe Overview

## Note

from LMS 
necessary to expose PORT 8000

### Actions
- Press Ctrl + C
    - Seems to have stopped server in terminal
- run command:
    - `python3 manage.py runserver`
        - same error no todo
            - created GitHub issue 
                per automated light bulb recommendation
                in Visual Studio Code

## Run Terminal Commands

```
python3 manage.py makemigrations --dry-run
```

```
python3 manage.py makemigrations
```

This adds the following file to migrations

```
0001_initial.py
```

## Run Terminal Commands

```
python3 manage.py showmigrations
```

```
Your_Thoughts
 [ ] 0001_initial
admin
 [X] 0001_initial
 [X] 0002_logentry_remove_auto_add
 [X] 0003_logentry_add_action_flag_choices
auth
 [X] 0001_initial
 [X] 0002_alter_permission_name_max_length
 [X] 0003_alter_user_email_max_length
 [X] 0004_alter_user_username_opts
 [X] 0005_alter_user_last_login_null
 [X] 0006_require_contenttypes_0002
 [X] 0007_alter_validators_add_error_messages
 [X] 0008_alter_user_username_max_length
 [X] 0009_alter_user_last_name_max_length
 [X] 0010_alter_group_name_max_length
 [X] 0011_update_proxy_permissions
 [X] 0012_alter_user_first_name_max_length
contenttypes
 [X] 0001_initial
 [X] 0002_remove_content_type_name
sessions
 [X] 0001_initial
```

```
python3 manage.py migrate --plan
```

### Output
Planned operations:
Your_Thoughts.0001_initial
    Create model Post

## Terminal Command

```
python3 manage.py migrate
```

### Output

```
Operations to perform:
  Apply all migrations: Your_Thoughts, admin, auth, contenttypes, sessions
Running migrations:
  Applying Your_Thoughts.0001_initial... OK
```

## Next Step

- Open admin.py

- Add these lines:

```
from .models import Post

admin.sit.register(Post)
```

### Then in terminal

Run

```
python3 manage.py runserver
```

- resolve no attribute 'sit' in admin.py Bug [Resolved]
- go to the admin panel
    - Note Posts table now shows under YOUR_THOUGHTS