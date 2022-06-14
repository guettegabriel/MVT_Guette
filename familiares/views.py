from django.shortcuts import render
from django.template import loader
from familiares.models import familiar

# Create your views here.

def familiares(request):
    familia = familiar.objects.all()
    
    return render (request, "index.html", {'familias':familia})