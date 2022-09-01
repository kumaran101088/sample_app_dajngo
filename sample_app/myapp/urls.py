from django.urls import path, include
from .views import member_upload_view, success_view

urlpatterns = [
    path('upload_members/', member_upload_view, name='upload_members'),
    path('success/', success_view, name='success_view')

]