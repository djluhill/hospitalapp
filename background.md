# Installing Dependencies
pip install -r requirements.txt

# Running the Server
python manage.py runserver
navigate to localhost:8000/static/index.html

# Notes
This project was built using Python 3. Python 2 may or may not work properly.

If you are using a Unix-type system (e.g. macOS or Ubuntu), you may need to use pip3 and python3 commands.


#  Create the project directory
mkdir tutorial
cd tutorial


#  Install Django and Django REST framework into the virtualenv
pip install django
pip install djangorestframework

#
python manage.py startproject (creates the settings.py which contains all the apps and manage.py and wsgy.py and urls.py)

- urls.py here is global
- app specific urls.py will be created manually for each app later on

                    from django.conf.urls import url, include
                    from django.contrib import admin

                    urlpatterns = [
                        url(r'^admin/', admin.site.urls),
  we only add this--->  url(r'^hospitals/', include('hospitals.urls')) 
                    ]

python manage.py startapp (creates the admin.py, apps.py, models.py, views.py)

- should receive basic outline of django files including: 
	- __init__.py - package not just a directory
	- admin.py - backend default website generated
	- apps.py - settings
	- models.py - what tables we want to store
	- tests.py - tests
	- views.py - take user request and give back something, look at a website they give you the files associated with that file, or a logout request logs you out
	- manage.py

# Select target database data 
- identify which columns are strings or integers
- identify negative values that are listed with parenthesis and convert to pure negative numbers i.e. without paranthesis
- identify which columns have null values or n/a values

# Create import columns (fields) into models.py and in parse.py and in settings.py
- properly account for each field characteristics 
- In models.py for example: facility_number = models.CharField(max_length=9, primary_key=True)
	- for all fields
- In parse.py for example: facility_number=row[0],
	- for all fields
- In settings.py make sure to select which classes you would like to target***


# Sync your database for the first time
python manage.py makemigrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

#Any subsequent changes to the database (i.e. models.py, parse.py or settings.py)
                    - 1 make changes to models.py or parse.py
                    - 2 python manage.py makemigrations
                    - 3 python manage.py migrate

#create serializers.py
- we are not doing authentication and we are not adding data through the api since its read only
- so don't have to define create or update because we just inherit the standard operations
- so this is a basic class i.e. ModelSerializer 

# add code to serializers.py *******
- create a serializer class
- what is required for read only?******
- def create
- def update

Notice how similar the API is to working with forms. The similarity should become even more apparent when we start writing views that use our serializer.***


# add code to views.py
- its already there so you dont have to create it
- so we inherit from the view sets which have built in behavior for basic CRUD operations
- in our case we are using read-only because the hospital entries are added with the parse.py script

# route to the view
- create urls.py under hospitals
- create this code for urls.py

                        from django.conf import settings
                        from django.conf.urls import url, include
                        from rest_framework import routers

                        from .views import *

                        router = routers.DefaultRouter()
                        router.register('hospitals', HospitalEntryViewSet)

                        urlpatterns = [
                            url(r'^api/', include(router.urls))
                        ]

Note everything should be wired up :
- the django models
- the RESTful API (but not connected from JQuery)
So you can now create the client-side.

#Create client-end code i.e. HTML, JS, CSS
- Create a static folder under main folder
- Create admin folder under static folder
- Create index.html
- create index.js
- Create index.css

add in settings.py near the bottom
STATIC_ROOT = './static/'  

in cmd (after you setup the static folders and doesn't need to be rerun when changing code in the static files)
python manage.py collectstatic
- so that way it knows to get the static files in each app and serve them under one directory i.e. static root, static root is specified in settings.py on STATIC_ROOT = './static/' 

- in collectstatic when it ran, it created all the default folders in static


good to go server-side

#Connect to the RESTful API from jQuery
- we used $.getJSON
- inside hospitals > static > index.js
- we update this page to reflect the data
- 3 dom interactions here
    - 1st by initially loading them
    - 2nd by filtering based on a search term
    - 3rd by sorting based on the attribute chosen by the user







