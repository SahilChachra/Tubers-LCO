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
#### 1. Follow documentations
#### 2. run -> python manage.py collectstatic

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

## Create Models for Slider for the homepage
#### 1. Created Slider class with fields that are required to be stored in the database
#### 2. Register the model to Django Admin in admin page(add the code) and then run -> python manage.py makemigrations and then -> python manage.py migrate
#### 3. Note - migrations to be made for every entry to database
#### 4. Now add data from admin panel
#### 5. Show all this in the webpage

