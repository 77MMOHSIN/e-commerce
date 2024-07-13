from django import forms
from .models import Customer
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm,UsernameField,PasswordChangeForm,PasswordResetForm,SetPasswordForm
from django.contrib.auth.models import User
from django.contrib.auth import password_validation
from django.utils.translation import gettext,gettext_lazy as _


class CustomerRegistrationForm(UserCreationForm):
    Email=forms.EmailField(required=True,widget=forms.EmailInput(attrs={'class':'form-control'}))
    password1=forms.CharField(label='Password',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    password2=forms.CharField(label='Confirm Password(again)',widget=forms.PasswordInput(attrs={'class':'form-control'}))
    class Meta:
        model=User
        fields=['username','Email','password1','password2']
        widgets={'username':forms.TextInput(attrs={'class':'form-control' })}
        # widgets={email:forms.EmailInput(attrs={'class':'form-control'})}
        
        
        
        
class LoginForm(AuthenticationForm):
    username=UsernameField(widget=forms.TextInput(attrs={'autofocus':True,'class':'form-control'}))
    password=forms.CharField(label=_('Password'),strip= False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'})) 
    
    
    
    
class MYpassword(PasswordChangeForm):
     old_password=forms.CharField(label=_('Old Password'),strip= False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))
     new_password1=forms.CharField(label=_('New Password'),strip= False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}),
     help_text=password_validation.password_validators_help_text_html())
     new_password2=forms.CharField(label=_('new_password(again)'),strip= False,widget=forms.PasswordInput(attrs={'autocomplete':'current-password','class':'form-control'}))    
class Customerprofileform(forms.ModelForm):
    class Meta:
        model=Customer
        fields=['name','locality','city','state','zipcode']
        widgets={'name':forms.TextInput(attrs={'class':'form-control'}),'locality':forms.TextInput(attrs={'class':'form-control'}),'city':forms.TextInput(attrs={'class':'form-control'}),'state':forms.TextInput(attrs={'class':'form-control'}),'zipcode':forms.TextInput(attrs={'class':'form-control'})}
                           
                
        
                    
                