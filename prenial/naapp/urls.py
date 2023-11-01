# urls.py
from django.urls import path
from django.contrib.auth import views as auth_views
from . import views
from django.conf.urls.static import static
from django.conf import settings
urlpatterns = [
    path('login/', auth_views.LoginView.as_view(template_name='login.html'), name='login'),
    path('organizations/', views.organization_list, name='organization_list'),
    path('organization/<int:pk>/', views.organization_detail, name='organization_detail'),
    path('organization/create/', views.organization_create, name='organization_create'),
    path('organization/<int:pk>/update/', views.organization_update, name='organization_update'),
    path('organization/<int:pk>/delete/', views.organization_delete, name='organization_delete'),
    path('superadmin/organizations/', views.superadmin_organization_list, name='superadmin_organization_list'),
    path('signup/', views.signup, name='signup'),
    path('update_profile/', views.update_profile, name='update_profile'),
    path('accounts/profile/', views.profile, name='profile'),
    path('logout/', views.user_logout, name='logout'),
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)