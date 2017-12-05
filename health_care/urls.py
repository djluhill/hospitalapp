"""health_care URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url, include
from django.contrib import admin

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^hospitals/', include('hospitals.urls'))
]

"""
    url(r'^hospitals/', include('hospitals.urls'))
    - this tells django to direct all request which begin with hospitals/ to urls for the hospitals app
    - in the url it would say http://localhost:8000/hospitals/api
"""


"""
the urlpatterns object is a list of url() functions. In Python, lists are defined using square brackets. 
for example: [item1, item2, item3]. 

urlpatterns = [
    url(r'^$', views.index),
    url(r'^([0-9]+)/$', views.best),
]

The odd-looking syntax for the pattern is known as a regular expression. We'll talk about these in a later article!
The second argument to url() is another function that will be called when the pattern is matched. 
The notation views.index indicates that the function is called index() and can be found in a module called views 
(i.e. inside a file named views.py).


"""