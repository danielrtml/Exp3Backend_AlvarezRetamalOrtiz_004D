from django import forms
from django.forms import ModelForm, fields
from django.forms import widgets
from django.forms.models import ModelChoiceField
from django.forms.widgets import Widget
from .models import Motivo, Usuario


class UsuarioForm(forms.ModelForm):

    class Meta:
        model=Usuario
        fields = ['NickUsuario', 'nombre', 'email', 'mensaje', 'idMotivo']
        labels ={
            'NickUsuario': 'Nick de usuario',
            'nombre': 'Nombre de usuario',
            'email': 'Email del usuario',
            'mensaje': 'Mensaje del usuario',
            'idMotivo': 'Motivo de la consulta'
            
        }
        widgets={
            'NickUsuario': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder':'Ingrese su nick',
                    'id': 'NickUsuario'
                }
            ),
            'nombre': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su nombre',
                    'id': 'nombre'
                }
            ),
            'email': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su correo',
                    'id': 'email'
                }
            ),
            'mensaje': forms.TextInput(
                attrs={
                    'class': 'form-control',
                    'placeholder': 'Ingrese su mensaje'
                    'id': 'mensaje',
                }
            ),
            'idMotivo': forms.Select(
                attrs={
                    'class': 'form-control',
                    'id': 'idMotivo'
                }
            )
        }