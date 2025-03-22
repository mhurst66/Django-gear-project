from django.shortcuts import render
from .models import Gear

def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def gear_index(request):
    gears = Gear.objects.all()
    return render(request, 'gears/index.html', {'gears': gears})

def gear_detail(request, gear_id):
    gear = Gear.objects.get(id=gear_id)
    return render(request, 'gears/detail.html', {'gear': gear})