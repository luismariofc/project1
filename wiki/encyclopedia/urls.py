from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),  # path(no additional argument, what shoud be viewed (file, name of the function, give a name)
    path("wiki/<str:title>", views.wiki, name="wiki"),
    path("edit_page/<str:title>", views.edit_page, name="edit_page"),
    path("random_page", views.random_page, name="random_page"),
    path("search", views.search, name="search"),
    path("add_page", views.add_page, name="add_page"),
    path("delete/<str:title>", views.delete_page, name="delete_page")
]
