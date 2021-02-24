from django_filters import FilterSet
from .models import Candidate


class CandidateFilter(FilterSet):
    class Meta:
        model = Candidate
        fields = { 'status': ['exact'], 'position': ['exact', 'contains'], }
