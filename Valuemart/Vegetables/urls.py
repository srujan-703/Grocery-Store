from django.urls import path
from django.views.generic.base import View
from .views import Vegetables

urlpatterns = [
    path('vegetables',Vegetables.as_view(), name="vegetables")
]
