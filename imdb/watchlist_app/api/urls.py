from django.urls import path
# from watchlist_app.api.views import movie_list,movie_details # import function based views
from watchlist_app.api.views import ReviewDetails, ReviewList, WatchListAV,WatchListDetails,StreamPlatformList, StreamPlatformDetails # import class based views

urlpatterns = [
   
    # url for function based views
    # path('list/', movie_list, name='movie-list'),
    # path('<int:id>', movie_details, name="movie-details")

    # url for class based views
    path('list/', WatchListAV.as_view(), name='Watch-List'),
    path('list/<int:id>', WatchListDetails.as_view(), name="WatchList-Details"),
    path('stream/', StreamPlatformList.as_view(), name ='StreamPlatform-List'),
    path('stream/<int:id>', StreamPlatformDetails.as_view(), name="StreamPlatform-Details"),

    # path('review/',ReviewList.as_view(), name="review-list"),
    # path('review/<int:pk>', ReviewDetails.as_view(),name="review-details")

    path('stream/<int:pk>/review',ReviewList.as_view(), name="review-list"),
    path('stream/review/<int:pk>', ReviewDetails.as_view(),name="review-details")
]