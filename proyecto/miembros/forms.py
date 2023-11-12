from django import forms
from .models import estadocivil , nacionalidad, genero

class EstadoCivilForm(forms.ModelForm):
    nombre = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Nombre del estado civil",
                "class": "form-control"
            }
        )
    )

    class Meta:
        model = estadocivil
        fields = ['nombre']

    def __init__(self, *args, **kwargs):
        super(EstadoCivilForm, self).__init__(*args, **kwargs)
        self.fields['nombre'].label = "Estado Civil" 
        
        
        
        
        
class GeneroForm(forms.ModelForm):
    nombre = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Nombre del género",
                "class": "form-control"
            }
        )
    )

    class Meta:
        model = genero
        fields = ['nombre']

    def __init__(self, *args, **kwargs):
        super(GeneroForm, self).__init__(*args, **kwargs)
        self.fields['nombre'].label = "Género"






class NacionalidadForm(forms.ModelForm):
    nombre = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Nombre de la nacionalidad",
                "class": "form-control"
            }
        )
    )

    class Meta:
        model = nacionalidad
        fields = ['nombre']

    def __init__(self, *args, **kwargs):
        super(NacionalidadForm, self).__init__(*args, **kwargs)
        self.fields['nombre'].label = "Nacionalidad"        