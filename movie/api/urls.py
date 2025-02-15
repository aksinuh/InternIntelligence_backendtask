from django.urls import path
from .views import MovieSearchView

urlpatterns = [
    path('search/', MovieSearchView.as_view(), name='movie-search'),
]