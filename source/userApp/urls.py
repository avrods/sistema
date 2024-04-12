from django.urls import path

from . import views

app_name = 'userApp'

urlpatterns = [
    path('auth/signup/', views.SignUp, name='signup'),
    path('auth/signin/', views.SignIn, name='signin'),
    path('auth/logout/', views.SignOut, name='logout'),
]