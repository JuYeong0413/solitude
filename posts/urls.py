from django.urls import path
from . import views

app_name = "posts"
urlpatterns = [
    path('new/', views.new, name="new"),
    path('create/', views.create, name="create"),
    path('edit/<int:id>/', views.edit, name="edit"),
    path('update/<int:id>/', views.update, name="update"),
    path('delete/<int:id>/', views.delete, name="delete"),
    path('create_comment/<int:id>/', views.create_comment, name="create_comment"),
    path('delete_comment/<int:id>/', views.delete_comment, name="delete_comment"),
    path('like_toggle/<int:id>/', views.like_toggle, name="like_toggle"),
    path('show/', views.show, name="show"),
    path('search/', views.search, name="search"),
]