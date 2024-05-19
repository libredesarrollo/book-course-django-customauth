from django import forms
from django.contrib.auth.models import User
from django.core.exceptions import ValidationError
from django.contrib.auth.forms import UserCreationForm
from django.core.files.images import get_image_dimensions

from .models import UserProfile

class CustomUserCreationForm(UserCreationForm):
    email = forms.EmailField(label="Email", max_length=50, help_text='Put your favorite emil', error_messages={'invalid':'Email is invalid'})

    def clean_email(self):
        email = self.cleaned_data['email'].lower()
        u = User.objects.filter(email = email)
        if u.count():
            raise ValidationError('Email is taking')
        
        return email
    
    def save(self, commit=True):
        user = User.objects.create_user(
            self.cleaned_data['username'],
            self.cleaned_data['email'],
            self.cleaned_data['password1'],
        )
        return user

class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('avatar','user', 'address', 'language', 'age')
        widgets = {
            'user': forms.HiddenInput(),
            'address': forms.Textarea(attrs={'rows':3})
        }

    def clean_avatar(self):
        avatar = self.cleaned_data['avatar']

        # size
        w, h = get_image_dimensions(avatar)
        max_width = max_height = 1500
        if w > max_width or h > max_height:
            raise forms.ValidationError('Very large image, the image cannot exceed the %d %d' % (max_width, max_height))
        
        #ext
    
        m,t = avatar.content_type.split('/')
        print(m)
        print(t)
        if not(m == 'image' and t in ['jpeg', 'jpg', 'gif', 'png','webp']):
            raise forms.ValidationError("Image not supported, we only support: 'jpeg', 'jpg', 'gif', 'png'")
        
        #size image
        if len(avatar) > (1024 * 30):
            raise forms.ValidationError('Image cannot exceed 30kb')

        return avatar