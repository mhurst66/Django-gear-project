from django.shortcuts import render

class Gear:
    def __init__(self, name, breed, description, age):
        self.name = name
        self.breed = breed
        self.description = description
        self.age = age

# Create a list of Cat instances
gears = [
    Gear('Lolo', 'tabby', 'Kinda rude.', 3),
    Gear('Sachi', 'tortoiseshell', 'Looks like a turtle.', 0),
    Gear('Fancy', 'bombay', 'Happy fluff ball.', 4),
    Gear('Bonk', 'selkirk rex', 'Meows loudly.', 6)
]


def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def gear_index(request):
    return render(request, 'gears/index.html', {'gears': gears})