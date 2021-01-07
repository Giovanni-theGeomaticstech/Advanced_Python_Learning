from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.hello, name='hello_endpoint2'),
    path("morning/", views.morning, name='morning_point')
]
