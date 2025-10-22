from django.http import HttpResponse


# Create your views here.


def greeting(request):
    return HttpResponse('<h1>Hi!<h1>')
    
    
def about(request):
    return HttpResponse('<h1>About<h1>')
