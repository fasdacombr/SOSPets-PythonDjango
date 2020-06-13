from django.shortcuts import render, redirect
from django.views.decorators.csrf import csrf_protect
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .models import Pet

# Create your views here.

@login_required(login_url='/login/')
def list_all_pets(request):
    pet = Pet.objects.filter(ativo=True)
    return render(request, 'list.html', {'pet':pet})

def list_user_pets(request):
    pet = Pet.objects.filter(ativo=True, usuario=request.user)
    return render(request, 'list.html', {'pet':pet})

def pet_detail(request, id):
    pet = Pet.objects.get(ativo=True, id=id)
    return render(request, 'pet.html', {'pet':pet})

def logout_user(request):
    logout(request)
    return redirect('/login/')

def login_user(request):
    return render(request, 'login.html')

@csrf_protect
def submit_login(request):
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = authenticate(username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect('/')
        else:
            messages.error(request, 'Usuário e/ou senha inválido(s). Favor tentar novamente!')
    return redirect('/login/')