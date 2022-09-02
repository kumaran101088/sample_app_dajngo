from django.http import JsonResponse
from django.shortcuts import render, redirect
import pandas as pd
from .models import Member
# Create your views here.

def home(request):
    members = Member.objects.all()
    context = {
        'count' : members.count()
    }
    
    return render(request, 'html_files/index.html', context)


