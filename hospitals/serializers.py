from rest_framework import serializers

from .models import *

class HospitalEntrySerializer(serializers.ModelSerializer):
    class Meta:
        model = HospitalEntry
        fields = "__all__"

#we are not doing authentication and we are not adding data through the api since its read only
# Examples Provided on django-rest framework.org
# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ('url', 'username', 'email', 'groups')


# class GroupSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = Group
#         fields = ('url', 'name')