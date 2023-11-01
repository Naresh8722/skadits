from django.db import models
from django.contrib.auth.models import User
class Organization(models.Model):
    name = models.CharField(max_length=100)
    # Add other fields as needed

    def __str__(self):
        return self.name

class UserProfile(models.Model):
    user = models.OneToOneField(User, on_delete=models.CASCADE)
    # org_name=models.OneToOneField(Organization, on_delete=models.CASCADE)
    profile_image = models.ImageField(upload_to='profile_images', blank=True, null=True)
    # Add other fields for the user profile information
    # ...

    def __str__(self):
        return self.user.username