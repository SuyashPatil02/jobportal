from django.urls import path
from . import views

urlpatterns = [

    # Jobs
    path('', views.job_list, name='job_list'),
    path('job/<int:job_id>/', views.job_detail, name='job_detail'),
    path('job/<int:job_id>/apply/', views.apply_job, name='apply_job'),

    # User Dashboard
    path('dashboard/', views.dashboard, name='dashboard'),

    # HR Dashboard
    path('employer-dashboard/', views.employer_dashboard, name='employer_dashboard'),

    # 🔥 Approve / Reject
    path('update-status/<int:app_id>/<str:status>/', views.update_status, name='update_status'),
]