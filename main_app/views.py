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
  Finch('Lolo', 'tabby', 'foul little demon', 3),
  Finch('Sachi', 'tortoise shell', 'diluted tortoise shell', 0),
  Finch('Raven', 'black tripod', '3 legged cat', 4),
  Finch('In Hat', 'Siamese', 'hairless', 4),

]
    

def finches_index(request):
    return render(request, 'finches/index.html', {'finches': finches })