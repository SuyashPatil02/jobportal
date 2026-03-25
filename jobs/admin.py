from django.contrib import admin
from .models import Job, Application

# Job admin (upgrade version)
@admin.register(Job)
class JobAdmin(admin.ModelAdmin):
    list_display = ('title', 'company', 'location', 'posted_by', 'created_at')
    search_fields = ('title', 'company', 'location')
    list_filter = ('company', 'location')


# Application admin (PRO LEVEL 🚀)
@admin.register(Application)
class ApplicationAdmin(admin.ModelAdmin):
    list_display = ('applicant', 'job', 'status', 'applied_at')
    list_filter = ('status', 'applied_at')
    search_fields = ('applicant__username', 'job__title')
    list_editable = ('status',)   # 🔥 Direct status change from admin