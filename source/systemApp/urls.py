from django.urls import path

from . import views

app_name = 'systemApp'

urlpatterns = [
    path('admin/', views.myAdmin, name='admin'),
    path('admin/edit/', views.edit_superuser, name='edit_superuser'),
    path('dashboard/', views.Dashboard, name='dashboard'),
]