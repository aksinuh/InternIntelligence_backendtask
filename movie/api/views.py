from rest_framework.generics import ListAPIView
from rest_framework.response import Response
from rest_framework.filters import SearchFilter
from movie.models import Movie, SearchHistory
from .serializers import MovieSerializer

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