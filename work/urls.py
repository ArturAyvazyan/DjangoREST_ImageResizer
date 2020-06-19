from django.contrib import admin
from django.urls import path, include 
from work.views import *

urlpatterns = [
    path('1', CarCreateView.as_view())
]
