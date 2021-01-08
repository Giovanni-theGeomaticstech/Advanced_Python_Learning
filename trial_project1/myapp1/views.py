from django.shortcuts import render
from django.http import HttpResponse
from datetime import datetime
# Create your views here.

def hello(request):
    number = 7
    text = f"<h1>Welcome to my app. My number is {number} !</h1>"
    return HttpResponse(text) # Use Http response to render as an html

def morning(request):
    name = "Gio"
    text = f"<h1>Good Morning {name} !</h1>"
    return HttpResponse(text) # Use Http response to render as an html

def article(request, articleid, name):
    text = f"<h1>The User: {name} has article id of {articleid} !</h1>"
    return HttpResponse(text)

def user_view(request, name):
    days_of_week = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturaday", "Sunday"]
    return render(request, 'Base/index.html', dict(today=datetime.now(), user_name=name, days_of_week=days_of_week))



