from RCJ.accounts.models import User
from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import user_passes_test, login_required
from django.contrib.auth import authenticate, login, logout

def user_perm_ti(view_func):
    def _wrapper(request):
        usuario = request.user
        user = get_object_or_404(User, slug = usuario)
        if user.get_nivel() == 0:
            return view_func(request)
        else:
            return redirect ('accounts:cadastro-usuario')
    return _wrapper                

def user_perm_gestores(view_func):
    def _wrapper(request):
        usuario = request.user
        user = get_object_or_404(User, slug = usuario)
        if user.get_nivel() == 1:
            return view_func(request)
        else:
            return redirect ('accounts:cadastro-usuario')       
    return _wrapper    

def user_perm_rh(view_func):
    def _wrapper(request):
        usuario = request.user
        user = get_object_or_404(User, slug = usuario)
        if user.get_nivel() == 2:
            return view_func(request)   
        else:
            return redirect ('accounts:cadastro-usuario')        
    return _wrapper 

def user_perm_back_office(view_func):
    def _wrapper(request):
        usuario = request.user
        user = get_object_or_404(User, slug = usuario)
        if user.get_nivel() == 3:
            return view_func(request)
        else:
            return redirect ('accounts:cadastro-usuario')        
    return _wrapper

def user_perm_supervisor(view_func):
    def _wrapper(request):
        usuario = request.user
        user = get_object_or_404(User, slug = usuario)
        if user.get_nivel() == 4:
            return view_func(request)
        else:
            return redirect ('accounts:cadastro-usuario')
    return _wrapper

def user_perm_operador(view_func):
    def _wrapper(request):
        usuario = request.user
        user = get_object_or_404(User, slug = usuario)
        if user.get_nivel() == 5:
            return view_func(request)
        else:
            return redirect ('accounts:cadastro-usuario')
    return _wrapper       