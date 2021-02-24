from django.db import models
from django.utils import timezone
from django.urls import reverse
from django.conf import settings
from django.contrib.auth.models import User


class Candidate(models.Model):
    STATUS_CHOICES = (
        ('new', 'New'),
        ('reviewed', 'Reviewed'),
        ('first_interview', 'First Interview'),
        ('second_interview', 'Second Interview'),
        ('third_interview', 'Third Interview'),
        ('testing', 'Testing'),
        ('offer', 'Offer'),
        ('hired', 'Hired'),
        ('rejected', 'Rejected'),
        ('declined', 'Declined'),
        ('inactive', 'Inactive'),
    )
    full_name = models.CharField(max_length=250, verbose_name="Full name" )
    phone_number_1 = models.CharField(max_length=25)
    phone_number_2 = models.CharField(max_length=25, blank=True)
    email = models.EmailField(max_length=100, blank=True)
    position = models.CharField(max_length=250, verbose_name="Position" )
    author = models.ForeignKey(User, related_name='candidates_created',
                                     on_delete=models.CASCADE)    
    description = models.TextField( blank=True )
    interview_date = models.DateTimeField(default=timezone.now, verbose_name="Interview date" )
    created = models.DateTimeField(auto_now_add=True, verbose_name="Created" )
    updated = models.DateTimeField(auto_now=True, verbose_name="Updated" )
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='new', verbose_name="Status" )
    
    class Meta:
        ordering = ('-interview_date',)

    def __str__(self):
        return self.full_name

    def get_absolute_url(self):
        return reverse('detail_candidates', args=[str(self.id)])
   