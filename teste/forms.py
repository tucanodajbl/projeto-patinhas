from django import forms

class NameForm(forms.Form):
    your_name = forms.CharField(label='Your name', max_length=100)

class AnimalForm(forms.Form):
    nome = forms.CharField(label='Nome', max_length=100)
    raca = forms.CharField(label='Raça', max_length=100)
    idade = forms.IntegerField(label='Idade Aproximada')
    porte = forms.CharField(label='Porte', max_length=100)
    pelo = forms.CharField(label='Cor do Pelo', max_length=100)
    obs = forms.CharField(label='Observações', max_length=100)
    