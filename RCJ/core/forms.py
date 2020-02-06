from django import forms
from RCJ.core.models import EnderecoCliente, ContatoCliente, Produto, Client, InfoVenda, InfoAuditoria


class EnderecoClienteForm(forms.ModelForm):
    
    class Meta:
        
        model = EnderecoCliente
        fields = '__all__' 
        
class ContatoClientForm(forms.ModelForm):
    
    class Meta:
        
        model = ContatoCliente
        fields = '__all__' 
        
class ProdutoForm(forms.ModelForm):
    
    class Meta:
        
        model = Produto
        fields= '__all__'

class ClientForm(forms.ModelForm):
    
    class Meta:
        
        model = Client
        exclude = ('endereco', 'contato')
        
    
class InfoAuditoriaForm(forms.ModelForm):
    
    class Meta:
        
        model = InfoAuditoria
        exclude = {'auditor'}
        
class InfoVendaForm(forms.ModelForm):
    
    class Meta:
        
        model = InfoVenda
        exclude = ('cliente','status_auditoria','status_pos_venda','created_date','info_auditoria','operador','supervisor')
        """
        widgets = {'operador': forms.HiddenInput(),
                    'supervisor': forms.HiddenInput()}
        """