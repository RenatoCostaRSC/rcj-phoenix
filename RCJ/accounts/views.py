from RCJ.accounts.forms import RegisterForm, EditAccountForm, SetPasswordCustomForm
from RCJ.accounts.models import User
from RCJ.funcionarios.models import Funcionario, Gestor
from RCJ.accounts.decorators import user_perm_ti, user_perm_gestores
from django.shortcuts import render, redirect, get_object_or_404,reverse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from django.urls import reverse




################################### CRUD USER ################################### 

def register_user(request):
    template_name = 'accounts/register_user.html'
    funcionario = Funcionario.objects.all()
    gestor = Gestor.objects.all()
    if request.method == 'POST':
        form = RegisterForm(request.POST)
        print(form.errors)
        if form.is_valid():
            print('formulario valido')
            form.save()
            return redirect('accounts:usuarios-cadastrados')
    else:
        form = RegisterForm()
    context = {
        'form': form,
        'funcionario': funcionario,
        'gestor': gestor
    }
    return render(request, template_name, context)

def edit_user(request, slug):
    template_name = 'accounts/edit_user.html'
    user = get_object_or_404(User, slug = slug)
    if request.method == 'POST':
        form1 = EditAccountForm(request.POST, instance = user)
        form2 = SetPasswordCustomForm(data=request.POST, user = user)
        if form1.is_valid() and form2.is_valid():
            form1.save()
            form2.save()
            return redirect('accounts:usuarios-cadastrados')
    else:
        form1 = EditAccountForm(instance = user)
        form2 = SetPasswordCustomForm(user=user)
    context = {
        'form1': form1,
        'form2': form2
        
    }
    return render(request, template_name, context)

#@login_required(login_url='accounts:login') # primeiro verificar se o usuario esta logado
#@user_perm_gestores # segundo verificar se o usuario tem acesso a view

def list_user(request):
    template_name = 'accounts/list_user.html'
    user = User.objects.all()
    context = {
        'user_list': user
    }
    return render (request, template_name, context)

def delete_user(request, slug):
    template_name = 'accounts/delete_user.html'
    user = get_object_or_404(User, slug = slug)
    user.delete()
    return redirect('accounts:usuarios-cadastrados')
    context = {
        'user': user
    }
    return render(request, template_name, context)

################################### LOGIN/LOGOUT USER ################################### 

def user_login(request):
    template_name = 'accounts/login.html'
    if request.POST:
        username = request.POST.get('username')
        password = request.POST.get('password')
        print(username)
        user = authenticate(request, username = username , password = password)
        teste = request.user.username
        if user is not None:
            login(request, user)
            return redirect('accounts:usuarios-cadastrados')
    else:
    #messages.error(request, 'Usuario ou senha invalidos. Tente novamente.')
        return render(request,template_name)

def user_logout(request):
    logout(request)
    return redirect('accounts:login')