from django.contrib import admin
from auth_.models import User


@admin.register(User)
class UserAdmin(admin.ModelAdmin):
    exclude = []

