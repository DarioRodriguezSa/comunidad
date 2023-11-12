from django import forms
from .models import estate, tipo


class estateForm(forms.ModelForm):
    nombre = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Nombre del estate",
                "class": "form-control"
            }
        )
    )

    class Meta:
        model = estate
        fields = ['nombre']

    def __init__(self, *args, **kwargs):
        super(estate.self).__init__(*args, **kwargs)
        self.fields['nombre'].label = "Estado_Evento"       




class tipoForm(forms.ModelForm):
    nombre = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Nombre del tipo",
                "class": "form-control"
            }
        )
    )

    class Meta:
        model = tipo
        fields = ['nombre']

    def __init__(self, *args, **kwargs):
        super(tipo.self).__init__(*args, **kwargs)
        self.fields['nombre'].label = "tipo_evento" 

