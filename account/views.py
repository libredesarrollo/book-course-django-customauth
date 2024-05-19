import os

from django.conf import settings
from django.urls import reverse
from django.shortcuts import render, redirect
from django.contrib.auth import login # as make_login
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import BaseUserCreationForm

from .models import UserProfile
from .forms import UserProfileForm

# from .forms import CustomUserCreationForm

# Create your views here.

def register(request):
    form = BaseUserCreationForm()

    if request.method == 'POST':
        form = BaseUserCreationForm(data=request.POST)
        if form.is_valid():
            user = form.save()
            login(request,user)

            return redirect(reverse('login'))

    return render(request, 'register.html', {'form':form})

@login_required
def profile(request):

    form = UserProfileForm()
    pathOldAvatar = None
    userprofile = None

    try:
        userprofile = UserProfile.objects.get(user = request.user)      
        form = UserProfileForm(instance=userprofile)  
    except UserProfile.DoesNotExist:
        pass

    if request.method == "POST":
        try:
            userprofile = UserProfile.objects.get(user = request.user)        
            form = UserProfileForm(request.POST, request.FILES, instance=userprofile)

            pathOldAvatar = os.path.join(settings.MEDIA_ROOT, userprofile.avatar.name)

        except UserProfile.DoesNotExist:
            form = UserProfileForm(request.POST, request.FILES)

        if form.is_valid():
            userprofile = form.save(commit=False)
            userprofile.user = request.user
            userprofile.save()

            if pathOldAvatar is not None and os.path.isfile(pathOldAvatar):
                os.remove(pathOldAvatar)

    return render(request, 'profile.html', {'form':form, 'userprofile':userprofile})