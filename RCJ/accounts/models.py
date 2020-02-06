from django.contrib.auth.models import AbstractBaseUser, PermissionsMixin, UserManager
from django.core import validators
from django.db import models
from django.urls import reverse
import re
from .utils import unique_slug_generator
from django.db.models import signals
from django.utils.text import slugify
from django.db.models.signals import pre_save

from RCJ.funcionarios.models import Funcionario, Gestor

# Create your models here.


class User(AbstractBaseUser, PermissionsMixin):
    
    NIVEL_CHOICES = (
        (5, 'OPERADOR'),
        (4, 'SUPERVISOR'),
        (3, 'BACKOFFICE'),
        (2, 'RECURSOS HUMANOS'),
        (1, 'DIRETORIA'),
        (0, 'TI')        
    )
    
    username = models.CharField(
        'Usuario', max_length = 30, unique = True,
        validators=[validators.RegexValidator(re.compile('^[\w.@+-]+$'),'O nome de usuario só pode conter letras, digitos ou os '
        'seguintes caracteres: @/./+/-/_', 'invalid')])
    slug = models.SlugField('atalho', max_length = 40, unique = True, null = False, blank = True)
    nivel = models.IntegerField(choices = NIVEL_CHOICES, null = False, blank = False)
    email = models.EmailField('E-mail', unique = True)
    funcionario = models.ForeignKey(Funcionario, verbose_name=('Funcionario'), on_delete=models.CASCADE)
    gestor = models.ForeignKey(Gestor, verbose_name=('Gestor'), on_delete=models.CASCADE)
    name = models.CharField('Nome', max_length = 50, blank = True)
    is_active = models.BooleanField('Esta Ativo?', default = True)
    is_staff = models.BooleanField('É da Equipe?', default = False)
    is_admin = models.BooleanField('É administrador do sistema?', default = False)
    date_joined = models.DateField('Data de Cadastro', auto_now_add = True)
    
    objects = UserManager()
    
    USERNAME_FIELD = 'username'
    REQUIRED_FIELDS = ['email']    
        
    def __str__(self):
        return self.funcionario.name
    
    def get_short_name(self):
        return self.username
    
    def get_full_name(self):
        return str(self)
    
    def get_absolute_url(self):
        return reverse('user_detail', kwargs={'slug': self.slug})
    
    def get_nivel(self):
        return self.nivel
    
    class Meta:
        verbose_name= 'Usuário'
        verbose_name_plural = 'Usuários' 


def usuario_pre_save_receiver(sender, instance, *args, **kwargs):
    #teste = slugify(instance.name) + '-%s'  % instance.cpf.cpf 
    instance.slug = slugify(instance.username)
    
pre_save.connect(usuario_pre_save_receiver, sender = User)  

"""
def user_pre_save_receiver(sender, instance, *args, **kwargs):
    if not instance.slug:
        instance.slug = unique_slug_generator(instance)
pre_save.connect(user_pre_save_receiver, sender = User)
"""   
