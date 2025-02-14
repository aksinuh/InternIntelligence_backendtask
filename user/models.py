from django.db import models
from django.contrib.auth.models import AbstractUser
# Create your models here.


class User(AbstractUser):
    email = models.EmailField(unique=True)
    
    def get_full_name(self):
        return super().get_full_name()
    
    
class Project(models.Model):
    title = models.CharField(max_length=100)
    description = models.TextField()
    start_data = models.DateField()
    end_data =models.DateField()
    image = models.ImageField(upload_to='projects/', null=True, blank=True)
    link = models.URLField(max_length=300)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.title
    

class Level(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
    
class Skill(models.Model):
    name = models.CharField(max_length=100)
    proficiency_level = models.ForeignKey(Level, on_delete=models.CASCADE, related_name="level") # Bacarıq səviyyəsi (məsələn: Beginner, Intermediate, Advanced)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    
    def __str__(self):
        return self.name
    
    
class Achievement(models.Model):
    title = models.CharField(max_length=255)
    description = models.TextField()
    date_achieved = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    
    
class Contact(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    message = models.TextField()
    submitted_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Message from {self.name}"