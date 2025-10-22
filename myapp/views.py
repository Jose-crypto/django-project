from django.http import HttpResponse 
from .models import Project , Task
from django.shortcuts import render

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
    return render(request, 'projects.html',{
        'projects': projects
    })

def tasks(request,title):
    #tareas= Task.objects.get(title=title)
    return render(request, 'tasks.html')