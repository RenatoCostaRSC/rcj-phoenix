from RCJ.funcionarios.models import Funcionario, Endereco, Rg, Cpf, TituloDeEleitor
from django import forms
from django.utils.text import slugify
from django.shortcuts import get_object_or_404


class FuncionarioForm(forms.ModelForm):
    
    class Meta:
        
        model = Funcionario
        exclude = ('rg','cpf','voter_title','adress','slug')

class EnderecoForm(forms.ModelForm):
    
    class Meta:
        
        model = Endereco
        fields = '__all__'
        
        
class RgForm(forms.ModelForm):
        
    class Meta:
        
        model = Rg
        fields = '__all__'
        error_messages = {
            'rg' : {
                'unique' : ("Rg já cadastrado no sistema")
            }
        }
                
class CpfForm(forms.ModelForm):
    
    class Meta:
        
        model = Cpf
        fields = '__all__'
        error_messages = {
            'cpf' : {
                'unique' : ("CPF já cadastrado no sistema")
            }
        }
        
class TituloDeEleitorForm(forms.ModelForm):
    
    class Meta:
        
        model = TituloDeEleitor
        fields = '__all__'
        error_messages = {
            'titulo_de_eleitor' : {
                'unique' : ("Titulo de eleitor já cadastrado no sistema")
            }
        }        