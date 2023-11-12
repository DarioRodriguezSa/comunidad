from django import forms
from .models import status , categoria, duracion, curso, clase, tiempo


class statusForm(forms.ModelForm):
    nombre = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Nombre del status",
                "class": "form-control"
            }
        )
    )

    class Meta:
        model = status
        fields = ['nombre']

    def __init__(self, *args, **kwargs):
        super(status, self).__init__(*args, **kwargs)
        self.fields['nombre'].label = "Estado_actividad"




class tiempoForm(forms.ModelForm):
    nombre = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Nombre del status",
                "class": "form-control"
            }
        )
    )

    class Meta:
        model = tiempo
        fields = ['nombre']

    def __init__(self, *args, **kwargs):
        super(tiempo, self).__init__(*args, **kwargs)
        self.fields['nombre'].label = "Tiempo_actividad"       





class categoriaForm(forms.ModelForm):
    nombre = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Nombre de la Categoria",
                "class": "form-control"
            }
        )
    )

    class Meta:
        model = categoria
        fields = ['nombre']

    def __init__(self, *args, **kwargs):
        super(categoria, self).__init__(*args, **kwargs)
        self.fields['nombre'].label = "Categoría_Actividad"




class duracionForm(forms.ModelForm):
    nombre = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Nombre de la duracion",
                "class": "form-control"
            }
        )
    )

    class Meta:
        model = duracion
        fields = ['nombre']

    def __init__(self, *args, **kwargs):
        super(duracion, self).__init__(*args, **kwargs)
        self.fields['nombre'].label = "Duración_Actividad"        


class cursoForm(forms.ModelForm):
    nombre = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Nombre del curso",
                "class": "form-control"
            }
        )
    )

    class Meta:
        model = curso
        fields = ['nombre']

    def __init__(self, *args, **kwargs):
        super(curso, self).__init__(*args, **kwargs)
        self.fields['nombre'].label = "Curso_Actividad"   



class claseForm(forms.ModelForm):
    nombre = forms.CharField(
        widget=forms.TextInput(
            attrs={
                "placeholder": "Nombre de la clase",
                "class": "form-control"
            }
        )
    )

    class Meta:
        model = clase
        fields = ['nombre']

    def __init__(self, *args, **kwargs):
        super(clase, self).__init__(*args, **kwargs)
        self.fields['nombre'].label = "Clase_Actividad"                