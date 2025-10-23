
from django.urls import path
from . import views

urlpatterns=[
    path('',views.index),
    path('about/',views.about),
    path('hello/<str:username>',views.greeting),
    path('projects/',views.projects),
    path('tasks/',views.tasks),
    path('form/', views.create_task),
    path('form_create_project',views.create_project)
]