from rest_framework import serializers
from django.contrib.auth import authenticate
from django.contrib.auth import get_user_model
from rest_framework_simplejwt.tokens import RefreshToken
from movie.models import Movie, MovieDetail, Rating, SearchHistory, Watchlist, Genre


class GenreSerilizer(serializers.ModelSerializer):
    class Meta:
        model = Genre
        fields = ('name',)


class MovieSerializer(serializers.ModelSerializer):
    genre = GenreSerilizer(many=True)
    class Meta:
        model = Movie
        fields = (
            'id',
            'title',
            'description',
            'release_date',
            'genre',
            'rating',
            'poster_image',
            'trailer_url',
            'duration',
            'language',

        )
        
        
class MovieCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Movie
        fields = (
            'title',
            'description',
            'release_date',
            'genre',
            'rating',
            'poster_image',
            'trailer_url',
            'duration',
            'language',

        )
        

class MovieDetailSerializer(serializers.ModelSerializer):
    movie = serializers.CharField(source="movie.title")
    class Meta:
        model = MovieDetail
        fields = (
            'id',
            'movie',
            'director',
            'cast',
            'budget',
            'box_office',
            'awards',
            
        )
        
        
class MovieDetailCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = MovieDetail
        fields = (
            'movie',
            'director',
            'cast',
            'budget',
            'box_office',
            'awards',
            
        )
        
class RatingSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.username")
    movie = serializers.CharField(source="movie.title")
    class Meta:
        model = Rating
        fields = (
            'id',
            'user',
            'movie',
            'score',
            'comment',
        )
        
        
class RatingCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Rating
        fields = (
            'user',
            'movie',
            'score',
            'comment',
        )
        
        
class WatchlistSerializer(serializers.ModelSerializer):
    user = serializers.CharField(source="user.username")
    movie = serializers.CharField(source="movie.title")
    class Meta:
        model = Watchlist
        fields = (
            'id',
            'user',
            'movie',
        )


class WatchlistCreateSerializer(serializers.ModelSerializer):
    class Meta:
        model = Watchlist
        fields = (
            'user',
            'movie',
        )
