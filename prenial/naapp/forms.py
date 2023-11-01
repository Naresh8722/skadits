from django import forms
from .models import Organization

class OrganizationForm(forms.ModelForm):
    class Meta:
        model = Organization
        fields = ['name'] 


from django import forms
from django.contrib.auth.models import User
from .models import Organization

class SignUpForm(forms.Form):
    organization = forms.ModelChoiceField(queryset=Organization.objects.all())
    first_name = forms.CharField(max_length=100)
    last_name = forms.CharField(max_length=100)
    email = forms.EmailField()
    mobile_number = forms.CharField(max_length=15)
    password = forms.CharField(widget=forms.PasswordInput)
    confirm_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get("password")
        confirm_password = cleaned_data.get("confirm_password")

        if password != confirm_password:
            raise forms.ValidationError("Passwords do not match")

    def save(self):
        org = self.cleaned_data['organization']
        first_name = self.cleaned_data['first_name']
        last_name = self.cleaned_data['last_name']
        email = self.cleaned_data['email']
        mobile_number = self.cleaned_data['mobile_number']
        password = self.cleaned_data['password']

        user = User.objects.create_user(username=email, email=email, password=password, first_name=first_name, last_name=last_name)
        # Additional user attributes assignment
        user.save()
        return user


from django.contrib.auth.models import User
from .models import UserProfile

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ['profile_image',]  # Include other profile fields

class ChangePasswordForm(forms.Form):
    old_password = forms.CharField(widget=forms.PasswordInput)
    new_password = forms.CharField(widget=forms.PasswordInput)
    confirm_new_password = forms.CharField(widget=forms.PasswordInput)

    def clean(self):
        cleaned_data = super().clean()
        new_password = cleaned_data.get("new_password")
        confirm_new_password = cleaned_data.get("confirm_new_password")

        if new_password != confirm_new_password:
            raise forms.ValidationError("New passwords do not match")
