# from django.shortcuts import render
from rest_framework import viewsets

from .models import *
from .serializers import *
# Create your views here.

class HospitalEntryViewSet(viewsets.ReadOnlyModelViewSet):
    queryset = HospitalEntry.objects.all()
    serializer_class = HospitalEntrySerializer


"""Handling the request in views.py

Views are the base of the web application, receiving HTTP requests from web clients and returning HTTP responses.
In between, they marshall the other resources of the framework to access databases, render templates, etc. 

For EXAMPLE - below is a minimal view function index(), which could have been called by our URL mapper in the urls.py section. 
Like all view functions it receives an HttpRequest object as a parameter (request) and returns an HttpResponse object. 
In this case we don't do anything with the request, and our response simply returns a hard-coded string. 

"""
## filename: views.py (Django view functions)


"""  
----------------

Querying data in views.py

The Django model provides a simple query API for searching the database. 
This can match against a number of fields at a time using different criteria 
(e.g. exact, case-insensitive, greater than, etc.), and can support complex statements 
(for example, you can specify a search on U11 teams that have a team name that starts with "Fr" or ends with "al"). 

For EXAMPLE - The code snippet shows a view function (resource handler) for displaying all of our U09 teams. 

## filename: views.py

from django.shortcuts import render
from .models import Team 

def index(request):
    list_teams = Team.objects.filter(team_level__exact="U09") 
    context = {'youngest_teams': list_teams}
    return render(request, '/best/index.html', context) 

*****Note here how we can use the model query API to filter for all records 
where the team_level field has exactly the text 'U09'(note how this criteria is passed to 
the filter() function as an argument with the field name and match type separated by 
a double underscore: team_level_exact).
This function uses the render() function to create the HttpResponse that is sent back to the browser. 
  This function is a shortcut; it creates an HTML file by combining a specified HTML template 
  and some data to insert in the template (provided in the variable named "context").


"""

