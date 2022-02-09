from django.contrib import admin
from django.contrib.auth.admin import UserAdmin
from .models import Group


# Register your models here.
admin.site.register(Group)
UserAdmin.fieldsets += (("Custom fields", {"fields": ("group",)}),)
