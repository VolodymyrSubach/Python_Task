from django.urls import path, include

from score.views import RestaurantListView, CreateRestaurantView

app_name = 'restaurant'

urlpatterns = [
    path('list/', RestaurantListView.as_view(), name='list'),
    path('create/', CreateRestaurantView.as_view(), name='create')
    ]
