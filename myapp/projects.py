from django import forms

class ProjectForm(forms.Form):
    name = forms.CharField(label='Titulo del proyecto', max_length=200)