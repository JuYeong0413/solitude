from django.urls import path
from . import views

app_name = "classes"
urlpatterns = [
    path('<int:id>/', views.main, name="main"),
]