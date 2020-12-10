from django import forms
from .models import Empleado

class RegistroForm(forms.ModelForm):
    """Form definition for Prueba."""

    class Meta:
        """Meta definition for Pruebaform."""

        model = Empleado
        fields = ['first_name','last_name','job','departamento','habilidades']
        widgets = {
            'first_name': forms.TextInput(
                attrs= {
                    'class': 'form-control',                    
                }
            ),
            'last_name': forms.TextInput(
                attrs= {
                    'class': 'form-control',                    
                }
            ),
            'job': forms.Select(
                attrs= {
                    'class': 'mdb-select md-form colorful-select dropdown-primary',                    
                }
            ),
            'departamento': forms.Select(
                attrs= {
                    'class': 'mdb-select md-form colorful-select dropdown-primary',                    
                }
            ),
            'habilidades': forms.SelectMultiple(
                attrs= {
                    'class': 'form-control',                    
                }
            )
        }
    
    #validaciones del campo cantidad clean_atributo
    def clean_cantidad(self):
        cantidad = self.cleaned_data['cantidad']
        if cantidad < 10:
            raise forms.ValidationError('Ingrese un numero mayor a 10')
        
        return cantidad

