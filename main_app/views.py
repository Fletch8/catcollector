from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def index(request):
   return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def contact(request):
    return render(request, 'contact.html')

# Make a view function
# Make the html page
# Add the view to the urls.py inside of main_app