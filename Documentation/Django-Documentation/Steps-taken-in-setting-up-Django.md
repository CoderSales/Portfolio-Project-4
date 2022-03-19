## Documentation Used:
- [Hello Django: Part 1: Creating the Say Hello App](https://docs.google.com/document/d/113P2BPOkrG6rMxsrm8GCbO6CVG2b1R9htD4tRdkSltQ/edit)

### Steps taken
#### Step 1: Create Project and App
##### #1 Install Django

```
pip3 install django==3.2

```

#### #2: Create Project

```
django-admin startproject Profile_Project_4 .
```

##### Note on Filename
Profile-Project-4
is name of Project on GitHub Repository.
However, dash "-" is not a valid character
for last command, so underscore substituted for dash 
in assigning project name for Django using django-admin command.
See last command above.

Original command format from documentation:

```
django-admin startproject PROJ_NAME .
(Don’t forget the ‘.‘)
```



#### #3: Create a new App

```
python3 manage.py startapp Your_Thoughts
```

##### Note on App Name
Per above.
Your Thoughts
will be the name of the App on the website.
However, neither dash "-", nor space " " are valid characters
for last command, so underscore substituted for space 
in assigning App_Name for Django using django-admin command.
See last command above.

Original command format from documentation:

```
python3 manage.py startapp APP_NAME

```

At this point it seems that this is a python3 command,
whereas the previous was a Django command,
so possibly the same restrictions do not apply,
however, for simplicity, speed, and progress to be made,
the naming convention will be maintained.

##### * To run the server 
(Step after 3 in Hello Django Documentation)

```
python3 manage.py runserver
```

## In django_todo / settings.py:

### #4 Add your app to INSTALLED APPS

INSTALLED_APPS = [
    ...
    'django.contrib.staticfiles',
    'todo', <-- new code added -->
]

## Ran migration code per terminal message

```
python manage.py migrate
```
