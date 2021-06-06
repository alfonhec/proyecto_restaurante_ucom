from django.db.models import fields
from django import forms
from .models import Cliente

class ClientesForm(forms.ModelForm):

    class Meta:

        model= Cliente

        fields = [
            'id_cliente',
            'nombre',
            'apellido',
            'documento',
            'celular',
            'email',
            'ultima_compra',
            'id_tipo_documento',
            'id_ciudad',
            'id_nacionalidad', 
        ]
        labels = {
            'id_cliente': 'Codigo Cliente',
            'nombre': 'Nombre',
            'apellido': 'Apellido',
            'documento':'Nro. documento',
            'celular':'Celular',
            'email':'Email',
            'ultima_compra': 'Ultima Compra',
            'id_tipo_documento': 'Tipo Documento',
            'id_ciudad': 'Ciudad',
            'id_nacionalidad': 'Nacionalidad',
        }

        widgets = {
            'id_cliente': forms.TextInput(attrs={'class': 'form-control mb-2 form-row'}),
            'nombre': forms.TextInput(attrs={'class': 'form-control mb-2'}),
            'apellido': forms.TextInput(attrs={'class': 'form-control'}),
            'documento': forms.TextInput(attrs={'class': 'form-control'}),
            'celular': forms.TextInput(attrs={'class': 'form-control form-row' }),
            'email': forms.TextInput(attrs={'class': 'form-control'}),
            'ultima_compra': forms.TextInput(attrs={'class': 'form-control'}),
            'id_tipo_documento': forms.TextInput(attrs={'class': 'form-control'}),
            'id_ciudad':forms.TextInput(attrs={'class': 'form-control'}),
            'id_nacionalidad': forms.TextInput(attrs={'class': 'form-control'}),
        }

