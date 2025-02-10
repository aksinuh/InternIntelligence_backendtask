from django.contrib import admin
from django.contrib.auth import get_user_model
# Register your models here.

User = get_user_model()

@admin.register(User)
class Useradmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email']
    list_display_links = ['username']