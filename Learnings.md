# Learnings

* views should always return a `HttpResponse` or some Django object like `render`. Returning for example a string object would give an error saying: `'str' object has no attribute 'get'`. Django has built-in functions to secure the responses, which comes in when we use `HttpResponse`. 
* we can either read in files from `.html` or put the whole html as a string object. BUT as a professional use django template engine which is better option.  
* to load in templates from custom directory, need to add the path in `settings.py`. In `TEMPLATES=` (list of dict), add the new directory path as an element in the array obj called `DIRS` (key). 
```
my_title = "My Page"
my_context = {"page_title": my_title}
html_template = "home.html"     #   file moved to templates
return render(request, html_template, my_context)
```  
To read in the `my_context` in html file, we use `{{}}` method. Just put the name of the key we want to use.  
  
* Some basic attributes of `request` that is being passed:  
  * `request.user`
  * `request.user.is_authenticated`
  * `request.method`
* To inherit from `base.html`, as in use it as a scaffold, other html files can extend it by putting `{% extends 'base.html' %}` at the top.
* In order to view some data from child html, use:
```
{% block var_name %}
some data
{% endblock var_name %}
```
should be on both the files. Make sure to match the variable name. Its basically content substitution.
* `{{ block.super }}` -> to use from parent html file
* to use other template, say in subdir named `snippets` -> `{% include 'snippets/welcome-user-msg.html' %}`
* Created `visits` folder, by running command `python manage.py startapp visits`. In here we can create our models.
* After making changes to model, run `python manage.py makemigrations`. It tells django to GET READY to make changes to the database.
* Then run `python manage.py migrate`.