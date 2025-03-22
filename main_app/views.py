from django.shortcuts import render
from .models import Gear

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def gear_index(request):
    gears = Gear.objects.all()
    return render(request, 'gears/index.html', {'gears': gears})