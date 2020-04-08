from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='reco-home'),
]
