from django.http import HttpResponse , JsonResponse
from .models import Project , Task
from django.shortcuts import get_object_or_404

# Create your views here.
def index(request):
    return HttpResponse('Index page')

def greeting(request,username):
    print(username)
    return HttpResponse('<h1>Hi! %s <h1>' % username)
    
    
def about(request):
    return HttpResponse('<h1>About<h1>')


def projects(request):
    projects = list(Project.objects.values())
    return JsonResponse(projects , safe=False)

def tasks(request,id):
    tareas= get_object_or_404(Task,id=id)
    return HttpResponse('Tarea: %s ' % tareas.titulo)