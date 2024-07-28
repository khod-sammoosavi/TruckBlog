from django.shortcuts import render
from .models import Home

# Create your views here.


def home(req):
    context = {
        "home": Home.objects.all()
    }
    return render(req, "home.html", context=context)
