from django.contrib import admin
from django.urls import path
from DjangoValidAPP import views

urlpatterns = [
    path('register/',views.index),
    path('sign/',views.sign)
]
