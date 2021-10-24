# from django.shortcuts import render
# from watchlist_app.models import Movie
# from django.http import JsonResponse

# # Create your views here.

# def movie_list(request):
#   movies = Movie.objects.all() # get the query_set
#   data = {"Movies": list(movies.values())}  # convert the query_set to dictionary
#   return JsonResponse(data) # return the json response


# def movie_details(request,id):
#   movie = Movie.objects.get(pk=id)
#   my_data = {
#     "Name" : movie.name,
#     "Description" : movie.description,
#     "Active" : movie.active
#   }
#   return JsonResponse(my_data)
