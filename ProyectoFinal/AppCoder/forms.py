from django import forms


class disfracesbuscarFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    precio = forms.IntegerField()

class disfracesFormulario(forms.Form):
    nombre = forms.CharField(max_length=30)
    precio = forms.IntegerField()