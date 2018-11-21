from django import forms
from .models import Comida
from django.contrib.auth.forms import AuthenticationForm
from django.forms.widgets import PasswordInput, TextInput

class Menu(forms.ModelForm):

    class Meta:
        model = Comida
        fields = ('Menu', 'Plato')
        widgets = {
            'Menu': 'Seccion': forms.Select(attrs={'class': 'form-control custom-select-value'}),
  		      'Plato': 'Seccion': forms.Select(attrs={'class': 'form-control custom-select-value'}),
 			
        }
