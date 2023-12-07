from django import forms


class disfracesbuscarFormulario(forms.Form):
    disfraces = forms.CharField()
    precio = forms.IntegerField()


class disfracesfiltrados(forms.Form):
    disfraces = forms.CharField()


class disfracesFormulario(forms.Form):
    nombre = forms.CharField()
    precio = forms.IntegerField()