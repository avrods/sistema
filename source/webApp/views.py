from django.shortcuts import render

# Create your views here.
def Home(request):
    context = {
        'title': 'Sistema Administración',
    }
    return render(request, 'home.html', context)

def Modules(request):
    context = {
        'title': 'Modulos',
    }
    return render(request, 'modules.html', context)

def Price(request):
    context = {
        'title': 'Precios',
    }
    return render(request, 'price.html', context)

def Help(request):
    context = {
        'title': 'Ayuda',
    }
    return render(request, 'help.html', context)