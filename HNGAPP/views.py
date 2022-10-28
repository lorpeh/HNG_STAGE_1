from dataclasses import field, fields
from django.shortcuts import render
from .models import Profile
from .serializers import ProfileSerializers
from rest_framework.response import Response
from rest_framework.decorators import api_view
from rest_framework import status


slackUsername = "Lorpeh"
age = 27
bio = "Hi, My name is Tolulope.I am an upcoming backend developer and i have a great interest in developing and building APIs"


@api_view(["GET"])
def get_Profile(request):
    # Profile.objects.create(slackUsername=slackUsername, age=age, bio=bio)
    profile = Profile.objects.all().last()
    app_url = ProfileSerializers(profile)
    return Response(app_url.data, status=status.HTTP_200_OK)






# Create your views here.
