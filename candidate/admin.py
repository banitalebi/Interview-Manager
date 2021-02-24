from django.contrib import admin
from .models import Candidate


@admin.register(Candidate)
class CandidateAdmin(admin.ModelAdmin):
    list_display = ('full_name', 'position', 'interview_date', 'status', 'updated', 'created')
    list_filter = ('status', 'created', 'updated', 'position', 'author')
    search_fields = ('full_name', 'phone_number_1', 'phone_number_2', 'email', 'description')
    raw_id_fields = ('author',)
    date_hierarchy = 'interview_date'
    ordering = ('full_name', 'position', 'interview_date', 'status', 'updated', 'created')
    list_per_page = 5
