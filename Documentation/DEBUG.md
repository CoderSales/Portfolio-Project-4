## Branch Bug [Resolved]
Accidentally opened GitPod from the User Story section of GitHub, and then committed from this repository which git classed as a side branch.
Solution:
- Merged with main
- GitHub advised that this branch can be safely deleted
- Deleted side branch to avoid confusion with main branch
- Option is present to restore side branch.

## runserver bug [Resolved]
### Solution steps
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