from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("words", views.words),
    path("exercises", views.exercises),
]