from django.urls import path
from . import views


urlpatterns = [
    path("", views.group, name="group"),
]
