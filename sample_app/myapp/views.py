from django.http import JsonResponse
from django.shortcuts import render, redirect
import pandas as pd
from .models import Member
# Create your views here.

def home(request):
    return render(request, 'html_files/index.html')


