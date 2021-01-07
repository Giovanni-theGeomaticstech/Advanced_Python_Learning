from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.

def hello(request):
    number = 7
    text = f"<h1>Welcome to my app. My number is {number} !</h1>"
    return HttpResponse(text) # Use Http response to render as an html

def morning(request):
    name = "Gio"
    text = f"<h1>Good Morning {name} !</h1>"
    return HttpResponse(text) # Use Http response to render as an html
