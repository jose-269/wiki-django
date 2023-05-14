from django.urls import path
from . import views

app_name = "wiki"

urlpatterns = [
    path("", views.index, name="index"),
    path("wiki/<str:title>", views.entry, name="title"),
    path("search/", views.search, name="search"),
    path("new/", views.newEntry, name="new"),
    path("edit/<str:title>", views.editEntry, name="edit"),
    path("random", views.randomEntry, name="random"),
]