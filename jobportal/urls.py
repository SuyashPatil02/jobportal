from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static

from django.contrib.auth import views as auth_views

urlpatterns = [

    # 🔐 Admin Panel
    path('admin/', admin.site.urls),

    # 🔐 Authentication (Login / Logout)
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('logout/', auth_views.LogoutView.as_view(next_page='/'), name='logout'),

    # 📦 Apps
    path('', include('jobs.urls')),
    path('', include('users.urls')),
]

# 📁 Media files (Resume upload)
if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)