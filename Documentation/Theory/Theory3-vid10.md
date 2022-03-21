## Reference
LMS Video 10 (Django)

## Difference between GET and POST requests
- Simple
    - GET requests get information from the server
    - POST requests send or post information to the server

## Application
- Sending the data for a new comment
to the 
/add url
so using POST

- need to add special template flag to the
form as a security measure

- just inside the opening form tag
whenever we are posting information in Django
    - need to add the CSRF_token
        - Cross Site Request Forgery token
        - this token is a randomly generated 
            unique value 
            added to the form as a hidden input field
            when the form is submitted
            - and works to guarantee that the data we are posting is 
            actually coming from our Your_Thoughts App
            and not from another website

if we were to skip adding this token, 
Django would throw an error when we 
submitted the form because it wouldn't
be able to guarantee that the post data wasn't coming from
another site.

With all that done, the final piece of the puzzle here is how to handle
what happens when a user clicks submit on the form.