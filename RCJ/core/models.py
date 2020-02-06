from django.db import models

#from .utils import unique_slug_generator
from django.db.models.signals import pre_save
from django.db.models import signals
from django.utils.text import slugify

class EnderecoCliente(models.Model):
    
    street = models.CharField('Rua', max_length = 50, null = False, blank = False)
    number = models.IntegerField('Numero', null = False, blank = False)
    complement = models.CharField('Complemento', max_length = 50, null = False, blank = False)
    neighborhood = models.CharField('Bairro', max_length = 50, null = False, blank = False)
    reference_point = models.CharField('Ponto de referência', max_length = 50, null = False, blank = True)
    city = models.CharField('Cidade', max_length = 50, null = False, blank = False)
    state = models.CharField('Estado', max_length = 50, null = False, blank = False)

class ContatoCliente(models.Model):
    
    telefone_1 = models.CharField('Telefone 1', max_length = 11, null = True, blank = True)
    telefone_2 = models.CharField('Telefone 2', max_length = 11, null = True, blank = True)
    email = models.EmailField('E-mail', max_length = 50, null = True, blank = True)

class Produto(models.Model):
    
    EMPRESA_CHOICES = (
        ('SKY','SKY'),
        ('OI','OI'),
        ('CLARO','CLARO'),
        ('TIM', 'TIM')
    )
    
    TIPO_PRODUTO_CHOICES = (
        ('TV','TV'),
        ('BANDA_LARGA','BANDA LARGA'),
        ('MOVEL','MOVEL')
    )
    
    name = models.CharField('Nome', max_length = 5, choices = EMPRESA_CHOICES, null = False, blank= False)
    plano = models.CharField('Plano', max_length = 50, null = False, blank = False)
    valor = models.DecimalField('Valor', max_digits=5, decimal_places=2)
    
    def __str__(self):
        return self.plano
    

class Client(models.Model):
    
    SEXO_CHOICES = (
        ('M','MASCULINO'),
        ('F','FEMININO')
    )
    
    slug = models.SlugField('atalho', max_length = 11, unique = True, null = False, blank = True)
    name = models.CharField('Nome', max_length = 50, blank = False)
    cpf = models.CharField('CPF', max_length = 11, blank = False, null = False, unique = True)
    rg = models.CharField('RG', max_length = 11, blank = False, null = False, unique = True)
    date_of_birth = models.DateField('Data de Nascimento')
    sex = models.CharField('Sexo', max_length = 1, choices = SEXO_CHOICES)
    endereco = models.OneToOneField("EnderecoCliente", verbose_name=("Endereço"), on_delete=models.CASCADE)
    contato = models.OneToOneField("ContatoCliente", verbose_name=("Contato"), on_delete=models.CASCADE)

    def __str__(self):
        return self.name

def client_pre_save_receiver(sender, instance, *args, **kwargs):
    teste = slugify(instance.name) + '-%s'  % instance.cpf 
    instance.slug = teste
    
pre_save.connect(client_pre_save_receiver, sender = Client)  
    
class InfoAuditoria(models.Model):
    
    STATUS_AUDITORIA_CHOICE = (
        ('APROVADA', 'APROVADA'),
        ('REPROVADA', 'REPROVADA'),
        ('CONSULTAR', 'CONSULTAR'),
        ('CANCELADO', 'CANCELADO'),
        ('DESISTENCIA', 'DESISTENCIA'),
        ('CHECKLIST', 'CHECKLIST'),
        ('PENDENTE', 'PENDENTE')
        
    )
    STATUS_POS_VENDA_CHOICE = (
        ('HABILITADO', 'HABILITADO'),
        ('DESISTENCIA', 'DESISTÊNCIA'),
        ('EM ROTA', 'EM ROTA'),
        ('AGUARDANDO PAGAMENTO','AGUARDANDO PAGAMENTO')
        
    )
    auditor = models.CharField('Auditor', max_length = 50, null = True, blank = True)
    status_auditoria = models.CharField('Status da Auditoria', max_length = 12, choices = STATUS_AUDITORIA_CHOICE, null = True, blank = False, default = 'PENDENTE')
    status_pos_venda =  models.CharField('Status Pós venda', max_length = 21, choices = STATUS_POS_VENDA_CHOICE, null = True, blank = False, default = 'AGUARDANDO PAGAMENTO')
    observacoes = models.TextField('Observações', max_length = 1000, null = True, blank = True)
    
    
class InfoVenda(models.Model):
    
    CANAL_DA_VENDA_CHOICE = (
        ('ATIVO', 'ATIVO'),
        ('PREDITIVO', 'PREDITIVO'),
        ('DISCADOR', 'DISCADOR'),
        ('LEAD', 'LEAD'),
        ('REDES SOCIAIS', 'REDES SOCIAIS')
    )
    
    ADESAO_CHOICE = (
        ('GRATIS','GRÁTIS'),
        ('INTEGRAL','INTEGRAL'),
        ('PARCIAL','PARCIAL')

    )
    FORMA_DE_PAGAMENTO_CHOICE = (
        ('CARTAO DE CREDITO','CARTÃO DE CRÉDITO'),
        ('DEBITO EM CONTA','DÉBITO EM CONTA'),
        ('BOLETO BANCÁRIO','BOLETO BANCÁRIO')
    )
    
    STATUS_VENDA_CHOICE = (
        ('PRE APROVADA','PRE APROVADA'),
        ('REPROVADA','REPROVADA'),
        
    )
    produto = models.ForeignKey(Produto, verbose_name=("Produto"), on_delete=models.CASCADE)
    cliente = models.ForeignKey(Client, verbose_name=("Cliente"), on_delete=models.CASCADE)
    canal_da_venda = models.CharField('Canal da venda', max_length = 14, choices = CANAL_DA_VENDA_CHOICE, null = False, blank = False)
    status_venda = models.CharField('Status da Venda', max_length = 14, choices = STATUS_VENDA_CHOICE, null = False, blank = False )
    info_auditoria = models.OneToOneField("InfoAuditoria", verbose_name=("Informação Auditoria"), on_delete=models.CASCADE)
    operador = models.CharField('Operador', max_length = 50, null = False, blank = False)
    supervisor = models.CharField('Supervisor', max_length = 50, null = False, blank = False)
    created_date = models.DateField('Data da venda', auto_now_add = True)
    adesao = models.CharField('Adesão', max_length = 10, choices = ADESAO_CHOICE, null = False, blank = False)
    forma_de_pagamento = models.CharField('Forma de pagamento', max_length = 17, choices = FORMA_DE_PAGAMENTO_CHOICE, null = False, blank = False)
    observacoes = models.TextField('Observações', max_length = 1000, null = True, blank = True)
    
    def set_operador(self, operador):
        self.operador = operador
        return operador 
    
         
    
    
    
    
