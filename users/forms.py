from django import forms
from .models import User


class SignupForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ["group"]

    def signup(self, request, user):
        user.group = self.cleaned_data["group"]
        user.save()
