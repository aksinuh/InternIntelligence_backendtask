from django.contrib import admin
from django.contrib.auth import get_user_model
from .models import Movie, Genre, MovieDetail, Rating, SearchHistory, Watchlist
# Register your models here.

@admin.register(Movie)
class Movieadmin(admin.ModelAdmin):
    list_display = ['id', 'title', 'release_date', 'rating', 'language']
    list_display_links = ['title']
    

@admin.register(Genre)
class Genreadmin(admin.ModelAdmin):
    list_display = ['id', 'name']
    list_display_links = ['name']
    
    
@admin.register(MovieDetail)
class MovieDetailadmin(admin.ModelAdmin):
    list_display = ['id', 'movie', 'director', 'cast', 'awards']
    list_display_links = ['id']
    
    
@admin.register(Rating)
class Ratingadmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'movie', 'score']
    list_display_links = ['user']   
    
    
@admin.register(SearchHistory)
class SearchHistoryadmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'search_term', 'searched_at']
    list_display_links = ['id']
    
    
@admin.register(Watchlist)
class Watchlistadmin(admin.ModelAdmin):
    list_display = ['id', 'user', 'movie']
    list_display_links = ['id']
    