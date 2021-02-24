from django_tables2.utils import A  # alias for Accessor
import django_tables2 as tables
from .models import Candidate


class CandidateTable(tables.Table):
    full_name = tables.LinkColumn('detail_candidates', args=[A('pk')])
    
    class Meta:
        model = Candidate
        template_name = 'django_tables2/semantic.html'
        exclude = ('description', 'author', 'email', 'phone_number_2', 'phone_number_1')
        sequence = ('id',
                    'full_name',
                    'position',
                    'status',
                    'interview_date',
                    'updated',
                    'created' )
