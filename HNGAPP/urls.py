from django.urls import path
from .views import get_Profile

urlpatterns = [
    path("", get_Profile, name="app_url")
]