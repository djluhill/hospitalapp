from django.conf import settings
from django.conf.urls import url, include
from rest_framework import routers

from .views import *

router = routers.DefaultRouter()
router.register('hospitals', HospitalEntryViewSet)

urlpatterns = [
    url(r'^api/', include(router.urls))
]
