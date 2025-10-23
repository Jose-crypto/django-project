from django.http import HttpResponse 
from .models import Project , Task
from django.shortcuts import render , redirect
from .forms import CreateNewTask
from .projects import ProjectForm
# Create your views here.
def index(request):
    title="Djanngo Course"
    return  render(request, 'index.html', {'title':title} )


def greeting(request,username):
    print(username)
    return HttpResponse('<h1>Hi! %s <h1>' % username)
    
    
def about(request):
    return render(request , 'about.html')


def projects(request):
   # projects = list(Project.objects.values())
    projects = Project.objects.all()
    return render(request, 'projects/projects.html',{
        'projects': projects
    })

def tasks(request):
    tasks= Task.objects.all()
    return render(request, 'tasks/tasks.html',{
        'tasks': tasks
    } )
    
def create_task(request):
    if request.method == 'GET':
        return render(request, 'tasks/form.html',{
            'form': CreateNewTask()
        }) 
    else:
        Task.objects.create(titulo=request.POST['titulo'] ,descripcion=request.POST['descripcion'], project_id=2)
        return redirect('/tasks/')
    

def create_project(request):
    if request.method== 'GET':
        return render(request, 'projects/form_create_project.html',{
            'form': CreateNewTask()
        })
    else:
        ProjectForm.objects.create(name=request.POST['name'])
