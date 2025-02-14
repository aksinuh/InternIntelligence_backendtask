from django.urls import path
from .views import (
    LoginView, LogoutView, ProjectListCreateAPIView,
    ProjectRetrieveUpdateDestroyAPIView,SkillListCreateAPIView,
    SkillRetrieveUpdateDestroyAPIView, AchievementListCreateAPIView,
    AchievementRetrieveUpdateDestroyAPIView, ContactCreateAPIView
)


urlpatterns = [
    path('login/', LoginView.as_view(), name='login'),
    path('logout/',LogoutView.as_view(), name='logout'),
    path('project/', ProjectListCreateAPIView.as_view(), name="Project_ListCreate"),
    path('project/<int:pk>',ProjectRetrieveUpdateDestroyAPIView.as_view(), name="Project_RetrieveUpdate_Destroy"),
    path('skill/', SkillListCreateAPIView.as_view(), name="skill_ListCreate"),
    path('skill/<int:pk>',SkillRetrieveUpdateDestroyAPIView.as_view(), name="skill_RetrieveUpdate_Destroy"),
    path('achievement/', AchievementListCreateAPIView.as_view(), name="achievement_ListCreate"),
    path('achievement/<int:pk>',AchievementRetrieveUpdateDestroyAPIView.as_view(), name="achievement_RetrieveUpdate_Destroy"),
    path('contact/', ContactCreateAPIView.as_view(), name="contactcreate"),
]

