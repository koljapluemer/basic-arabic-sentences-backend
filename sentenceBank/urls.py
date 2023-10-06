from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("words", views.words),
    path("export", views.exercises_to_json),
    path("clozes", views.cloze_to_json)
]