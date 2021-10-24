from django.urls import path
# from watchlist_app.api.views import movie_list,movie_details # import function based views
from watchlist_app.api.views import MovieList,MovieDetails # import class based views

urlpatterns = [
   
    # url for function based views
    # path('list/', movie_list, name='movie-list'),
    # path('<int:id>', movie_details, name="movie-details")

    # url for class based views
    path('list/', MovieList.as_view(), name='Movie-List'),
    path('<int:id>', MovieDetails.as_view(), name="Movie-Details")
]