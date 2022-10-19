from django.urls import path, include

from score.views import RestaurantListView, EmployeeListView, CreateRestaurantView, UpdateRestaurantView

app_name = 'score'

urlpatterns = [
    path('restaurants/', RestaurantListView.as_view(), name='restaurantslist'),
    path('create_restaurants/', CreateRestaurantView.as_view(), name='create_restaurants'),
    path('update_restaurant/<int:pk>/', UpdateRestaurantView.as_view(), name='update_restaurants'),
    path('employees/', EmployeeListView.as_view(), name='employeeslist'),
    ]
