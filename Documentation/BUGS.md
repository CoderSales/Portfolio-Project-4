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

## file name not using snake case Bug
- file auto-generated using makemigrations command
begins with a digit

- in Problems in Console
    Message:

    ```
    Module name "0001_initial" doesn't conform to snake_case naming style
    ```

### Search string

```
Module name "0001_initial" doesn't conform to snake_case naming style
```

### Results
- [Errors on names of migrations #167](https://github.com/PyCQA/pylint-django/issues/167)

### Content

```
it's pylint.exe evap.

this isn't invoking pylint-django. If this is your command line then pylint is working as expected b/c you are not enabling the pylint-django plugin.
```

### Attempt to resolve Bug
try "enabling the pylint-django plugin"
by searching for

`file name not using snake case Bug`

in Extensions on left side bar in Visual Studio Code 

#### Found
Django

#### Action
Install

#### Further Actions
Extension: Django
Default page advises adding the following
code to settings:

```
"files.associations": {
    "**/*.html": "html",
    "**/templates/**/*.html": "django-html",
    "**/templates/**/*": "django-txt",
    "**/requirements{/**,*}.{txt,in}": "pip-requirements"
},
```

##### Action
Open Command Palette using `Ctrl + Shift + P` or cog wheel in bottom left of Visual Studio Code in GitPod

Type

`Preferences: Open Settings (JSON)`

into Command Palette search bar

Add code to bottom inside last curly bracket `}`


    Code added:

```
      - ,
      - line break
```


```
"files.associations": {
    "**/*.html": "html",
    "**/templates/**/*.html": "django-html",
    "**/templates/**/*": "django-txt",
    "**/requirements{/**,*}.{txt,in}": "pip-requirements"
},
```
#### Recommendation
Extension: Django
also states:

```
Emmet enthusiasts should have this to their configuration as well:
```

```
"emmet.includeLanguages": {"django-html": "html"},
```
#### Action
Open Command Palette using `Ctrl + Shift + P` or cog wheel in bottom left of Visual Studio Code in GitPod

Type

`Preferences: Open Settings (JSON)`

into Command Palette search bar

Add code to bottom inside last curly bracket `}`


    Code added:

```
      - ,
      - line break
```


```
"emmet.includeLanguages": {"django-html": "html"},
```

### Unresolved
Bug still persists

# New Bug
in models.py 
str (for string)
has a Problem in console
that it does not return
a string

## Status
Although unresolved,
when server view of admin page
in Browser is refreshed
Posts now display 
names of Users instead of generic values as before,
as required.

## Not Deploying to heroku Bug

### Possible causes

- DEBUG variable
- DISABLE_COLLECTSTATIC config var
- Migration files
- Location of STATIC folder
- Path to STATIC folder