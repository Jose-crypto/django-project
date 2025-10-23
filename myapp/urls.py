
from django.urls import path
from . import views

urlpatterns=[
    path('',views.index),
    path('about/',views.about , name='about'),
    path('hello/<str:username>',views.greeting,name='hello'),
    path('projects/',views.projects,name='projects'),
    path('tasks/',views.tasks, name='tasks'), 
    path('form/', views.create_task, name='form'),
    path('form_create_project/',views.create_project, name='form_create_project')
]