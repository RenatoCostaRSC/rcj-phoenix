from django.contrib.auth.forms import UserCreationForm, SetPasswordForm
from RCJ.accounts.models import User
from django import forms
from django.contrib import messages

class RegisterForm(forms.ModelForm):
    
    password1 = forms.CharField(label = 'Senha', widget = forms.PasswordInput) 
    password2 = forms.CharField(label = 'Confirmação de Senha', widget = forms.PasswordInput)
    
    def clean_user(self):
        
        user = self.cleaned_data['user']
        if User.objects.filter(user = user).exists():
            raise forms.ValidationError('Usuario já existe')
        return user
    
    def clean_password2(self):
        
        password1 = self.cleaned_data.get("password1")
        password2 = self.cleaned_data.get("password2")
        
        if password1 and password2 and password1 != password2:
            raise forms.ValidationError('A confirmação de senha esta incorreta') 
        return password2
    
    def save(self, commit = True):
        
        user = super(RegisterForm, self).save(commit = False)
        user.set_password(self.cleaned_data['password1'])
        if commit:
            user.save()
        return user
    
    class Meta:
        model = User
        fields = ['username','email', 'nivel', 'funcionario','gestor']
        
class EditAccountForm(forms.ModelForm):
    
    def clean_user(self):
            
        user = self.cleaned_data['user']
        queryset = User.objects.filter(user = user).exclude(pk = self.instance.pk) 
        if queryset.exists():
            raise forms.ValidationError('Usuario já existe')
        return user
    
    class Meta:
        model = User
        fields = ['username','email', 'nivel', 'funcionario','gestor']
        
class SetPasswordCustomForm(SetPasswordForm):
    """
    A form that lets a user change set their password without entering the old
    password
    """
    error_messages = {
        'password_mismatch':("The two password fields didn't match."),
    }
    new_password1 = forms.CharField(label="New password",
                                    widget=forms.PasswordInput)
    new_password2 = forms.CharField(label="New password confirmation",
                                    widget=forms.PasswordInput)

    def __init__(self, user, *args, **kwargs):
        self.user = user
        super(SetPasswordForm, self).__init__(*args, **kwargs)

    def clean_new_password2(self):
        password1 = self.cleaned_data.get('new_password1')
        password2 = self.cleaned_data.get('new_password2')
        if password1 and password2:
            if password1 != password2:
                print('oi')
                raise forms.ValidationError(
                    self.error_messages['password_mismatch'],
                    code='password_mismatch',
                )
        return password2

    def save(self, commit=True):
        self.user.set_password(self.cleaned_data['new_password1'])
        if commit:
            self.user.save()
        return self.user
        