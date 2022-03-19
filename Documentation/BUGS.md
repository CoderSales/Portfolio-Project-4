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

