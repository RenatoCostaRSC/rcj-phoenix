from RCJ.core.forms import EnderecoClienteForm, ContatoClientForm, ProdutoForm, ClientForm, InfoVendaForm, InfoAuditoriaForm
from RCJ.core.models import EnderecoCliente, ContatoCliente, Client, InfoVenda, Produto, InfoAuditoria
from RCJ.accounts.models import User
from django.shortcuts import render, redirect, get_object_or_404


# Create your views here.
################################################# CRUD PRODUTO #########################################################################
def create_produto(request):
    template_name = 'core/create_produto.html'
    if request.method == 'POST':
        form = ProdutoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('#')
    else:
        form = ProdutoForm()
    context = {
        'form':form
    }
    return render(request, template_name, context)

def edit_produto(request, pk):
    template_name = 'core/edit_produto.html'
    produto = get_object_or_404(Produto, pk = pk)
    if request.method == 'POST':
        form = ProdutoForm(request.POST, instance = produto)
        if form.is_valid():
            form.save()
        return redirect('core:cadastrar_produto')
    else:
        form = ProdutoForm(instance = produto)
    context = {
        'form':form
    }
    return render(request, template_name, context)

def delete_produto(request, pk):
    template_name = 'core/delete_produto.html'
    produto = get_object_or_404(Produto, pk = pk)
    if request.method == 'POST':
        produto.delete()
        return redirect('#')
    context = {
        'produto': produto
    }
    return render(request, template_name, context)

def list_produtos(request):
    template_name = 'core/list_produtos.html'
    produto = Produto.objects.all()
    context = {
        'produto': produto
    }
    return render(request, template_name, context)
#####################################################################################################################################################################

######################################################### CRUD FICHA CLIENTE ########################################################################################

def implanta_ficha_cliente(request):
    template_name = 'core/implanta_ficha.html'
    if request.method == 'POST':
        teste = InfoVenda()
        usuario = User.objects.get(username = request.user.get_username())
        print(usuario.gestor)
        operador = usuario.funcionario.name
        gestor = usuario.gestor
        form1 = ClientForm(request.POST)
        form2 = EnderecoClienteForm(request.POST)
        form3 = ContatoClientForm(request.POST)
        form4 = InfoVendaForm(request.POST)
        form5 = InfoAuditoriaForm(request.POST)
        print(form1.errors)
        print(form2.errors)
        print(form3.errors)
        print(form4.errors)
        print(form5.errors)
        if form1.is_valid() and form2.is_valid() and form3.is_valid() and form4.is_valid():
            venda = form4.save(commit = False)
            cliente = form1.save(commit = False)
            endereco = form2.save()
            contato = form3.save()
            infoauditoria = form5.save()
            cliente.endereco = endereco
            cliente.contato = contato
            cliente.save()
            venda.cliente = cliente
            venda.info_auditoria = infoauditoria
            venda.supervisor = gestor
            venda.operador = operador
            venda.save()
            return redirect('#')
    else:
        form1 = ClientForm()
        form2 = EnderecoClienteForm()
        form3 = ContatoClientForm()
        form4 = InfoVendaForm()
        form5 = InfoAuditoriaForm()
    context = {
        'form1':form1,
        'form2':form2,
        'form3':form3,
        'form4':form4,
        'form5':form5
    }
    return render(request, template_name, context)

def fila_clientes(request):
    template_name = 'core/fila_cliente.html'
    infovenda = InfoVenda.objects.all()
    context = {
        'fila':infovenda
    }
    return render(request, template_name, context)

def tratar_clientes(request, slug, pk):
    template_name = 'core/tratar_cliente.html'
    cliente = get_object_or_404(Client, slug = slug)
    endereco = get_object_or_404(EnderecoCliente, pk = pk)
    contato = get_object_or_404(ContatoCliente, pk = pk)
    infovenda = get_object_or_404(InfoVenda, pk = pk)
    infoauditoria = get_object_or_404(InfoAuditoria, pk = pk)
    if request.method == 'POST':
        form1 = ClientForm(request.POST, instance = cliente)
        form2 = EnderecoClienteForm(request.POST, instance = endereco)
        form3 = ContatoClientForm(request.POST, instance = contato)
        form4 = InfoVendaForm(request.POST, instance = infovenda)
        form5 = InfoAuditoriaForm(request.POST, instance = infoauditoria)
        
        if form1.is_valid() and form2.is_valid() and form3.is_valid() and form4.is_valid():
            cliente = form1.save(commit = False)
            venda = form4.save(commit = False)
            endereco = form2.save()
            contato = form3.save()
            infoauditoria = form5.save()
            cliente.endereco = endereco
            cliente.contato = contato
            cliente.save()
            venda.cliente = cliente
            venda.info_auditoria = infoauditoria
            venda.save()
            return redirect('#')
    else:
        form1 = ClientForm(instance = cliente)
        form2 = EnderecoClienteForm(instance = endereco)
        form3 = ContatoClientForm(instance = contato)
        form4 = InfoVendaForm(instance = infovenda)
        form5 = InfoAuditoriaForm(instance = infoauditoria)
    context = {
        'form1': form1,
        'form2': form2,
        'form3': form3,
        'form4': form4,
        'form5': form5,
    }
    return render(request, template_name, context)
                
            
            
        
