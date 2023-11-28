from django.shortcuts import render
from django.http import HttpResponse
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
    return render(request, 'listings/hello.html',{'bands': bands})


def listing(request):
    news = New.objects.all()
    return render(request, 'listings/news.html',{'news': news})
