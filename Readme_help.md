## Initial Setup
#### 1. The project's frontend was designed using AdobeXD (Figma can also be used)
#### 2. Developer can use Template depending on the usecase
#### 3. After making the design, flowchart can be made using - coggle.it

## Links used
#### 1. Postgresql(this link has PGadmin4 also) -> https://www.postgresql.org/download/windows/
#### 2. Refer Django documentation -> https://docs.djangoproject.com/en/3.1/
#### 3. Better documentation -> https://djangopackages.org
#### 4. Admin panel theme -> https://github.com/django-cms/djangocms-admin-style

## Environment Settings
#### 1. Installed pipenv (allows to create a virtual environment and also saves a file with all configureations)
#### 2. To activate the envirnoment -> use >pipenv shell ( this will either create a new environemnt or run the old one)

## Django commands
#### 1. To create Django project ->  django-admin startproject project-name
#### 2. To run Django server (cd to the project folder) -> python manage.py runserver

## Fix migration errors
#### 1. Make some files and fix it ->  python manage.py makemigrations
#### 2. After all the migrations files have been done -> python manage.py migrate
#### 3. Then run the server again -> python manage.py runserver

## Create user for Admin panel in Django
#### 1. to create admin user -> python manage.py createsuperuser
#### 2. Then run the server and add localhostIP/admin/ -> enter id password entered during creation process
#### 3. Add a theme for panel -> pipenv install djangocms-admin-style
#### 4. Add in setting.py TEMPLATES -> 'DIRS': ['templates'] and create a templates folder
#### 5. After following the guide in github repo - run migration command

## Add static files
#### 1. Add JS, CSS & images in tubers/tubers/static/
#### 2. Follow documentations
#### 3. run -> python manage.py collectstatic

## Start App
#### 1. Create app -> python manage.py startapp appName
#### 2. create urls.py file
#### 3. In settings.py -> add all the app names you added in INSTALLED_APPS , here -> 'webpages.apps.WebpagesConfig'

## Setup URLS
#### 1. Add the new path in urls.py in tubers + add static configuration
#### 2. Go to webappName/urls.py and then add path 
#### 3. In views.py add method which will be called for each request

## Preparation for templates
#### 1. Add folder in tubers/templates/webpages
#### 2. Create base.html file in tubers/templates
#### 3. Create all the webpages required for the project and update return statement in tibers/webpage/views.py
#### 4. Add template files in static (js, css)
#### 5. collect static by running command
#### 6. Add template code and fix sources of local css, js and images
#### 7. Refactor code
#### 8. include - {% load static %} if we are loading anything from static from a page

## Setting up Slider for the homepage
#### 1. Created Slider class with fields that are required to be stored in the database in models.py
#### 2. Register the model to Django Admin in admin page(add the code - admin.site.register(class_name)) and then run -> python manage.py makemigrations and then -> python manage.py migrate
#### 3. Note - migrations to be made for every entry to database(every change to database schema)
#### 4. Now add data from admin panel
#### 5. Show all this in the webpage
#### 6. Add code to views and pass data for specific page
#### 7. Edited Home.html and added dynamic code.

## Adding more things to Admin Panel
#### Link - https://docs.djangoproject.com/en/3.1/ref/contrib/admin/#inlinemodeladmin-objects
#### 1. in admin.py create a class and pass admin.ModelAdmin
#### 2. Parameters used are being overriden by us by passing a new values
#### 3. list_display - can be overridden
#### 4. To make selected field as clickable use list_display_link
#### 5. To enable search, search_field = ('parameter',)
#### 6. to add filter -> list_field = ('para',)
We can defines many functions to change the view of the data in admin panel. Follow = https://docs.djangoproject.com/en/3.1/ref/contrib/admin/#inlinemodeladmin-objects and search for "Elements of list_display can also be properties".

## Show Teams dynamically
#### 1. Go to views.py and add teams in data
#### 2. Update frontend - home.html page to display data from database

## Youtuber app - Creating the app + Restricting choice of the user
#### 1. Create app -> python manage.py startapp youtubers
#### 2. Update settings.py - INSTALLED_APPS
#### 3. Go to urls.py in tubers and add the youtube url
#### 4. Create urls.py in youtubers app
#### 5. Add routes in new urls.py
#### 6. Now define methods in views.py
#### 7. Create model in models.py
#### 8. Register the model admin.py in youtubers app
#### 9. Perform migration
#### 10. Restrict user choice in Models - in models.py
#### 11. Create choices and pass it as parameter
#### 12. We now change textfield in admin panel - install django-ckeditor and mention in installed apps(follow : https://github.com/django-ckeditor/django-ckeditor)
#### 13. Import ckeditor add RichTextField as field
#### 14. Make migrations
#### 15. Edit admin panel view for Youtubers app

## Transfer data from Youtube app to Webpages app
#### 1. Go to Webpgaes/views and import the app
#### 2. Mention the data required from the Model
#### 3. Update frontend - home.html

## Fixing Navbar
#### 1. Use -> {% url 'home' %} where home comes from url mentioned in urls.py of webpages app

## Connect Tubers in navbar to page
#### 1. Created new folder named youtubers in templates
#### 2. Added new html file (paste the code there of the page)
#### 3. Go to views.py in youtubers and in youtubers(), fetch the data and pass it with the template
#### 4. When we pass url in template(like in href) the code is {% url 'name_of_function_in_views.py' %}

## For setting up Search(general) in home.html
#### 1. Create new html page in youtubers/search.html and add the data
#### 2. In views.py, add the search function
#### 3. Created a query to get the data
#### 4. POST request requires CSRF token (for GET request its not required)
#### 5. Edit form tag - put method='get/post and action='url_of_page' attributes
#### 6. Give name to input same as that used in views.py (eg : keyword in seach() and keyword in input tag in search page)

## For filtered search
#### 1. In function search write relevant quiers and pass it on data
#### 2. Write relevant if statements for query
#### 3. In the search.html, mention method and action in form tag
#### 4. Replace all hard coded values with dynamic value
#### 5. Use for loops to display options

##  Creating Accounts
#### 1. Create new app -> python manage.py startapp accounts
#### 2. Register the app by mentioning the name of app in Settings.py
#### Go to app.py of Accounts and copy class name. Go to main app's(tubers) settings.py and mention it in INSTALLED_APPS
#### Syntax is -> app_name.apps.classNameCopiedFromApp.py
#### 3. Now update main app's (tubers) urls.py and metion path
#### 4. Create urls.py in accounts
#### 5. Now mention all the urls required for the app
#### views.logout is inbuilt in Django. It's keyword. avoid using it
#### 6. Now go to views.py and add functions for each url defined in accounts/urls.py
#### 7. Configure Templates - in views.py return render(request, 'path/template_name.html')
#### 8. Add new folder in templates - accounts. 
#### 9. Now add extends base, block content and HTML code to login.html
#### 10. Load static in template and correct the urls mentioned in template as {% static './path' %}
#### 11. Now configure rest of the pages like above (from step 9)

## Configure Buttons - Login and Signup and logout
#### 1. Go to templates/includes/navbar and add relevant url to buttons
#### 2. Go to accounts/views import logout from auth and in logout_user function call logout(request)

## Configure Register page
#### 1. In register.html, add method and action to the form 
#### 2. Add { csrf_token } -> this way django verifies it's post method only
#### 3. Add name to inputs in form
#### 4. Now in accounts/views.py fetch the data(in register()) from the form only if method==POST
#### 5. User -> predefined model for user in Django
#### 6. Perform checks of password and other fields (whatever required)
#### 7. Password entered will be auto-encrypted