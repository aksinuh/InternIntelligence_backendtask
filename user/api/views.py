from rest_framework.generics import GenericAPIView
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import APIView
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework.permissions import IsAuthenticated
from .serializers import LoginSerializer, ProjectSerializer, ProjectCreateSerializer, SkillSerializer, SkillCreateSerializer, AchievementSerializer


class LoginView(GenericAPIView):
    serializer_class = LoginSerializer
    
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
        
    