from django.urls import path, include
from .views import home, convert, member_view

urlpatterns = [
    path('home/', home, name='home'),
    path('add/', convert, name='add'),
    path('member/<int:id>', member_view, name='member_view'),

]