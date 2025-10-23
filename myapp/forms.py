from django import forms

class CreateNewTask(forms.Form):
    titulo = forms.CharField(label='Titulo de la tarea', max_length=200)# esto envia al html no a la DB
    descripcion = forms.CharField(label="Descripcion de la tarea",widget=forms.Textarea)
    
    
class CreateNewProject(forms.Form):
    nombre_proyecto=forms.CharField(label='Titulo del proyecto', max_length=200)