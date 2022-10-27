from importlib.metadata import MetadataPathFinder
from .models import Profile
from rest_framework import serializers


class ProfileSerializers(serializers.ModelSerializer):
    class Meta:
     model = Profile
     exclude =["id"]