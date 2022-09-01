from django.shortcuts import render
from .cloud_tasks import send_task
from django.http import JsonResponse
import time
# Create your views here.

def home(request):
    return render(request, 'html_files/index.html')

def create_task(request):
    """ A simple view that triggers the task """
    task = "Example Task"
    send_task(url="/task/", payload=task)
    return JsonResponse({'message': "task created"})


def task_view(request):
    """ Processes a task """
    payload = request.body.decode('utf-8')
    time.sleep(20)
    print(f"{payload} is completed")