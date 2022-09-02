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
    # df = pd.read_csv(r'C:\Users\Kumaran\Desktop\MOCK_DATA.csv')
    # for row in range(1, 10000):
    #     member = Member(
    #         member_id = df.loc[row, 'id']+1,
    #         age = df.loc[row, 'age_new'],
    #         gender = df.loc[row, 'gender'],
    #         height = df.loc[row, 'height_new'],
    #         weight = df.loc[row, 'weight_new'],
    #         st_bp = df.loc[row, 'ap_hi_new'],
    #         dy_bp = df.loc[row, 'ap_lo_new'],
    #         chol = df.loc[row, 'cholesterol'],
    #         gluc = df.loc[row, 'gluc'],
    #         smoke = df.loc[row, 'smoke'],
    #         alco = df.loc[row, 'alco'],
    #         active = df.loc[row, 'active'],
    #         cardio = df.loc[row, 'cardio'],
    #         medication = df.loc[row, 'medication_new']
    #     )
    #     member.save()
    return render(request, 'html_files/index.html', context)


