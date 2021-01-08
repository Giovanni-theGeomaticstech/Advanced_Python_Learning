from django.urls import include, path
from . import views

urlpatterns = [
    path("", views.hello, name='hello_endpoint2'),
    path("morning/", views.morning, name='morning_point'),
    path("article/<int:articleid>/<str:name>/", views.article, name='article_view'),
    path("user/<str:name>/", views.user_view, name='user_view'),
]
