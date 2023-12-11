from django import forms

class disfracesbuscarformulario(forms.Form):
    nombre = forms.CharField(label='nombre', max_length=30, required=True)

class disfracesFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    precio = forms.IntegerField()

class tipodisfracesFormulario(forms.Form):
    clase = forms.CharField(max_length=30)
    talle = forms.IntegerField()
    cantidad = forms.IntegerField()