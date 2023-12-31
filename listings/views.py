from django.http import HttpResponse
from django.shortcuts import render
from django.db import models
from listings.models import Band
from listings.models import New


def hello(request):
    bands = Band.objects.all()
    return HttpResponse(f"""
        <h1>Hello Django !</h1>
        <p>Mes groupes préférés sont :<p>
        """)


def about(request):
    return HttpResponse('<h1>À propos</h1> <p>Nous adorons merch !</p>')


def contact(request):
    bands = Band.objects.all()
    return render(request, 'listings/listings.html', {'bands': bands})


def listing(request):
    bands = Band.objects.all()
    return render(request, 'listings/listings.html', {'bands': bands})


def home(request):
    logo = models.ImageField(name='Logo.jpeg')
    news = New.objects.all()
    return render(request, 'listings/home.html', {'logo': logo, 'news': news})
