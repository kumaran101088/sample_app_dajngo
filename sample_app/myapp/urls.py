from django.urls import path, include
from .views import home, convert, member_view, total_risk_score, individual_risk_score, search

urlpatterns = [

    #TEMPLATES
    path('home/', home, name='home'),
    path('add/', convert, name='add'),
    path('search/', search, name='search'),
    path('member/<int:id>', member_view, name='member_view'),

    #APIs
    path('trs/', total_risk_score, name='total_risk_score'),
    path('irs/<int:id>', individual_risk_score, name='individual_risk_score'),

]