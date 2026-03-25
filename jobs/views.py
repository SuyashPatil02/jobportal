from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.contrib.auth import logout
from .models import Job, Application


# 🔍 Job List Page with Search
def job_list(request):

    query = request.GET.get('q')

    if query:
        jobs = Job.objects.filter(title__icontains=query)
    else:
        jobs = Job.objects.all()

    return render(request, 'job_list.html', {'jobs': jobs})


# 📄 Job Detail Page
def job_detail(request, job_id):
    job = get_object_or_404(Job, id=job_id)
    return render(request, 'job_detail.html', {'job': job})


# 📝 Apply Job
@login_required
def apply_job(request, job_id):

    job = get_object_or_404(Job, id=job_id)

    if request.method == 'POST':

        resume = request.FILES.get('resume')
        cover_letter = request.POST.get('cover_letter')

        if resume and cover_letter:

            Application.objects.create(
                job=job,
                applicant=request.user,
                resume=resume,
                cover_letter=cover_letter
            )

            return redirect('job_list')

    return render(request, 'apply_job.html', {'job': job})


# 👤 User Dashboard
@login_required
def dashboard(request):

    applications = Application.objects.filter(applicant=request.user)

    return render(request, 'dashboard.html', {
        'applications': applications
    })


# 🏢 Employer Dashboard (HR Panel)
@login_required
def employer_dashboard(request):

    jobs = Job.objects.filter(posted_by=request.user)

    applications = Application.objects.filter(job__posted_by=request.user)

    return render(request, 'employer_dashboard.html', {
        'jobs': jobs,
        'applications': applications
    })


# 🔥 Approve / Reject Application
@login_required
def update_status(request, app_id, status):

    application = get_object_or_404(Application, id=app_id)

    # 🔐 Security check (HR only)
    if application.job.posted_by != request.user:
        return redirect('employer_dashboard')

    application.status = status
    application.save()

    return redirect('employer_dashboard')


# 🚪 Logout
def logout_view(request):
    logout(request)
    return redirect('job_list')