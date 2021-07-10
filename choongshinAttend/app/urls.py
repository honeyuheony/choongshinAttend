from django.contrib import admin
from django.urls import path
from .views import *
urlpatterns = [
    path('attend1/', one, name="attend1"),
    path('attend2/', two, name="attend2"),
    path('attend3/', three, name="attend3"),
    path('attend4/', four, name="attend4"),
    path('attend5/', five, name="attend5"),
    path('attend6/', six, name="attend6"),
    path('attend/', attend, name="attend"),
]
