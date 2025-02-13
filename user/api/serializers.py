from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.serializers import ModelSerializer
from django.utils import timezone
from user.models import Project, Skill, Achievement, Contact

User = get_user_model()

class LoginSerializer(serializers.Serializer):
    username = serializers.CharField(required=False, allow_blank=True)
    email = serializers.EmailField(required=False, allow_blank=True)
    password = serializers.CharField(write_only=True)
    
    
    def validate(self, data):
        username = data.get('username')
        email = data.get('email')
        password = data.get('password')
        
        if not username and not email:
            raise serializers.ValidationError("İstifadəçi adı və ya email daxil edilməlidir.")
        
        if not password:
            raise serializers.ValidationError("Password is required.")
        
        user = None
        
        if username:
            user = authenticate(username=username, password=password)
        elif email:
            try:
                user_obj = User.objects.get(email=email)
                user = authenticate(username= user_obj.username, password=password)
            except User.DoesNotExist:
                raise serializers.ValidationError("No user found with this email.")
        
        if not user:
            raise serializers.ValidationError("Invalid username, email, or password.")
      
      
        refresh = RefreshToken.for_user(user)    
        return{
            'username': user.username,
            'email': user.email,
            'access': str(refresh.access_token),
            'refresh': str(refresh),
            
        }
 
 
        
class ProjectSerializer(serializers.Serializer):
    class Meta:
        model = Project
        fields = {
            'id',
            'title',
            'description',
            'start_data',
            'end_data',
            'image',
            'link',
            'created_at',
            'updated_at'
        }


class ProjectCreateSerializer(serializers.Serializer):
    class Meta:
        model = Project
        fields = {
            'title',
            'description',
            'start_data',
            'end_data',
            'image',
            'link'
        }
        

class SkillSerializer(serializers.Serializer):
    class Meta:
        model = Skill
        fields = {
            'name',
            'proficiency_level',
            'created_at',
            'updated_at'
        }
        
        
class SkillCreateSerializer(serializers.Serializer):
    class Meta:
        model = Skill
        fields = {
            'name',
            'proficiency_level'
        }        


class AchievementSerializer(serializers.Serializer):
    class Meta:
        model = Achievement
        fields = {
            'title',
            'description',
            'date_achieved',
            'created_at',
            'updated_at',
        }        


class AchievementcreateSerializer(serializers.Serializer):
    class Meta:
        model = Achievement
        fields = {
            'title',
            'description',
            'date_achieved',
        }


class contactSerializer(serializers.Serializer):
    class meta:
        model = Contact
        fields = {
            'name',
            'email',
            'message',
            
        }