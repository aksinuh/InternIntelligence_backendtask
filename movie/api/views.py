from rest_framework.generics import ListAPIView, ListCreateAPIView,RetrieveUpdateDestroyAPIView
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from movie.models import Movie, SearchHistory, MovieDetail, Rating, Watchlist
from rest_framework.permissions import IsAuthenticated, AllowAny
from .serializers import (
    MovieSerializer, MovieCreateSerializer, 
    MovieDetailSerializer, MovieDetailCreateSerializer,
    RatingSerializer, RatingCreateSerializer,
    WatchlistSerializer, WatchlistCreateSerializer 
    )


class MovieSearchView(ListAPIView):
    queryset = Movie.objects.all()
    serializer_class = MovieSerializer
    filter_backends = [SearchFilter]
    search_fields = ['title', 'genre__name']

    def list(self, request, *args, **kwargs):
        # Axtarış sorğusunu əldə et
        search_query = request.query_params.get('search', '')

        # İstifadəçi daxil olubsa, axtarış tarixçəsini saxla
        if request.user.is_authenticated and search_query:
            SearchHistory.objects.create(user=request.user, search_term=search_query)

        # Axtarışı davam etdir
        return super().list(request, *args, **kwargs)
    
    
class MovieListCreateAPIView(ListCreateAPIView):
    queryset = Movie.objects.all()
    permission_classes = [AllowAny]
    serializer_class = MovieCreateSerializer
    
    def get_serializer_class(self):
        if self.request.method == "GET":
            return MovieSerializer
        return super().get_serializer_class()
    

class MovieRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Movie.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = MovieCreateSerializer
    
    def get_serializer_class(self):
        if self.request.method == "GET":
            return MovieSerializer
        return super().get_serializer_class()
    
    
class MovieDetailListCreateAPIView(ListCreateAPIView):
    queryset = MovieDetail.objects.all()
    permission_classes = [AllowAny]
    serializer_class = MovieDetailCreateSerializer
    
    def get_serializer_class(self):
        if self.request.method == "GET":
            return MovieDetailSerializer
        return super().get_serializer_class()
    

class MovieDetailRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = MovieDetail.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = MovieDetailCreateSerializer
    
    def get_serializer_class(self):
        if self.request.method == "GET":
            return MovieDetailSerializer
        return super().get_serializer_class()
    
    
class RatingListCreateAPIView(ListCreateAPIView):
    queryset = Rating.objects.all()
    permission_classes = [AllowAny]
    serializer_class = RatingCreateSerializer
    
    def get_serializer_class(self):
        if self.request.method == "GET":
            return RatingSerializer
        return super().get_serializer_class()
    

class RatingRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Rating.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = RatingCreateSerializer
    
    def get_serializer_class(self):
        if self.request.method == "GET":
            return RatingSerializer
        return super().get_serializer_class()
    
    
class WatchlistListCreateAPIView(ListCreateAPIView):
    queryset = Watchlist.objects.all()
    permission_classes = [AllowAny]
    serializer_class = WatchlistCreateSerializer
    
    def get_serializer_class(self):
        if self.request.method == "GET":
            return WatchlistSerializer
        return super().get_serializer_class()
    

class WatchlistRetrieveUpdateDestroyAPIView(RetrieveUpdateDestroyAPIView):
    queryset = Watchlist.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = WatchlistCreateSerializer
    
    def get_serializer_class(self):
        if self.request.method == "GET":
            return WatchlistSerializer
        return super().get_serializer_class()
    
