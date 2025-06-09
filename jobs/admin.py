from django.contrib import admin
from .models import Job

class JobAdmin(admin.ModelAdmin):
    list_display = ('position', 'company', 'status')
    search_fields = ('company',)

admin.site.register(Job, JobAdmin)

# Register your models here.
