from django.views.generic import (
    TemplateView,
    ListView,
    DetailView 
)
from django.views.generic.edit import ( 
    CreateView, 
    UpdateView, 
    DeleteView 
)
from django.contrib.postgres.search import SearchVector
from django.shortcuts import render
from django.urls import reverse_lazy
from .models import Candidate
from .tables import CandidateTable
from .filters import CandidateFilter
from django.contrib.auth.mixins import LoginRequiredMixin
from django_filters.views import FilterView
from django_tables2.views import SingleTableMixin
from .forms import SearchForm


class HomePageView(TemplateView):
    template_name = 'home.html'


class FilteredCandidateListView(LoginRequiredMixin, SingleTableMixin, FilterView):
    model = Candidate
    table_class = CandidateTable
    filterset_class = CandidateFilter
    paginate_by = 5  
    template_name = 'candidate/list_candidates.html'

      
class CandidateDetailView(DetailView):
    model = Candidate
    template_name = 'candidate/detail_candidates.html'


class CandidateCreateView(CreateView):
    model = Candidate
    template_name = 'candidate/add_candidates.html'
    success_url = reverse_lazy('list_candidates')
    fields = ['full_name',
                'phone_number_1',
                'phone_number_2',
                'email',
                'position',                    
                'status',
                'interview_date',
                'description',
                'author']


class CandidateUpdateView(UpdateView):
    model = Candidate
    template_name = 'candidate/edit_candidates.html'
    fields = [ 'status',
               'interview_date',
               'description']


class CandidateDeleteView(DeleteView):
    model = Candidate
    template_name = 'candidate/delete_candidates.html'
    success_url = reverse_lazy('list_candidates')


def search_candidates(request):
    form = SearchForm()
    query = None
    results = []
    if 'query' in request.GET:
        form = SearchForm(request.GET)
        if form.is_valid():
            query = form.cleaned_data['query']
            results = Candidate.objects.annotate( search=SearchVector(
                'full_name', 'position'), ).filter(search=query)
    return render(request, 'candidate/search_candidates.html',{'form': form,
                                                                'query': query,
                                                                 'results': results})
