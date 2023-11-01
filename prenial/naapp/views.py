from django.shortcuts import render, get_object_or_404, redirect
from .models import Organization
from .forms import OrganizationForm 
from django.contrib.auth.decorators import login_required

def organization_list(request):
    organizations = Organization.objects.all()
    return render(request, 'organization_list.html', {'organizations': organizations})

@login_required
def organization_detail(request, pk):
    if request.user.is_superuser:
        organization = get_object_or_404(Organization, pk=pk)
        return render(request, 'organization_detail.html', {'organization': organization})
    else:
        return redirect('login')
@login_required
def organization_create(request):
    if request.user.is_superuser:
        if request.method == 'POST':
            form = OrganizationForm(request.POST)
            if form.is_valid():
                form.save()  # Saves the form data to the database
                return redirect('organization_list')  # Redirect to organization list after creation
        else:
            form = OrganizationForm()  # Empty form for GET requests

        return render(request, 'organization_create.html', {'form': form})
    else:
        return redirect('organization_list')

@login_required        
def organization_update(request, pk):
    organization = get_object_or_404(Organization, pk=pk)
    if request.user.is_superuser:
        if request.method == 'POST':
            form = OrganizationForm(request.POST, instance=organization)
            if form.is_valid():
                form.save()  # Saves the updated form data to the database
                return redirect('organization_list')  # Redirect to organization list after update
        else:
            form = OrganizationForm(instance=organization)  # Prefill form with existing organization data

        return render(request, 'organization_update.html', {'form': form, 'organization': organization})
    else:
        return redirect('login')
@login_required
def organization_delete(request, pk):
    organization = get_object_or_404(Organization, pk=pk)
    if request.user.is_superuser:
        if request.method == 'POST':
            organization.delete()  # Deletes the organization
            return redirect('organization_list')  # Redirect to organization list after deletion

        return render(request, 'organization_delete.html', {'organization': organization})
    else:
        return redirect('login') 
@login_required
def superadmin_organization_list(request):
    if request.user.is_superuser:
        organizations = Organization.objects.all()
        return render(request, 'superadmin_organization_list.html', {'organizations': organizations})
    else:
        return redirect('login')  # Redirect to the login page for unauthorized users


from .forms import SignUpForm

def signup(request):
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            # Redirect to a success page or login page
            return redirect('login')
    else:
        form = SignUpForm()
        # print(form)    
    return render(request, 'signup.html', {'form': form})


from django.contrib.auth import update_session_auth_hash
from django.contrib.auth.models import User
from .forms import UserProfileForm, ChangePasswordForm
@login_required
def update_profile(request):
    user = request.user
    profile = user.userprofile if hasattr(user, 'userprofile') else None

    if request.method == 'POST':
        profile_form = UserProfileForm(request.POST, request.FILES, instance=profile)
        password_form = ChangePasswordForm(request.POST)

        if profile_form.is_valid():
            profile = profile_form.save(commit=False)
            profile.user = user
            profile.save()

        if password_form.is_valid():
            new_password = password_form.cleaned_data['new_password']
            user.set_password(new_password)
            user.save()
            update_session_auth_hash(request, user)  # Update the user's session to prevent logout

        return redirect('profile')  # Redirect to the profile view or any other page after updates

    else:
        profile_form = UserProfileForm(instance=profile)
        password_form = ChangePasswordForm()
        # print(profile_form)
        # print(password_form)
    return render(request, 'update_profile.html', {'profile_form': profile_form, 'password_form': password_form})

@login_required
def profile(request):
    user = request.user
    profile = user.userprofile if hasattr(user, 'userprofile') else None
    return render(request, 'profile.html', {'user': user, 'profile': profile})

from django.contrib.auth import logout
from django.shortcuts import redirect
def user_logout(request):
    logout(request)
    # Redirect to a different page after logging out, such as the login page or home page
    return redirect('login')  # Ch