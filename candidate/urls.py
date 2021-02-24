from django.urls import path
from . import views


urlpatterns = [
    path('<int:pk>/delete/', views.CandidateDeleteView.as_view(), name='delete_candidates'),
    path('<int:pk>/edit/', views.CandidateUpdateView.as_view(), name='edit_candidates'),
    path('new/', views.CandidateCreateView.as_view(), name='add_candidates'),
    path('<int:pk>/', views.CandidateDetailView.as_view(), name='detail_candidates'),
    path('list_candidates/', views.FilteredCandidateListView.as_view(), name='list_candidates'),
    path('search/', views.search_candidates, name='search_candidates'),
]
