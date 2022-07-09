from unicodedata import name
from django.shortcuts import render


# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

class Finch:  
  def __init__(self, name, breed, description, age):
    self.name = name
    self.breed = breed
    self.description = description
    self.age = age

finches = [
  Finch('Tweety', 'Wren', 'yellow', 60),
  Finch('Sachi', 'BlackBird', 'blue', 0),
  Finch('Raven', 'Robin', 'green', 4),
  Finch('In Hat', 'Magpie', 'red', 4),
]
    

def finches_index(request):
    return render(request, 'finches/index.html', {'finches': finches })