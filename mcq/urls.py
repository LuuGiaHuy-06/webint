from . import views
from django.urls import path 

urlpatterns = [
    path("", views.mcq_fast, name="index"),
]