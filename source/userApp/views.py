from django.shortcuts import render, redirect

from django.contrib.auth import login, authenticate, logout, update_session_auth_hash

# Decorador de autenticación para redireccionar a la página de inicio si el usuario ya ha iniciado sesión (user_passes_test es para el usuario administrador)
from django.contrib.auth.decorators import login_required, user_passes_test

from django.contrib.auth.forms import UserChangeForm
from .decorators import logged_out_required

from .forms import CustomUserCreationForm, CustomAuthenticationForm, SuperUserChangeForm
from .models import CustomUser

# Create your views here.
@logged_out_required(login_url='webApp:home')
def SignUp(request):
    if request.method == 'POST':
        form = CustomUserCreationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('userApp:signin')
    else:
        form = CustomUserCreationForm()

    context = {
        'title': 'Registrarse',
        'form': form,
    }
    return render(request, 'signup.html', context)

@logged_out_required(login_url='webApp:home')
def SignIn(request):
    if request.method == 'POST':
        form = CustomAuthenticationForm(data=request.POST)
        if form.is_valid():
            user = authenticate(request, username=form.cleaned_data['username'], password=form.cleaned_data['password'])
            if user is not None:
                login(request, user)
                return redirect('systemApp:dashboard')
    else:
        form = CustomAuthenticationForm()

    context = {
        'title': 'Iniciar sesión',
        'form': form,
    }
    return render(request, 'signin.html', context)

@login_required
def SignOut(request):
    logout(request)
    return redirect('userApp:signin')  
