from django.urls import path

from . import views

app_name = 'todo'

urlpatterns = [
    # /todo/
    path('', views.index, name='index'),
    # /todo/add_todo/
    path('add_todo/', views.add_todo, name='add_todo'),
    # ex: /todo/1/
    path('<int:todo_id>/', views.steps, name='steps')
]
