from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView, CreateAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated, AllowAny
from user.models import Project, Skill, Achievement, Contact
from .serializers import (
    LoginSerializer, ProjectSerializer,
    ProjectCreateSerializer, SkillSerializer,
    SkillCreateSerializer, AchievementSerializer,
    AchievementcreateSerializer, ContactSerializer,
    UserRegistrationSerializer
)

class UserRegistrationView(CreateAPIView):
    serializer_class = UserRegistrationSerializer
    permission_classes = [AllowAny]


class LoginView(GenericAPIView):
    serializer_class = LoginSerializer
    permission_classes = [AllowAny]
    
    
    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        return Response(serializer.validated_data, status=status.HTTP_200_OK)
        

class LogoutView(APIView):
    permission_classes = [IsAuthenticated]

    def post(self, request):
        try:
            refresh_token = request.data.get("refresh")
            if not refresh_token:
                return Response({"error": "Refresh token tələb olunur."}, status=status.HTTP_400_BAD_REQUEST)

            token = RefreshToken(refresh_token)
            token.blacklist()  # Tokeni blackliste əlavə edirik
            return Response({"detail": "Successfully logged out."}, status=status.HTTP_205_RESET_CONTENT)

        except Exception as e:
            return Response({"error": "Invalid refresh token."}, status=status.HTTP_400_BAD_REQUEST)
        

class ProjectListCreateAPIView(ListCreateAPIView):
    serializer_class = ProjectCreateSerializer
    permission_classes = [AllowAny]
    queryset = Project.objects.all()
    
    def get_serializer_class(self):
        if  self.request.method == "GET":
            return ProjectSerializer
        return super().get_serializer_class()
    

class ProjectRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = ProjectCreateSerializer
    permission_classes = [AllowAny]
    queryset = Project.objects.all()
    
    def get_serializer_class(self):
        if  self.request.method == "GET":
            return ProjectSerializer
        return super().get_serializer_class()
    
    
class SkillListCreateAPIView(ListCreateAPIView):
    serializer_class = SkillCreateSerializer
    permission_classes = [AllowAny]
    queryset = Skill.objects.all()
    
    def get_serializer_class(self):
        if  self.request.method == "GET":
            return SkillSerializer
        return super().get_serializer_class()
    

class SkillRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = SkillCreateSerializer
    permission_classes = [AllowAny]
    queryset = Skill.objects.all()
    
    def get_serializer_class(self):
        if  self.request.method == "GET":
            return SkillSerializer
        return super().get_serializer_class()
    
    
class AchievementListCreateAPIView(ListCreateAPIView):
    serializer_class = AchievementcreateSerializer
    permission_classes = [AllowAny]
    queryset = Achievement.objects.all()
    
    def get_serializer_class(self):
        if  self.request.method == "GET":
            return AchievementSerializer
        return super().get_serializer_class()
    

class AchievementRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    serializer_class = AchievementcreateSerializer
    permission_classes = [AllowAny]
    queryset = Achievement.objects.all()
    
    def get_serializer_class(self):
        if  self.request.method == "GET":
            return AchievementSerializer
        return super().get_serializer_class()
    
class ContactCreateAPIView(CreateAPIView):
    serializer_class = ContactSerializer
    permission_classes = [AllowAny]
    