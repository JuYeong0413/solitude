from django.urls import path
from . import views

app_name = "majors"
urlpatterns = [
    path('', views.main, name="main"),
]