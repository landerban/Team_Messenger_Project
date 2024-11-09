from django import forms
from django.contrib.auth.forms import BaseUserCreationForm
from .models import CustomUser


class UserRegistrationForm(BaseUserCreationForm):
    first_name = forms.CharField(max_length=20)
    last_name = forms.CharField(max_length=20)

    class Meta:
        model = CustomUser
        fields = ['username', 'first_name', 'last_name',
                  'email', 'password1', 'password2']

    def clean(self):
        cleaned_data = super().clean()
        return cleaned_data

    def save(self, commit=True):
        user = super().save(commit=False)
        user.first_name = (self.cleaned_data["first_name"])
        user.last_name = (self.cleaned_data["last_name"])
        user.user_id = (self.cleaned_data["username"])
        if commit:
            user.save()
        return user
