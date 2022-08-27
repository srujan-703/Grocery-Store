from django.urls import path
from django.views.generic.base import View
from .views import Cream

urlpatterns = [
    path('cream', Cream.as_view(), name="cream")
]
