from django.urls import path
from django.views.generic.base import View
from .views import Juices

urlpatterns = [
    path('juices', Juices.as_view(), name="juices")
]
