from django.urls import path
from . import views

urlpatterns = [
    path('demo', views.index, name='demo'),
    path('new_interaction', views.new_interaction, name='new_interaction'),
    path('home', views.home, name='home'),
    path('drawing', views.drawing, name='drawing'),
    path('home-dark', views.home_dark, name='home-dark')
]
