from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required, user_passes_test

from source.userApp.decorators import logged_out_required
from source.userApp.forms import CustomUserCreationForm, CustomAuthenticationForm, SuperUserChangeForm
from source.userApp.models import CustomUser


# Create your views here.
@login_required
def Dashboard(request):
    context = {
        'title': 'Panel de Administración',
    }
    return render(request, 'dashboard.html', context)

def is_superuser(user):
    return user.is_superuser

@login_required
@user_passes_test(lambda u: u.is_superuser)
def myAdmin(request):
    users = CustomUser.objects.all()
    context = {
        'title': 'Administración',
        'users': users
    }
    return render(request, 'admin.html', context)

@login_required
@user_passes_test(lambda u: u.is_superuser)
def edit_superuser(request):
    if request.method == 'POST':
        form = SuperUserChangeForm(request.POST, instance=request.user)
        if form.is_valid():
            user = form.save(commit=False)
            password = form.cleaned_data['password']
            if password:
                user.set_password(password)
            user.save()
            update_session_auth_hash(request, user)
            return redirect('systemApp:dashboard')
    else:
        form = SuperUserChangeForm(instance=request.user)

    context = {
        'title': 'Editar SuperUsuario',
        'form': form
    }
    return render(request, 'user-edit.html', context)  