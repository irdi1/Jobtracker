from django.db import models
from django.contrib.auth.models import User

# Create your models here.
class Job(models.Model):
    STATUS_CHOICES = [
        ('applied', 'Applied'),
        ('interview', 'Interview'),
        ('offer', 'Offer'),
        ('rejected', 'Rejected'),
        ]

    position = models.CharField(max_length=100)
    company =  models.CharField(max_length=100)
    status = models.CharField(max_length=20, choices=STATUS_CHOICES, default='applied')
    notes = models.TextField(blank=True)
    applied_date = models.DateField(auto_now_add=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='jobs')


    def __str__(self):
        return f"{self.position} at {self.company} ({self.status})"
    
