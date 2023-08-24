from django.urls import path
from . import views

urlpatterns = [
    path("", views.home),
    path("<slug:slug>/", views.film, name="film_detail"), 
]