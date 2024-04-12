from django.urls import path

from . import views

app_name = 'webApp'

urlpatterns = [
    path('', views.Home, name='home'),
    path('modules/', views.Modules, name='modules'),
    path('price/', views.Price, name='price'),
    path('help/', views.Help, name='help'),
]