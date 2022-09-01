from django.urls import path, include
from .views import home, task_view, create_task

urlpatterns = [
    path('', home),
    path('create/', create_task, name='create_task'),
    path("task/", task_view, name="task_view")
]