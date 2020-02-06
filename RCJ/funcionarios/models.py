#from .utils import unique_slug_generator
from django.db.models.signals import pre_save
from django.db.models import signals
from django.utils.text import slugify
import re
from django.urls import reverse
from django.db import models


class Gestor(models.Model):
    
    nome = models.CharField('Nome', max_length=50)
    
    def __str__(self):
        return self.nome

class Funcionario(models.Model):
    
    CARGO_CHOICES = (
        ('TI', 'TI'),
        ('DIRETORIA', 'DIRETORIA'),
        ('RECURSOS HUMANOS', 'RECURSOS HUMANOS'),
        ('BACKOFFICE', 'BACKOFFICE'),
        ('SUPERVISOR', 'SUPERVISOR'),
        ('OPERADOR', 'OPERADOR')
    )
    
    SEX_CHOICES = (
        ('M', 'MASCULINO'),
        ('F', 'FEMININO')
    )
    ESTADO_CIVIL_CHOICES = (
        ('SOLTEIRO', 'SOLTEIRO'),
        ('CASADO', 'CASADO'),
        ('DIVORCIDADO', 'DIVORCIADO')
    )
    CHILDREN_CHOICES = (
        ('SIM','SIM'),
        ('NAO','NÃO')
    )
    AMOUNT_OF_CHILDREN_CHOICES = (
        (0,'0'),
        (1,'1'),
        (2,'2'),
        (3,'3'),
        (4,'4'),
        (5,'5'),
        (6,'6'),
        (7,'7'),
        (8,'8'),
        (9,'9'),
        (10,'10'),   
    )
    DEGREE_OF_INSTITUTION_CHOICES = (
        ('ENSINO FUNDAMENTAL COMPLETO','ENSINO FUNDAMENTAL COMPLETO'),
        ('ENSINO FUNDAMENTAL INCOMPLETO','ENSINO FUNDAMENTAL INCOMPLETO'),
        ('ENSINO MEDIO COMPLETO','ENSINO MÉDIO COMPLETO'),
        ('ENSINO MEDIO COMPLETO','ENSINO MÉDIO INCOMPLETO'),
        ('ENSINO SUPERIOR COMPLETO','ENSINO SUPERIOR COMPLETO'),
        ('ENSINO SUPERIOR INCOMPLETO','ENSINO SUPERIOR INCOMPLETO')
    )
    name = models.CharField('Nome', max_length = 50, null = False, blank = False)
    slug = models.SlugField('Atalho',unique = True)
    date_of_birth = models.DateField('Data de nascimento')
    sex = models.CharField('Sexo', max_length = 1, choices = SEX_CHOICES, null = False, blank = False)
    children = models.CharField('Filhos', max_length = 3, choices = CHILDREN_CHOICES, null = False, blank = False)
    amount_of_children = models.IntegerField('Quantidade de filhos', choices = AMOUNT_OF_CHILDREN_CHOICES, null = False, blank = False, default = 0)
    fathers_name = models.CharField('Nome do pai', max_length = 50, null = False, blank = False)
    mothers_name = models.CharField('Nome da mãe', max_length = 50, null = False, blank = False)
    degree_of_institution = models.CharField('Grau de instituição', max_length = 31, null = False, blank = False)
    cargo = models.CharField('Cargo', max_length = 17, choices = CARGO_CHOICES, null = False, blank = False)
    adress = models.OneToOneField('Endereco', verbose_name=('Endereço'), on_delete=models.CASCADE)
    rg = models.OneToOneField('Rg', verbose_name=('RG'), on_delete = models.CASCADE)
    cpf = models.OneToOneField('Cpf', verbose_name=('CPF'), on_delete = models.CASCADE)
    voter_title = models.OneToOneField('TituloDeEleitor', verbose_name=('Titulo de eleitor'), on_delete = models.CASCADE)
    
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse('funcionario_detail', kwargs={'slug': self.slug})

def funcionario_pre_save_receiver(sender, instance, *args, **kwargs):
    teste = slugify(instance.name) + '-%s'  % instance.cpf.cpf 
    instance.slug = teste
    
pre_save.connect(funcionario_pre_save_receiver, sender = Funcionario)  
     
    
class Endereco(models.Model):
    
    street = models.CharField('Rua', max_length = 50, null = False, blank = False)
    number = models.IntegerField('Numero', null = False, blank = False)
    complement = models.CharField('Complemento', max_length = 50, null = False, blank = False)
    neighborhood = models.CharField('Bairro', max_length = 50, null = False, blank = False)
    city = models.CharField('Cidade', max_length = 50, null = False, blank = False)
    state = models.CharField('Estado', max_length = 50, null = False, blank = False)
    
    def __str__(self):
        return self.street
 
class Rg(models.Model):
    
    rg = models.CharField('RG', max_length = 11, null = False, blank = False, unique = True)
    shipping_date = models.DateField('Data de expedição')
    dispatching_agency = models.CharField('Órgão expeditor', max_length = 10, null = False, blank = False)
    
    def __str__(self):
        return self.rg
    
class Cpf(models.Model):
    
    cpf = models.CharField('CPF', max_length = 11, null = False, blank = False, unique = True)
    
    def __str__(self):
        return self.cpf
    
class TituloDeEleitor(models.Model):

    titulo_de_eleitor = models.CharField('Titulo de eleitor', max_length = 12, null = False, blank = True , unique = True)
    zone = models.CharField('Zona eleitoral', max_length = 12, null = False, blank = True)
    

    

        
    