from django.contrib import admin

# Register your models here.
from .models import UserProfile, Organization

admin.site.register(UserProfile)
admin.site.register(Organization)