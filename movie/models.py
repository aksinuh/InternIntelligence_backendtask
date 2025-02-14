from django.db import models
from django.contrib.auth import get_user_model
# Create your models here.

User = get_user_model()


class Movie(models.Model):
    title = models.CharField(max_length=150)
    description  = models.TextField(null=True, blank=True)
    release_date = models.DateField()
    genre = models.ManyToManyField("Genre", related_name="genre_janr")
    rating = models.FloatField(default=0.0)
    poster_image = models.ImageField(upload_to="project\movie_png")
    trailer_url = models.URLField(max_length=300)
    duration = models.DurationField()
    language = models.CharField(max_length=50)
    
    def __str__(self):
        return self.title


class Genre(models.Model):
    name = models.CharField(max_length=50)
    
    def __str__(self):
        return self.name
    
class MovieDetail(models.Model):
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='details')
    director = models.CharField(max_length=200)
    cast = models.TextField()
    budget = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    box_office = models.DecimalField(max_digits=15, decimal_places=2, null=True, blank=True)
    awards = models.TextField(blank=True, null=True)

    def __str__(self):
        return f"Details for {self.movie.title}"
    
    
class Rating(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='ratings')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='ratings')
    score = models.IntegerField()
    comment = models.TextField(blank=True, null=True)

    class Meta:
        unique_together = ('user', 'movie')
        constraints = [
            models.CheckConstraint(check=models.Q(score__gte=1, score__lte=5), name='score_range_1_to_5')
        ]

    def __str__(self):
        return f"{self.user.username} - {self.movie.title}: {self.score}"


class SearchHistory(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='search_histories')
    search_term = models.CharField(max_length=200)
    searched_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} searched for '{self.search_term}' on {self.searched_at}"
    
    
class Watchlist(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='watchlist')
    movie = models.ForeignKey(Movie, on_delete=models.CASCADE, related_name='watchlist_entries')

    class Meta:
        unique_together = ('user', 'movie')

    def __str__(self):
        return f"{self.user.username}'s Watchlist: {self.movie.title}"