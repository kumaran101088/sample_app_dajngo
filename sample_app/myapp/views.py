import pandas as pd
from rest_framework import status
import datetime, statistics, time
from .filters import MemberFilter
from .models import Member, Activity
from django.http import JsonResponse
from rest_framework.response import Response
from django.shortcuts import render, redirect
from rest_framework.decorators import api_view

# df = pd.read_csv(r'C:\Users\Kumaran\Desktop\dailySteps_merged.csv', low_memory=False)

def home_view(request):

    smokers = Member.objects.filter(smoke=1).count()
    alcoholics = Member.objects.filter(alco=1).count()
    female = Member.objects.filter(gender=2).count()
    male = Member.objects.filter(gender=1).count()
    total_members = Member.objects.all().count()
    chol_high = Member.objects.filter(chol=3).count()
    gluc_high = Member.objects.filter(gluc=3).count()
    cardio_members = Member.objects.filter(cardio=1).count()
    n_active_members = Member.objects.filter(active=0).count()

    context = {
        'smokers' : smokers,
        'alcoholics' : alcoholics,
        'female' : female,
        'male' : male,
        'total_members' : total_members,
        'chol_high' : chol_high,
        'gluc_high' : gluc_high,
        'cardio_members' : cardio_members,
        'n_active_members' : n_active_members
    }

    return render(request, 'html_files/index.html', context)

def search_view(request):
    if request.method == 'POST':
        try:
            value = int(request.POST.get('search'))
            ind_member = Member.objects.filter(member_id=value)[0]
        except Exception as e:
            return render(request, 'html_files/not_found.html')
        return redirect('member_view', ind_member.member_id)
    else:
        return render(request, 'html_files/search.html')

def member_view(request, id):
    try:
        ind_member = Member.objects.filter(member_id=id)[0]
        total_activities = Activity.objects.filter(patient=ind_member)
        total_steps = sum([activity.steps for activity in total_activities])
        member_active = 1
        if ind_member.active == 0:
            if total_steps/len(total_activities) < 7000:
                member_active = 0
        activities = Activity.objects.filter(patient=ind_member).order_by('-a_date')[:9]
        recent_steps = [activity.steps for activity in activities]
        recent_dates = [activity.a_date.strftime("%d/%m/%Y") for activity in activities]
        age = 2016 - (datetime.date(2016, 12, 5) - datetime.timedelta(days=ind_member.age)).year

    # for index in range(20, 500):
    #     print(index)
    #     try:
    #         ind_member = Member.objects.filter(member_id=index)[0]
    #         activities = Activity.objects.filter(patient=ind_member)
    #         for activity in activities:
    #             members = len(Activity.objects.filter(patient=ind_member).filter(a_date=activity.a_date))
    #             print(members)
    #             if members > 1:
    #                 print(Activity.objects.filter(patient=ind_member).filter(a_date=activity.a_date).last().delete())
    #     except:
    #         print(f'not found {index}')


        context = {
            'member': ind_member,
            'recent_steps' : recent_steps,
            'recent_dates' : recent_dates,
            'total_steps' : total_steps,
            'member_active' : member_active,
            'age' : age,
        }

    except:
        return render(request, 'html_files/not_found.html')
    return render(request, 'html_files/member.html', context)

@api_view(['GET'])
def individual_risk_score(request, id):
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
    return Response({'risk_score' : risk_score}, status=status.HTTP_200_OK)

@api_view(['GET'])
def total_risk_score(request):
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
    median_risk_score = statistics.median(percentile_scores)
    average_risk_score = round(sum(percentile_scores)/len(percentile_scores))
    return Response({'median_risk_score' : median_risk_score, 'average_risk_score' : average_risk_score}, status=status.HTTP_200_OK)

def convert(request):
    # for row in range(311, len(df)):
    #     date = df.loc[row, 'ActivityDay'].split('/')
    #     new_date = datetime.date(int(date[-1]), int(date[0]), int(date[1]))
    #     if Member.objects.filter(member_id=df.loc[row, 'member_id']).exists():
    #         activity = Activity(
    #             patient = Member.objects.filter(member_id=df.loc[row, 'member_id'])[0],
    #             a_date = new_date,
    #             steps = df.loc[row, 'StepTotal']
    #         )
    #         print(row, Member.objects.filter(member_id=df.loc[row, 'member_id'])[0], new_date, df.loc[row, 'StepTotal'])
    #         activity.save()
    return render(request, 'html_files/home.html')

