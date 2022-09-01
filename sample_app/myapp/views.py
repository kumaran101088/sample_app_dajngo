import os
from google.cloud import storage
from django.http import JsonResponse
from .cloud_tasks import read_convert_file
from django.shortcuts import render, redirect
# Create your views here.

# os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'sample-groi-ec80f9674098.json'
storage_client = storage.Client()

def success_view(request):
    bucket = storage_client.get_bucket('my-fourth-bucket')
    blob = bucket.blob('member_data.csv')
    try:
        blob.delete()
    except:
        pass
    try:
        blob.upload_from_filename('static/MOCK_DATA.csv')
    except:
        return render(request, 'html_files/fail.html')
    try:
        os.remove('static/MOCK_DATA.csv')
    except:
        pass
    return render(request, 'html_files/success.html')

def member_upload_view(request):

    if request.method == 'POST':
        print('BEFORE convert file')
        read_convert_file(request.FILES.get('file'))
        return redirect('success_view')
    return render(request, 'html_files/index.html')

