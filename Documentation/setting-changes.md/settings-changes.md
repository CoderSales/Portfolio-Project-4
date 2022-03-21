## 1.1 Search string
`Class 'Post' has no 'objects' member`
## 1.2 Result / Reference
- [Class has no objects member](https://stackoverflow.com/questions/45135263/class-has-no-objects-member)
## 1.3 Content

```
Install pylint-django using pip as follows

pip install pylint-django
```

## 1.4 Actions
### 1.4.1 Action 1
ran
`pip install pylint-django`

### relevant content 2

```
Then in Visual Studio Code goto: User Settings (Ctrl + , or File > Preferences > Settings if available ) Put in the following (please note the curly braces which are required for custom user settings in VSC):

{"python.linting.pylintArgs": [
     "--load-plugins=pylint_django"
],}
```
### 1.4.2 Action 2
Pasted the following code into settings:

```
Then in Visual Studio Code goto: User Settings (Ctrl + , or File > Preferences > Settings if available ) Put in the following (please note the curly braces which are required for custom user settings in VSC):

{"python.linting.pylintArgs": [
     "--load-plugins=pylint_django"
],}
```

### relevant content 3
```
But in newer versions of VSC you will not find the option to edit or paste that command in User Settings.

For newer versions, add the code in the following steps:

Press ctrl shift p to open the the Command Palette.
Now in Command Palette type Preferences: Configure Language Specific Settings.
Select Python.
Add these lines inside the first curly braces:
    "python.linting.pylintArgs": [
            "--load-plugins=pylint_django",
        ]
Make sure that pylint-django is also installed.
```

### action 3
- Ctrl Shift P
- Pasted in:
    - Preferences: Configure Language Specific Settings
    - Enter
- Pasted in:

```
    "python.linting.pylintArgs": [
            "--load-plugins=pylint_django",
        ]
```
## Result of last action
in terminal:
`This setting does not support per-language configuration.`

## 2.1 Search String
`This setting does not support per-language configuration.`
## 2.2 Result / Reference
- [How to change the per-language configuration of setting "editor.insertSpaces" to "auto"](https://stackoverflow.com/questions/30057721/how-to-change-the-per-language-configuration-of-setting-editor-insertspaces-to)
## 2.3 Content

```
To use perlanguage settings, you use the [language_id] in square brackets:

example:

{
  "[typescript]": {
    "editor.formatOnSave": true,
    "editor.formatOnPaste": true
  },
  "[markdown]": {
    "editor.formatOnSave": true,
    "editor.wrappingColumn": 0,
    "editor.renderWhitespace": "all",
    "editor.acceptSuggestionOnEnter": false
  }
}
Update: editor.tabSize and editor.insertSpaces are now supported in version 1.10
```

## 2.4 Action
None taken