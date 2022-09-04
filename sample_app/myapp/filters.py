import django_filters
from .models import Member

class MemberFilter(django_filters.FilterSet):
    class Meta:
        model = Member
        fields = ['member_id']