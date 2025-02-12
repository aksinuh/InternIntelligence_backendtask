from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Project,Level, Skill, Achievement, Contact
# Register your models here.

User = get_user_model()

@admin.register(User)
class Useradmin(admin.ModelAdmin):
    list_display = ['id', 'username', 'email']
    list_display_links = ['username']


@admin.register(Level)
class Leveladmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['name']
    
    
@admin.register(Skill)
class Skilladmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'proficiency_level']
    list_display_links = ['name']
    
    
@admin.register(Achievement)
class Achievementadmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'date_achieved']
    list_display_links = ['title']


@admin.register(Contact)
class Contactadmin(admin.ModelAdmin):
    list_display = ['id', 'name', 'email']
    list_display_links = ['name']
    
    
@admin.register(Project)
class Projectadmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'description']
    list_display_links = ['title']