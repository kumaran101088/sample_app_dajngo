from django.urls import path, include
from .views import home_view, convert, member_view, total_risk_score, individual_risk_score, search_view

urlpatterns = [

    #TEMPLATES
    path('home/', home_view, name='home'),
    path('add/', convert, name='add'),
    path('search/', search_view, name='search'),
    path('member/<int:id>', member_view, name='member_view'),

    #APIs
    path('trs/', total_risk_score, name='total_risk_score'),
    path('irs/<int:id>', individual_risk_score, name='individual_risk_score'),

]