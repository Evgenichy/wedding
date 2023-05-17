from django.urls import path
from .import views

urlpatterns = [
    path('', views.vote, name='index'),
    path('success', views.success, name='success')
    ]
