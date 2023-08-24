from django.shortcuts import render
from django.http.response import HttpResponse
from .models import Film
from django.shortcuts import render, get_object_or_404
# Create your views here.

def home(req):
    films = Film.objects.all()
    return render(req,"app/app.html",{"films": films})


def films(reg):
    pass

def film(request, slug):
    film = get_object_or_404(Film, slug=slug)
    return render(request, "app/film_detail.html", {"film": film})
    

   

