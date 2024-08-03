from django.shortcuts import render
from .models import Home, Menu

# Create your views here.


def home(req):
    context = {
        "home": Home.objects.all(),
        "menus": Menu.objects.all(),
        'current_path': req.get_full_path()
    }
    return render(req, "Home/home.html", context=context)
