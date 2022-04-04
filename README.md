# Part 1 of 2: Non-stock README.md contents for Portfolio-Project-4

## Design Approach
Mobile first

## Documentation (Table of Contents)
In repository:
Navigate to Documentation folder.

**Main Documentation Files present:**
- BUGS.md
- CHALLENGES.md
- DEBUG.md
- DESIGN-DECISIONS.md
- LOG.md
- PLAN.md
- REFERENCES.md

### Django-Documentation (Subfolder)
- Django-References.md
- Steps-taken-in-setting-up-Django.md


## Wireframe
Overview ![Overview](assets/images/wireframe-overview.png)

Mobile First Home Page ![Mobile First Home Page](assets/images/mobile-first-home-page-compressed.png)

Desktop Home Page ![Desktop Home Page](assets/images/desktop-home-page-compressed.png)

## Elements of Website
- Django
- login


## Design Thinking and Agile Approach
(LMS Reference: Django Blog 002: Project Prerequisites)

- Content important
- Easy signup
- Easy to engage

- Problem statement:
How to develop a blog application that provides this functionality to the useer?

## Technologies used:
- [Python](https://www.python.org/)
- [Django](https://docs.djangoproject.com/en/4.0/topics/i18n/)
- [HTML5](https://en.wikipedia.org/wiki/HTML5)
- [CSS](https://en.wikipedia.org/wiki/CSS)
- [JavaScript](https://en.wikipedia.org/wiki/JavaScript)
- [GitHub](https://github.com/)
- [Gitpod](https://www.gitpod.io/)
- [Visual Studio Code](https://code.visualstudio.com/)
- [Cloudinary](https://cloudinary.com/)
- [Bootstrap](https://getbootstrap.com/docs/5.1/getting-started/contents/)
- [heroku](https://en.wikipedia.org/wiki/Heroku)
- [tiny png](https://tinypng.com/)


## Theory
### Django
django schematic ![django schematic](assets/images/basic-django-compressed.png)
[Django introduction](https://developer.mozilla.org/en-US/docs/Learn/Server-side/Django/Introduction/basic-django.png)

## Deployed site:
![responsive-design.png](assets/images/responsive-design.png)

## Main References:
## Template
- [Template](https://github.com/Code-Institute-Org/gitpod-full-template)
### LMS Tutorials:
- Hello Django
- I think therefore I blog
- Building an eCommerce platform
### Corresponding repositories:
- [Hello Django](https://github.com/Code-Institute-Solutions/Hello-Django-Django3/tree/master/08-Testing)
- [Django3blog](https://github.com/Code-Institute-Solutions/Django3blog/blob/master/12_final_deployment/)
- [eCommerce platform](https://github.com/Code-Institute-Solutions/Boutique-Ado/tree/master/05-The-Home-Page)
## Video on which post observation was made
- [Two Vortex Rings Colliding in SLOW MOTION - Smarter Every Day 195](https://youtu.be/EVbdbVhzcM4?t=381)
## Other references
- Stackoverflow

For further references, see REFERENCES.md in Documentation folder.

## Notes on deployment
For errors in the database and migrations, as a last resort:
### Completely remove Django migrations and reset database

1. Remove the all migrations files in project. Go through each of project apps' migration folders and remove everything inside, except the __init__.py file.

2. Drop the database. If using Heroku Postgres, the command for this is: 
- `heroku login -i`

- `heroku pg:reset DATABASE_URL`.

    - Locally, delete the db.sqlite3 file.
Note: only use if no other option.
3.  Run the commands python3 manage.py makemigrations and python3 manage.py migrate to remake migrations and setup the new database.

### Standard Deployment
1. Once `python3 manage.py makemigrations` and `python3 manage.py migrate` are run
`python3 manage.py createsuperuser`
2. Push to GitHub and heroku
Note: Must authorise GitHub to connect to heroku
3. Either use Automatic deployment or manual deployment
4. Click Open App

Note:
DEBUG = False

From Django Documentation(https://docs.djangoproject.com/en/4.0/howto/deployment/checklist/):
`When DEBUG = False, Django doesn’t work at all without a suitable value for ALLOWED_HOSTS.`




# Part 2 of 2: Stock Template for README.md

![CI logo](https://codeinstitute.s3.amazonaws.com/fullstack/ci_logo_small.png)

Welcome Coder731,

This is the Code Institute student template for Gitpod. We have preinstalled all of the tools you need to get started. It's perfectly ok to use this template as the basis for your project submissions.

You can safely delete this README.md file, or change it for your own project. Please do read it at least once, though! It contains some important information about Gitpod and the extensions we use. Some of this information has been updated since the video content was created. The last update to this file was: **September 1, 2021**

## Gitpod Reminders

To run a frontend (HTML, CSS, Javascript only) application in Gitpod, in the terminal, type:

`python3 -m http.server`

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

To run a backend Python file, type `python3 app.py`, if your Python file is named `app.py` of course.

A blue button should appear to click: _Make Public_,

Another blue button should appear to click: _Open Browser_.

In Gitpod you have superuser security privileges by default. Therefore you do not need to use the `sudo` (superuser do) command in the bash terminal in any of the lessons.

To log into the Heroku toolbelt CLI:

1. Log in to your Heroku account and go to *Account Settings* in the menu under your avatar.
2. Scroll down to the *API Key* and click *Reveal*
3. Copy the key
4. In Gitpod, from the terminal, run `heroku_config`
5. Paste in your API key when asked

You can now use the `heroku` CLI program - try running `heroku apps` to confirm it works. This API key is unique and private to you so do not share it. If you accidentally make it public then you can create a new one with _Regenerate API Key_.

------

## Release History

We continually tweak and adjust this template to help give you the best experience. Here is the version history:

**September 1 2021:** Remove `PGHOSTADDR` environment variable.

**July 19 2021:** Remove `font_fix` script now that the terminal font issue is fixed.

**July 2 2021:** Remove extensions that are not available in Open VSX.

**June 30 2021:** Combined the P4 and P5 templates into one file, added the uptime script. See the FAQ at the end of this file.

**June 10 2021:** Added: `font_fix` script and alias to fix the Terminal font issue

**May 10 2021:** Added `heroku_config` script to allow Heroku API key to be stored as an environment variable.

**April 7 2021:** Upgraded the template for VS Code instead of Theia.

**October 21 2020:** Versions of the HTMLHint, Prettier, Bootstrap4 CDN and Auto Close extensions updated. The Python extension needs to stay the same version for now.

**October 08 2020:** Additional large Gitpod files (`core.mongo*` and `core.python*`) are now hidden in the Explorer, and have been added to the `.gitignore` by default.

**September 22 2020:** Gitpod occasionally creates large `core.Microsoft` files. These are now hidden in the Explorer. A `.gitignore` file has been created to make sure these files will not be committed, along with other common files.

**April 16 2020:** The template now automatically installs MySQL instead of relying on the Gitpod MySQL image. The message about a Python linter not being installed has been dealt with, and the set-up files are now hidden in the Gitpod file explorer.

**April 13 2020:** Added the _Prettier_ code beautifier extension instead of the code formatter built-in to Gitpod.

**February 2020:** The initialisation files now _do not_ auto-delete. They will remain in your project. You can safely ignore them. They just make sure that your workspace is configured correctly each time you open it. It will also prevent the Gitpod configuration popup from appearing.

**December 2019:** Added Eventyret's Bootstrap 4 extension. Type `!bscdn` in a HTML file to add the Bootstrap boilerplate. Check out the <a href="https://github.com/Eventyret/vscode-bcdn" target="_blank">README.md file at the official repo</a> for more options.

------

## FAQ about the uptime script

**Why have you added this script?**

It will help us to calculate how many running workspaces there are at any one time, which greatly helps us with cost and capacity planning. It will help us decide on the future direction of our cloud-based IDE strategy.

**How will this affect me?**

For everyday usage of Gitpod, it doesn’t have any effect at all. The script only captures the following data:

- An ID that is randomly generated each time the workspace is started.
- The current date and time
- The workspace status of “started” or “running”, which is sent every 5 minutes.

It is not possible for us or anyone else to trace the random ID back to an individual, and no personal data is being captured. It will not slow down the workspace or affect your work.

**So….?**

We want to tell you this so that we are being completely transparent about the data we collect and what we do with it.

**Can I opt out?**

Yes, you can. Since no personally identifiable information is being captured, we'd appreciate it if you let the script run; however if you are unhappy with the idea, simply run the following commands from the terminal window after creating the workspace, and this will remove the uptime script:

```
pkill uptime.sh
rm .vscode/uptime.sh
```

**Anything more?**

Yes! We'd strongly encourage you to look at the source code of the `uptime.sh` file so that you know what it's doing. As future software developers, it will be great practice to see how these shell scripts work.

---

Happy coding!
