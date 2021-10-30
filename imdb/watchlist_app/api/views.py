from django.db.models.query import QuerySet
from rest_framework import status
from watchlist_app.models import Review, StreamPlatform, WatchList
from watchlist_app.api.serializers import ReviewSerializer, WatchListSerializer, StreamPlatformSerializer
from rest_framework.response import Response
from rest_framework.decorators import api_view  # for function based views
from rest_framework.views import APIView # for class based views

from rest_framework import generics

########################################## CONCRETE VIEW CLASSES ######################################
class ReviewList(generics.ListCreateAPIView):
  queryset = Review.objects.all()
  serializer_class = ReviewSerializer


class ReviewDetails(generics.RetrieveUpdateDestroyAPIView):
  queryset = Review.objects.all()
  serializer_class = ReviewSerializer



########################################## CLASS BASED VIEWS ######################################
class StreamPlatformList(APIView):
  
   def get(self,request):
    movies = StreamPlatform.objects.all() # get the query set
    my_data = StreamPlatformSerializer(movies,many=True) # serialize data to make it python native
    return Response(my_data.data) # return json response

   def post(self,request):
    serializer = StreamPlatformSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    else:
      return Response(serializer.errors)



class StreamPlatformDetails(APIView):

   def get(self,request,id):
    try:
      movie = StreamPlatform.objects.get(pk=id)
    except StreamPlatform.DoesNotExist:
      return Response({'error': 'id not found'}, status=status.HTTP_404_NOT_FOUND)
    
    my_data = StreamPlatformSerializer(movie)
    return Response(my_data.data)


   def put(self, request, id):
    movie = StreamPlatform.objects.get(pk=id)
    serializer = StreamPlatformSerializer(movie,data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


   def delete(self,request,id):
    movie = StreamPlatform.objects.get(pk=id)
    movie.delete()
    return Response(status=status.HTTP_204_NO_CONTENT)


      
class WatchListAV(APIView):

  def get(self,request):
    movies = WatchList.objects.all() # get the query set
    my_data = WatchListSerializer(movies,many=True) # serialize data to make it python native
    return Response(my_data.data) # return json response

  def post(self,request):
    serializer = WatchListSerializer(data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    else:
      return Response(serializer.errors)


class WatchListDetails(APIView):

   def get(self,request,id):
    try:
      movie = WatchList.objects.get(pk=id)
    except WatchList.DoesNotExist:
      return Response({'error': 'id not found'}, status=status.HTTP_404_NOT_FOUND)
    
    my_data = WatchListSerializer(movie)
    return Response(my_data.data)


   def put(self, request, id):
    movie = WatchList.objects.get(pk=id)
    serializer = WatchListSerializer(movie,data=request.data)
    if serializer.is_valid():
      serializer.save()
      return Response(serializer.data)
    else:
      return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


   def delete(self,request,id):
    movie = WatchList.objects.get(pk=id)
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



    