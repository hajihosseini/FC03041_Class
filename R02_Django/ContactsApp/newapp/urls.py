from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path("",views.index, name="index"),
    path("delete/<int:id>",views.deleteContact),
    path("addcontact",views.addContact),
    path("sabt",views.handleContactAdd),
    path("editcontact/<int:id>",views.editContactPage),
    path("avaz/<int:id>",views.editContactForm),
]
