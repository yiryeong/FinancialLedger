from django.shortcuts import render
from django.urls import reverse
from allauth.account.views import PasswordChangeView


def index(request):
    return render(request, "users/index.html")


class CustomPasswordChangeView(PasswordChangeView):
    def get_success_url(self):
        return reverse("index")
