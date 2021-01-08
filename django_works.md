# This File will focus on the Multiple Apps developed with Django
- The `Learn Django App` in Google Play Store

## Django - Design Philosophies
- `Loosely Coupled` -> Makes each element of its stack development of the others
- `Less Coding` -> Less code so in turn a quick development
- `Don't Repeat Yourself (DRY)` -> Everything should be developed only in exactly one place instead of repeating it again
- `Fast Development` -> Facilitate hyper-fast development
- `Clean Design` -> Django maintains a clean design throughtout its own code and makes it easy to follow best web-dev practices

## Advantages of Django
- `Object-Relational Mapping (ORM) Support` : Django provides a bridge between the data model and database engine
    - supports a large set of `database systems`
    - It also supports `NoSQL` : `MongoDB` and google app engine through `Django-nonrel` fork
    
- `Multilingual Support`: Support multiple languages
- `Framework Support`: Has built in support for `Ajax, RSS, Caching` various other frameworks
- `Administration GUI`: Django provides a nice ready to use user interface for administrative activities
- `Development Environment`: Also comes with a lightweight webserver to facilitate end-to-end app development and testing

## MVC Pattern
- Django supports the MVC (Model-View-Controller) pattern, and then MVT (Model-View-Template)
- An app that provides UI (web or desktop) we talk about `Model View Controller` architecture
- Based on three components `Model, View, Controller`

### Django MVC - MVT Pattern
- `Model-View-Template` is slightly different from MVC
- The main difference is that Django takes care of `Controller part`
    - Software Code that controls the interactions between the `Model and View`
    - Leaving us with the `Template` -> the `HTML file` mixed with Django Template Language(DTL)
    - image for the MVT pattern interactions with each other to serve a user request
    -                                                Model  
    -                                               //
    - `user` -> <- `django` -> <- `url` -> <- `View`   
    -                                               \
    -                                                Template
    - The developer provides the Model, the view and the template then just maps it to a URL (endpoint) and Django does the magic to serve it to user

## The Environment
- Django is written in 100% pure python code 
- `django-admin.py --version` or `django-admin --version` 
- `Step 3 - Database Setup`
- `Step4 - Web Server` Lightweight webserver for developing and testing applications
    - It restarts whenever you modify the code
    - Django does support `Apache` and other popular web servers such as `Lighttpd`

## Create a Project
- Every web app we want to create is called a project
- A project is a `sum of applications`
- An application is a `set of code files` relying on the `MVT`pattern
- Lets say we want to build a website, the `website is our project`
- `Forum, news, contact engine are applications`
- This structure makes it easier to move an application between projects since every application is independent
### Start Your Project
- `django-admin startproject myproject_name`
- Creates a folder with `myproject_name`
  - It has a `manage.py`: This file is kind of your prject local django-admin for interacting with your project via cmd
  - `python manage.py help` shows you the full list of commands
  - `myproject_name` sub-folder is the actual python package of your project
  - It contains four files `__init__.py, settings.py, urls.py and wsgi.py`
    - `__init__.py`: Just for python, treat this folder as a package
    - `settings.py`: As the name indicates, your project settings
    - `urls.py`: All links of your project and the function to call. A kind of ToC (Table of Contents) of your project
    - `wsgi.py`: If you need to deploy your project over WSGI
      * WSGI - The Web Server Gateway Interface. It is a specification that describes how a `web server communicates` with `web applications` and how web applications can be chained together to process one request. 
        WSGI is a Python standard described in detail in PEP 3333.
        
### Setting Up Your Project
- Set `DEBUG = True` lets you get more information about your project's error
- Never set it to `True` in `production or live project`
- However this has to be set to `True` if you want the Django light server to serve static files do it only in dev mode
- Database components: `DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
        'HOST': '',
        'PORT': '',
    }
}`
  
- Database is set in the `Database` dictionary 
- Make sure you have the correct db engine installed
- You can also play around with other [settings](https://docs.djangoproject.com/en/3.1/ref/settings)
- When done try it out by doing `python manage.py runserver` or ./manage.py runserver

### Creating an Application
- A project is a sum of many applications
- Every application has an objective and can be reused into another project
- Like a contact form on a website can be an application and can be reused for others.
- See it as a module of your project
#### Steps for creating an Application
- `python manage.py startapp myapp1` or `./manage.py startapp myapp1`
- Files within this `myapp1` folder `__init__.py, admin.py, models.py, tests.py, views.py`
    - `__init__.py`: Just to make sure python handles this folder as a package
    - `admin.py`: This file helps you make the app modifiable in the `admin interface`
    - `models.py`: This is where all the application models are stored
    - `tests.py`: This where unit tests are
    - `views.py`: This is where your application views are.
    
#### Get The Project to know about your Application
- Now we have our `myapp1` but it is not registered within our Django project `trial_project1`
- To register our app we will go to `INSTALLED_APPS = () + myapp1`

### Admin Interface
- Django provides a ready to use user interface for administrative activities
- It automatically generates admin UI based on your project models
- The admin interface depends on the `django.contrib` module
- To have it working I have to make sure some modules are imported in the `Installed_Apps` and `Middleware_Classes`
- of the `trial_project1/settings.py`
- Before Launching server, to access the Admin Interface, the database needs to be initiated
- `python manage.py migrate` this will sync necessary tables
- `./manage.py createsuperuser` to create a superuser
- The admin interface gives you the ability to do the `CRUD`
- `Create, Read, Update, Delete` operations on models

### Creating Views
- A `view function` or `view for short is simply a Python function that takes
- `web request` and returns `web response` 
- This response can be: `Html contents of a web page, or a redirect, or a 404 error, or an XML, or an image or etc.`
- Note we use views to `create web pages`, `note that you need to associate a view to a URL to see it as a web page`
- in Django `views` are created in for an app `views.py`
#### Simple View
- `from django.http import HttpResponse`
- In a function we return `HttpResponse(#some info)`
- To see this as a page we have to map the endpoint
- Using `HttpResponse` to render the HTML is not the best way to render pages
- Django supports the MVT pattern so to make the precedent (earlier) action we will need a template
- A template
- `myapp1/templates/hello.html` and in the view 
- `from django.shortcuts import render 
  def hello(request):
  return render(request, "myapp1/templates/hello.html, {}")`
    
- views can also accept parameters

### URL Mapping
- Django has its own way for url mapping and its done by editing your project url.py (trial_project1/url.py)
- When a user makes a requests for a page on your web app, Django controller takes over
- to look for the corresponding view via the `url.py` file
- It then returns a `HttpResponse ot 404 not found error`
- In url.py thr most important thing is the `"urlpatterns"` tuple
- It is where the endpoints are defined.
- In path you have:
    - `The pattern` A regexp matching URL you want to be resolved and mapped
    - useful for passing parameters 
    - `The python path`: Same as when importing module
    - `The name`: Needed inorder for performing url reverse
    
#### Organizing Your URLs
- We want to be able to reuse applications
- How we have it now is that we are directly mapping from views in the `myapp1`
- The best practice is to create `url.py` per an application
- The include this url mapping into our project `urls.py`
- steps in the `myapp1` create a `url.py` file
- Then `from django.urls import include, path`
  
#### Passing Parameters to Views
- Sending Parameters to Views is done by capturing them with the `regexp` in `url pattern`
- [urls](https://docs.djangoproject.com/en/3.1/topics/http/urls/#passing-extra-options-to-view-functions)
- `path('name/<type(variable_name):variable_name>')`
- Note `HttpResponse(string)` or `render(file.html)`

### Template System
- [Templates documentation](https://docs.djangoproject.com/en/3.1/topics/templates/)
- Django makes it possible to separate `Python` and `HTML`
- The Python goes in `views` and `HTML` goes in templates
- Linking the two Django relies on the `render function` and the `Django Template Language`

#### The Render Function
- Takes three parameters `request`, `the path to the template`, `dictionary of parameters`
- `Request`: The initial request.
- `The path to the template`: This is the path relative to the `Template_DIRS` option in project `settings.py` variable
- `Dictionary of parameters`: A dictionary that contains all variables needed in the template.
- This variable can be created or you can use `locals()` `to pass all local variables declared in the view`

#### Django Template Language(DTL)
- Django's template engine offers a mini-language to define the user-facing layer of the application
- DISPLAYING VARIABLES
- A variable looks like this: `{{variable}}`
- The `template replaces the variable with the one sent by the view in the third parameter`
- By default Django looks in each `Installed_Apps` subdirectories for templates
- `APP_DIRS=True` allow this behaviour
- [Removing Hardcoded urls in Templates](https://docs.djangoproject.com/en/3.1/intro/tutorial03/#removing-hardcoded-urls-in-templates)

#### Filters
- These helps to modify variables at display time
- The structure of filters follow this format `{{var|filters}}`
- For eg: `{{string|truncatewords:80}}` will truncate the string so you only see the first 80 words
- `{{string:lower}}` - Converts the string to lowercase
- `{{}string|escape|linebreaks}` First escapes string contents and then converts line breaks to tags
- You can also set default for a variable

#### Tags
- These let you perform operations: if conditions, for loops, template inheritance and more
- Just like Python you can use `if, else and elif` in your template
- Tags are called via `{% tag body %}`
##### Tags if 
- `{% if today.day == 1 %} The first day of the month.
{% elif today == 30 %} the last day of the month. {% else %} I don't know.
  {% endif %}`.
  
##### Tags for
- `{% for day in days_of_week %}`

##### Block and Extend Tags
- A template system cannot be complete without `template inheritance`
- Meaning when designing templates we should have a `main template` which holds child's template
- will fill according to his own need.
- Like a page need a special css for the selected tab
- In `main_template.html we add` :
- `<title>{% block title%}Page Title{% endblock%}</title>` For the title
- `{% block content %} Body content {% endblock %}` FOr the body
- Now in the template file `index.template`
- `{% extends "main_template.html" %}` `{% block title %}` `My User Page` `{% endblock %}`
- Then put the body within `{% block content %} Content {% endblock %}`
- In `main_template.html` we define blocks using the tag block
- The title block will have the title and the content block will have the main content
- now in `index.html` we use extends to inherit from the `main_template.html` then we fill the
- `blocj define (content and title)`
- To define a tag block we do `{% block name_block%} Anything here {% endblock %}`


  