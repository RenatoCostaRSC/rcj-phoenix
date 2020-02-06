from django.shortcuts import render, redirect, get_object_or_404,reverse
from RCJ.funcionarios.forms import FuncionarioForm, EnderecoForm, RgForm, CpfForm, TituloDeEleitorForm  #FuncionarioTestForm
from RCJ.funcionarios.models import Funcionario, Rg, Cpf, TituloDeEleitor, Endereco, Gestor
from .utils import salva_gestor
    
def create_funcionario(request):
    template_name = 'funcionarios/register_funcionario.html'
    
    if request.method == 'POST':
        form_funcionario = FuncionarioForm(request.POST)
        form_endereco = EnderecoForm(request.POST)
        form_rg = RgForm(request.POST)
        form_cpf = CpfForm(request.POST)
        form_titulo = TituloDeEleitorForm(request.POST)
        nome = request.POST.get('name')
        cargo = request.POST.get('cargo')
        if form_funcionario.is_valid() and form_endereco.is_valid() and form_rg.is_valid() and form_cpf.is_valid() and form_titulo.is_valid():
            print('todos validos')
            funcionario = form_funcionario.save(commit = False)
            endereco = form_endereco.save()
            rg = form_rg.save()
            cpf = form_cpf.save()
            titulo = form_titulo.save()
            funcionario.adress = endereco
            funcionario.rg = rg
            funcionario.cpf = cpf
            funcionario.voter_title = titulo
            funcionario.save()
            salva_gestor(nome,cargo)
            return redirect('funcionarios:lista_funcionario')
    else:
        form_funcionario = FuncionarioForm()
        form_endereco = EnderecoForm()
        form_rg = RgForm()
        form_cpf = CpfForm()
        form_titulo = TituloDeEleitorForm()
    context = {
        'form1': form_funcionario,
        'form2': form_endereco,
        'form3': form_rg,
        'form4': form_cpf,
        'form5': form_titulo,  
    }
    return render(request, template_name, context)
    
def delete_funcionario(request, slug, pk):
    template_name = 'funcionarios/delete_funcionario.html'
    funcionario = get_object_or_404(Funcionario, pk = pk)
    endereco = get_object_or_404(Endereco, pk = pk)
    rg = get_object_or_404(Rg, pk = pk)
    cpf = get_object_or_404(Cpf, pk = pk)
    titulo = get_object_or_404(TituloDeEleitor, pk = pk)
    funcionario.delete()
    endereco.delete()
    rg.delete()
    cpf.delete()
    titulo.delete()
    return redirect('funcionarios:lista_funcionario')
    context = {
        'funcionario': funcionario
    }
    return render(request, template_name, context)

def edit_funcionario(request, slug, pk):
    template_name = 'funcionarios/edit_funcionario.html'
    funcionario = get_object_or_404(Funcionario, pk = pk)
    endereco = get_object_or_404(Endereco, pk = pk)
    rg = get_object_or_404(Rg, pk = pk)
    cpf = get_object_or_404(Cpf, pk = pk)
    titulo = get_object_or_404(TituloDeEleitor, pk = pk)
    if request.method == 'POST':
        form1 = FuncionarioForm(request.POST, instance = funcionario)
        form2 = EnderecoForm(request.POST, instance = endereco)
        form3 = RgForm(request.POST, instance = rg)
        form4 = CpfForm(request.POST, instance = cpf)
        form5 = TituloDeEleitorForm(request.POST, instance = titulo)
        if form1.is_valid() and form2.is_valid() and form3.is_valid() and form4.is_valid() and form5.is_valid():
            funcionario = form1.save(commit = False)
            endereco = form2.save()
            rg = form3.save()
            cpf = form4.save()
            titulo = form5.save()
            funcionario.adress = endereco
            funcionario.rg = rg
            funcionario.cpf = cpf
            funcionario.voter_title = titulo
            funcionario.save()
            
            return redirect('funcionarios:lista_funcionario')
    else:
        form1 = FuncionarioForm(instance = funcionario)
        form2 = EnderecoForm(instance = endereco)
        form3 = RgForm(instance = rg)
        form4 = CpfForm(instance = cpf)
        form5 = TituloDeEleitorForm(instance = titulo)
    context = {
        'form1': form1,
        'form2': form2,
        'form3': form3,
        'form4': form4,
        'form5': form5,
    }
    return render(request, template_name, context)
            

def list_funcionarios(request):
    template_name = 'funcionarios/list_funcionario.html'
    funcionarios = Funcionario.objects.all()
    context = {
        'funcionario_list': funcionarios
    }
    return render(request, template_name, context)    


