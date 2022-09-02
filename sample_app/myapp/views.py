from django.http import JsonResponse
from django.shortcuts import render, redirect
import pandas as pd
from .models import Member, Activity
import datetime, statistics
# Create your views here.

# df = pd.read_csv(r'C:\Users\Kumaran\Desktop\dailySteps_merged.csv', low_memory=False)

def home(request):
    members = Member.objects.all()
    individual_scores, percentile_scores = [], []
    for member in members:
        bmi = round((member.weight/(member.height*member.height)) * 10000)
        medication = 1 if member.medication == 'Y' else 0
        bp = round((member.st_bp+member.dy_bp)/2)
        score = (bmi*10) + (member.smoke*10) + (medication*10) + (member.alco*10) + (member.age*10) + (member.active*10) + (member.cardio*20) + (bp*10) + (member.gluc*10)
        individual_scores.append(score)
    for score in individual_scores:
        percentile_scores.append(round((len(list(filter(lambda x : x < score, individual_scores)))/len(individual_scores)) * 100))
    risk_score = statistics.median(percentile_scores)
    context = {
        'risk_score': risk_score
    }
    return render(request, 'html_files/index.html', context)

def member_view(request, id):
    try:
        ind_member = Member.objects.filter(member_id=id)[0]
        ind_bmi = round((ind_member.weight/(ind_member.height*ind_member.height)) * 10000)
        ind_medication = 1 if ind_member.medication == 'Y' else 0
        ind_bp = round((ind_member.st_bp+ind_member.dy_bp)/2)
        individual_score = (ind_bmi*10) + (ind_member.smoke*10) + (ind_medication*10) + (ind_member.alco*10) + (ind_member.age*10) + (ind_member.active*10) + (ind_member.cardio*20) + (ind_bp*10) + (ind_member.gluc*10)
    except:
        pass
    members = Member.objects.all()
    individual_scores, percentile_scores = [], []
    for member in members:
        bmi = round((member.weight/(member.height*member.height)) * 10000)
        medication = 1 if member.medication == 'Y' else 0
        bp = round((member.st_bp+member.dy_bp)/2)
        score = (bmi*10) + (member.smoke*10) + (medication*10) + (member.alco*10) + (member.age*10) + (member.active*10) + (member.cardio*20) + (bp*10) + (member.gluc*10)
        individual_scores.append(score)
    risk_score = round((len(list(filter(lambda x : x < individual_score, individual_scores)))/len(individual_scores)) * 100)
    return render(request, 'html_files/member.html', {'member' : ind_member, 'risk_score' : risk_score})

def convert(request):
    # for row in range(0, len(df)):
    #     date = df.loc[row, 'ActivityDay'].split('/')
    #     new_date = datetime.date(int(date[-1]), int(date[0]), int(date[1]))
    #     activity = Activity(
    #         patient = Member.objects.filter(member_id=df.loc[row, 'member_id'])[0],
    #         a_date = new_date,
    #         steps = df.loc[row, 'StepTotal']
    #     )
    #     activity.save()
    return render(request, 'html_files/home.html')

