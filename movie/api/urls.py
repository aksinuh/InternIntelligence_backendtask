from django.urls import path
from .views import( 
    MovieSearchView, MovieListCreateAPIView,
    MovieRetrieveUpdateDestroyAPIView,MovieDetailListCreateAPIView,
    MovieDetailRetrieveUpdateDestroyAPIView, WatchlistListCreateAPIView,
    WatchlistRetrieveUpdateDestroyAPIView, RatingListCreateAPIView,
    RatingRetrieveUpdateDestroyAPIView
    )

urlpatterns = [
    path('search/', MovieSearchView.as_view(), name='movie-search'),
    path('movie/', MovieListCreateAPIView.as_view(), name='movie-listcreate'),
    path('movie/<int:pk>', MovieRetrieveUpdateDestroyAPIView.as_view(), name='movie-Retrieve-Update-Destroy'),
    path('movie/detail/', MovieDetailListCreateAPIView.as_view(), name='movie-listcreate'),
    path('movie/detail/<int:pk>', MovieDetailRetrieveUpdateDestroyAPIView.as_view(), name='movie-Retrieve-Update-Destroy'),
    path('watchlist/', WatchlistListCreateAPIView.as_view(), name='Watchlist-listcreate'),
    path('watchlist/<int:pk>', WatchlistRetrieveUpdateDestroyAPIView.as_view(), name='Watchlist-Retrieve-Update-Destroy'),
    path('rating/', RatingListCreateAPIView.as_view(), name='Rating-listcreate'),
    path('rating/<int:pk>', RatingRetrieveUpdateDestroyAPIView.as_view(), name='Rating-Retrieve-Update-Destroy'),
]