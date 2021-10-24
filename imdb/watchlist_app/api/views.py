from rest_framework import status
from watchlist_app.models import Movie
from watchlist_app.api.serializers import MovieSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view  # for function based views
from rest_framework.views import APIView # for class based views


########################################## CLASS BASED VIEWS ######################################
class MovieList(APIView):

  def get(self,request):
    movies = Movie.objects.all() # get the query set
    my_data = MovieSerializer(movies,many=True) # serialize data to make it python native
    return Response(my_data.data) # return json response

  def post(self,request):
    serializer = MovieSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    else:
      return Response(serializer.errors)


class MovieDetails(APIView):

   def get(self,request,id):
    try:
      movie = Movie.objects.get(pk=id)
    except Movie.DoesNotExist:
      return Response({'error': 'Movie id not found'}, status=status.HTTP_404_NOT_FOUND)
    
    my_data = MovieSerializer(movie)
    return Response(my_data.data)


   def put(self, request, id):
    movie = Movie.objects.get(pk=id)
    serializer = MovieSerializer(movie,data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


   def delete(self,request,id):
    movie = Movie.objects.get(pk=id)
    movie.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)








########################################## FUNCTION BASED VIEWS ######################################

# @api_view(['GET','POST']) # By default set to 'GET"
# def movie_list(request):
#   if request.method == 'GET':
#     movies = Movie.objects.all() # get the query set
#     my_data = MovieSerializer(movies,many=True) # serialize data to make it python native
#     return Response(my_data.data) # return json response

#   if request.method == 'POST':
#     serializer = MovieSerializer(data=request.data)
#     if serializer.is_valid():
#       serializer.save()
#       return Response(serializer.data)
#     else:
#       return Response(serializer.errors)


# @api_view(['GET','PUT','DELETE'])
# def movie_details(request,id):

#   if request.method == 'GET':

#     try:
#       movie = Movie.objects.get(pk=id)
#     except Movie.DoesNotExist:
#       return Response({'error': 'Movie id not found'}, status=status.HTTP_404_NOT_FOUND)
    
#     my_data = MovieSerializer(movie)
#     return Response(my_data.data)

    

#   if request.method == 'PUT':
#     movie = Movie.objects.get(pk=id)
#     serializer = MovieSerializer(movie,data=request.data)
#     if serializer.is_valid():
#       serializer.save()
#       return Response(serializer.data)
#     else:
#       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

#   if request.method == 'DELETE':
#     movie = Movie.objects.get(pk=id)
#     movie.delete()
#     return Response(status=status.HTTP_204_NO_CONTENT)



    